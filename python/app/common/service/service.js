
/*
*   基本服务工具类 提供访问http的方法 post/get
*
*/
angular.module('com.common')
.service('baseService',['$http', '$q', 'Socket', function($http, $q, Socket){
    this.name = 'this.name';  

    this.post = function(url, params){
        url = url ? url : ' undefined !!!! ';
        params = params ? params : {};
        info("post.url:" + url + ":" + JSON.stringify(params));
        var deferred = $q.defer();
        $http({
            method: 'POST',
            url: url,
            data: params,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            transformRequest: function(data){
                var str = []; 
                for(var key in data){ 
                    str.push(encodeURIComponent(key) + "=" + encodeURIComponent(data[key])); 
                } 
                return str.join("&"); // key1=value1&key2=value2
            }
        }).then(
            function (result) {
                if(resOk(result)){
                    deferred.resolve(result.data);
                }else{
                    deferred.reject(result);
                }
            },
            function (error) {
                deferred.reject(error);   
            }
        );
        return deferred.promise;   
    };


    this.get = function(url, params){
        url = url ? url : ' undefined !!!! ';
        params = params ? params : {};
        info("get.url:" + url + ":" + JSON.stringify(params));
        var deferred = $q.defer();
        $http({
            method: 'GET',
            url: url,
            data: params,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            transformRequest: function(data){
                var str = []; 
                for(var key in data){ 
                    str.push(encodeURIComponent(key) + "=" + encodeURIComponent(data[key])); 
                } 
                return str.join("&"); // key1=value1&key2=value2
            }
        }).then(
            function (result) {
                if(resOk(result)){
                    deferred.resolve(result.data);
                }else{
                    deferred.reject(result);
                }
            },
            function (error) {
                deferred.reject(error);   
            }
        );
        return deferred.promise;   
    };

    this.test = function(url, params, result){
        info("post");
        info("url: " + url );
        info(params);  
        var deferred = $q.defer(); 
        
        deferred.resolve(result); 
          
        return deferred.promise;   
    };



    this.sendSocket = function(eventName, params){
        info("socket " + eventName + " >>>>>>>>>>>>>>>>> ");
        info(params);   
        Socket.send(eventName, params).then(
            function(ack){
                if(ack == 1){
                    info("发送失败");
                }
            }
        );
        //Socket.emit("message", params, function () {} );
    };
    this.sendSocketMsg = function(params){
        this.sendSocket("msg", params);

    };
    this.sendSocketEvent = function(params){
        this.sendSocket("event", params);
    };


}])







//反转 服务调用 返回 result 也要根据参数 决定是否缓存
.service('cacheService', ['$q','LocalStore','baseService', function ($q, LocalStore,baseService) {
    this.name = 'cacheService';
    this.cacheDefaultTime = 60;
    var ifCacheNeedNew = function(lastTime, res, time){
        var date = new Date();
        var delta = date.getTime() - lastTime;
        return !lastTime || !res || !delta || isNaN(delta) ||  delta > time*1000;
    };

    this.post =  function (url,params, time) {
        url = url ? url : ' undefined !!!! ';
        time = time ? (isNaN(time)? this.cacheDefaultTime : parseInt(time)) : this.cacheDefaultTime;
        params = params ? params : {};
        var storeName = url + JSON.stringify(params);   //缓存主键分离
        var storeNameLastTime = storeName + "_last_time";
        var lastTime = LocalStore.get(storeNameLastTime);
        var res = LocalStore.getObject(storeName);
        //超时 或者不存在 从后台获取
        if(ifCacheNeedNew(lastTime, res, time)){
            return baseService.post(url, params).then(function (data) {
                LocalStore.set(storeNameLastTime, (new Date()).getTime());
                LocalStore.setObject(storeName, data);

                var deferred = $q.defer();
                deferred.resolve(data);
                return deferred.promise;
            }, function (error) {
                return $q.reject(error);
            });
        }
        info("post.url:" + url + ":" + JSON.stringify(params) + ':' + time + 's cache');
        var deferred = $q.defer();
        deferred.resolve(res);
        return deferred.promise;
    };

}])



.factory('LocalStore', ['$window', function ($window) {
    return { // 存储单个属性
        set: function(key,value) {
            $window.localStorage.setItem(key, value);
        },
        get: function(key, defaultValue) { // 读取单个属性
            return  $window.localStorage.getItem(key) || defaultValue;
        },
        setObject: function(key, value) { // 存储对象，以JSON格式存储
            $window.localStorage.setItem(key, JSON.stringify(value));
            //$window.localStorage.setItem(key, value);
        },
        getObject: function (key) { // 读取对象
            try {
                return JSON.parse($window.localStorage.getItem(key) || '{}');
            }
            catch(err) {
                return {};
            }
        },
        remove: function (key) {
            $window.localStorage.removeItem(key);
        },
        clear : function (key) {
            $window.localStorage.removeItem(key);
        }
    }
}])
.factory('SessionStorage', ['$window', function ($window) {
    return { // 存储单个属性
        set: function(key,value) {
            $window.sessionStorage.setItem(key, value);
        },
        get: function(key, defaultValue) { // 读取单个属性
            return  $window.sessionStorage.getItem(key) || defaultValue;
        },
        setObject: function(key, value) { // 存储对象，以JSON格式存储
            $window.sessionStorage.setItem(key, JSON.stringify(value));
        },
        getObject: function (key) { // 读取对象
            return JSON.parse($window.sessionStorage.getItem(key) || '{}');
        },
        remove: function (key) {
            $window.sessionStorage.removeItem(key);
        },
        clear : function (key) {
            $window.sessionStorage.removeItem(key);
        }
    }
}])



 /**
 *  同步队列服务，将需要顺序执行的方法和参数传入，确保按照顺序依次执行。
 *  要求传入的方法返回promise对象，最后一个参数如果是函数类型，则作为回调函数执行。
 *  使用方法如下：
 *  SyncQueue(typeString, notPromise).push(obj, method, param1, param2, ..., callback);
 *
 *  typeString: 队列类型名称，支持多组队列各种同步，如果为null则使用缺省名字为：default的队列
 *  notPormise: 队列方法采用promise.then方式表明执行完成还是callback表明执行完全，缺省不设置为promise类型
 */
