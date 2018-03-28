angular.module('com.common')

//本终端的登陆状态数据 全局静态变量集合
.factory('Connection', ['$rootScope', '$log', '$timeout', function($rootScope, $log, $timeout) {
    var state = 2;
    function online(msg) {
        $timeout(function () {
            state = 1;
        });
        $log.log('online:' + getType());
    }
    function offline() {
        $timeout(function () {
            state = 2;
        });
        $log.log('offline:' + getType());
    }
    function noconnect() {
        if (state != 2) { //前提为非未连接状态
            $timeout(function () {
                state = 3;
            });
            $log.log('noconnect:' + getType());
        }
    }
    function connecting() {
        $timeout(function () {
            state = 4;
        });
        $log.log('connecting:' + getType());
    }
    function getType() {
        if (navigator.network && navigator.network.connection) {
            return navigator.network.connection.type;
        } else {
            return state;
        }
    }
    return {
        netState: function() {
            return state;
        },
        online : function() {
            return state == 1;
        },
        setOnline : function(msg) {
            online(msg);
        },
        setOffline : function() {
            offline();
        },
        setConnecting : function() {
            connecting();
        },
        setNoconnect : function() {
            noconnect();
        }
    };
}]) 

//客户端socket 控制 中心 
//发消息：Socket.emit(eventName, data, callback) 
//收消息：广播 $rootScope.$broadcast("socket:" + data.category, data);
.factory('Socket', ['$q', '$http', '$rootScope', 'Connection', '$log', '$timeout', '$SOCKET_ADDR', function($q, $http, $rootScope, Connection, $log, $timeout, $SOCKET_ADDR){
    var socket; // socket对象
    var logined = false; // 是否已经登录
    var disconnect_flag = false; // 主动断开标志
    var reconnect_timeout = 1000; // 断开超时重连时间

    function test(url, params, result){
        info("post");
        info("url: " + url );
        info(params);  
        var deferred = $q.defer(); 
        deferred.resolve(result); 
        return deferred.promise;   
    };

    // 创建socket对象
    function doConnect() {  
        info('socket addr: ' + $SOCKET_ADDR);
        var defer = $q.defer();
        if (socket) { //已有连接socket
            defer.resolve(socket); 
        } else {    //新建连接socket
            var config = {
                transports:['websocket', 'polling'], // websocket优先
                timeout:30 * 1000, // 超时时间
                forceNew: true,
                reconnection : false
            };
            socket = io($SOCKET_ADDR, config);
            socket.on('connect', function () { // 监听连接事件，自动登录处理，登录成功返回socket
                $log.log('socket connected!');
                //$q.all 执行多个异步任务进行回调，接受一个promise的数组
                $q.all([test('http://test.com', {'id':101,'name':'walker'}, -1)]).then(
                    function (params) { //params即为参数返回的集合 params[0] = service.post(url, args); 实现socket依赖http的认证登陆
                        $log.log('socket login result:' + params[0]);
                        Connection.setOnline('login ok ? online');
                    }
                );
            });
            socket.on('disconnect', function () {
                Connection.setNoconnect();
                $log.log('socket disconnected!');
                if (!disconnect_flag) { // 被动断开，超时重连
                    disconnect_flag = false;
                    setTimeout(function () {
                        socket.connect();
                    }, reconnect_timeout);
                }
            });
            socket.on('error', function (error) {
                Connection.setNoconnect();
                setTimeout(function () {
                    socket.connect();
                }, reconnect_timeout);
            });
            socket.on('connect_error', function(error){
                Connection.setNoconnect();
                setTimeout(function () {
                    socket.connect();
                }, reconnect_timeout);
            });
            socket.on('connect_timeout', function(){
                Connection.setNoconnect();
                setTimeout(function () {
                    socket.connect();
                }, reconnect_timeout);
            });
            socket.on("connecting", function (data) {
                Connection.setConnecting();
            });
            socket.on("reconnecting", function (data) {
                Connection.setConnecting();
            });   
// socket.emit('action');表示发送了一个action命令，命令是字符串的，在另一端接收时，可以这么写： socket.on('action',function(){...});
// socket.emit('action',data);表示发送了一个action命令，还有data数据，在另一端接收时，可以这么写： socket.on('action',function(data){...});
// socket.emit(action,arg1,arg2); 表示发送了一个action命令，还有两个数据，在另一端接收时，可以这么写： socket.on('action',function(arg1,arg2){...});
// 在emit方法中包含回调函数，例如：
//socket.emit('action',data, function(arg1,arg2){...} );那么这里面有一个回调函数可以在另一端调用，另一端可以这么写：socket.on('action',function(data,fn){   fn('a','b') ;  });
            // 注册监听message，并广播
            socket.on('message', function (data, ackServerCallback) {
                data = JSON.parse(data)
                info("socket message <<<<<<<<<<<<<<<<");
                info(data);
                $rootScope.$broadcast("socket:message", data); 
            });
            socket.on('event', function (data, ackServerCallback) {
                data = JSON.parse(data)

                info("socket event <<<<<<<<<<<<<<<<");
                info(data);
                $rootScope.$broadcast("socket:event", data); 
            });
            socket.on('msg', function (data, ackServerCallback) {
                data = JSON.parse(data)

                info("socket msg <<<<<<<<<<<<<<<<");
                var key = SocketGetKey(data);
                info(key);
                info(data);
                $rootScope.$broadcast(key, data); 
            });





           
        }
        return defer.promise;
    }

    //socket单例工厂
    function getSocket() {
        var deferred = $q.defer();
        if (socket) {
            // if (logined) { // 已连接并登录，直接返回socket
            //     deferred.resolve(socket);
            // } else { 
            //     // 等待登录成功再返回socket
            //      $rootScope.$on("socket:login", function () {
            //          deferred.resolve(socket);
            //      });
            // }
            deferred.resolve(socket);
        } else {
            doConnect().then(function(){
                deferred.resolve(socket);
            }, function(){
                deferred.resolve(undefined);
            });
        }
        return deferred.promise;
    }

    return {
        connect: function(){
            getSocket().then(function(socket){
                disconnect_flag = false;
                if (socket) {
                    socket.connect();
                }
            });
        },
        disconnect: function(){
            getSocket().then(function(socket){
                disconnect_flag = true;
                if (socket) {
                    socket.disconnect();
                }
            });
        },
        //发送消息 结果 回调函数
        emit: function (eventName, data, callback) {
            $log.log("socket:emit:" + eventName);
            getSocket().then(function (socket) {
                if (socket) {
                    socket.emit(eventName, data, function (ackData) {
                        $log.log("socket:emit:" + eventName + "   return!");
                        info(ackData);
                        if (callback) {
                            $timeout(function () {
                                callback(ackData);
                            });
                        }
                    });
                } else {
                    if (callback) {
                        $timeout(function () {
                            callback();
                        });
                    }
                }
            });
        },
        //发送消息 返回promise 成功或者失败
        send: function (eventName, data) {
            var defer = $q.defer(); 
            getSocket().then(function (socket) {
                if (socket) {
                    socket.emit(eventName, data);
                    defer.resolve(0); 
                }else{
                    defer.resolve(1); 
                }
            }); 
            return defer.promise;   
        }
    }
}




]);