.factory('SyncQueue', ['$q', '$rootScope', function ($q, $rootScope) {
    var queue = {}, status = {}, nPromise = {};
    return function (type, notPromise) {
        var init = function () {
            queue[type] = [];
            status[type] = 'ready';
            nPromise[type] = notPromise;
        };
        type = type || 'default';
        if (!queue[type]) { // 不存在此类队列，初始化各类状态状态，否则沿用前面的状态
            init();
        }
        return {
            /**
             * 提交待执行方法到队列
             * @param obj: 方法所属对象，方法执行的上下文环境
             * @param mothod: 可以为字符串，或者实际的方法体内容
             *
             * 注意：要求method和callback使用obj作为自身的上下文
             */
            push: function (obj, method) {
                var args = [].slice.call(arguments, 2);
                if (typeof method !== 'function') {
                    method = obj[method];
                }
                var callback = args[args.length - 1];
                if (typeof callback !== 'function') {
                    args.push(function () {
                    });
                }
                queue[type].push({"obj": obj, "method": method, "args": args});
                this._next();
            },
            isFinish: function () {
                var deferred = $q.defer();
                if (queue[type].length == 0 && status[type] == 'ready') {
                    deferred.resolve();
                } else { // 等待接收完成消息，返回完成通知
                    $rootScope.$on('sync_queue:finish:' + type, function () {
                        deferred.resolve();
                    });
                }
                return deferred.promise;
            },
            /**
             * 清理队列状态
             * 网络重连后执行此方法确保队列状态恢复
             */
            clear: function () {
                init();
            },
            _next: function () {
                if (status[type] == 'ready') {
                    var req = queue[type].shift();
                    if (req) {
                        var obj = req.obj;
                        var method = req.method;
                        var args = req.args;
                        var callback = args[args.length - 1];
                        var next = function () {
                            var newArgs = Array.prototype.slice.call(arguments);
                            callback.apply(obj, newArgs.concat([queue[type].length])); //执行回调方法
                            status[type] = 'ready';
                            that._next();
                        }
                        status[type] = 'pendding';
                        var that = this;
                        if (nPromise[type]) { //非promise的则要求最后一个参数为回调函数
                            args[args.length - 1] = next;
                            method.apply(obj, args);
                        } else {
                            method.apply(obj, args).then(next, next);
                        }
                    } else { //没有待执行的任务，广播完成消息
                        status[type] = 'ready';
                        $rootScope.$broadcast('sync_queue:finish' + type);
                    }
                }
            }
        };
    };
}])













  /**
 * 图片预览
 */
.provider('Preview', function () {
    return {
        $get: ['$rootScope', '$document', '$compile', function ($rootScope, $document, $compile) {
            var n = {
                /**
                 * 预览图片
                 * @param param {"current": "当前图片的索引", "imageList": "图片urls", "config":{"showDownload": true/false是否显示下载按钮}}
                 * @returns {boolean}
                 */
                openList: function (param) {
                    if (!param.imageList || param.imageList.length <= 0) return !1;
                    n.instance && (n.instance.close(), n.instance = null);
                    if(!param.config) param.config = {"showDownload": true};
                    if(!param.current) param.current = 0;
                    var a = {};
                    n.isOpen = !0, param = param || {}, angular.extend(a, param);
                    var newScope;
                    newScope = $rootScope.$new(), angular.extend(newScope, {
                        imageList: param.imageList,
                        current: param.current,
                        config: param.config
                    });
                    var template = angular.element('<div preview-directive class="J_Preview" config="config" current="current" image-list="imageList"></div>'),
                        compileTmpl = $compile(template)(newScope),
                        bodyEle = $document.find("body").eq(0);
                    bodyEle.append(compileTmpl);
                    var u = {
                        close: function () {
                            var e = compileTmpl.scope();
                            e && e.$destroy(), compileTmpl.remove()
                        }
                    };
                    return n.instance = u, u;
                },
                open : function(imgurl){
                    var imageList = [];
                    imageList.push(imgurl);
                    var param = {};
                    param['imageList'] = imageList;
                    param['current'] = 0;
                    this.openList(param);
                }
            };
            return n;
        }]
    };
})  