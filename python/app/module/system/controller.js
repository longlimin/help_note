 
angular.module('com.system')

.controller('com.system.pageCtrl', ['$scope', '$rootScope', '$state','$interval','systemService','Preview', 
    function ($scope, $rootScope, $state, $interval, systemService, Preview) {
    //嵌套路由 scope可访问 <任意module> 的上层html的 ctrl/scope

    $scope.goHome = function(){ 
        $state.go('main.system.list');
    }
    $scope.goAdd = function(){ 
        $state.go('main.system.add');
    }
    $scope.goUpdate = function(id){
        var params = {"id":id};
        $state.go('main.system.update', params);
    }
  
    $scope.clickPort = function(item){
        systemService.setports(item).then(
        function (data) { 
            info(data); 
            $scope.ports = data;
        }, error); 
    }
    $scope.clickTurnCamera = function(value){
        var params = {'value':value}
        systemService.turnCamera(params).then(
            function (data) { 
                info(data);  
        }, error); 
    } 
    $scope.clickMove = function(value){
        var params = {'value':value}
        systemService.move(params).then(
        function (data) { 
            info(data);  
        }, error); 
    } 




    $scope.keydown = function(event){
        if (event.keyCode == 13) {
            $scope.clickWrite();
        }   
    };
    $scope.dbclick = function(event){
        // Preview.open( $scope.image );
    }
    //发送消息
    $scope.clickWrite = function(){
        var params = SocketMake(SOCKET_MSG);
        params["value"] = $scope.taWrite;
        systemService.sendSocketMsg(params);
    };
    $scope.clickListen = function(){
        var params = SocketMake(SOCKET_MV);
        params["value"] = "start";
        systemService.sendSocketMsg(params);
    };
    //广播监听接收结果
    $scope.$on(SOCKET_MSG, function (event, data) {
        // $scope.taRead = data;//绑定更新太慢
        $("#read").val(toStr(data));
    });
    $scope.$on(SOCKET_MV, function (event, data) {
        $("#read").val(toStr(data));
    });
    systemService.getports("").then(
        function (data) { 
            info(data);
            //debugger;  
            $scope.ports = data;
        }, error);  

    var i = 0;
    //定时获取图片 延时问题？？？图片压缩 访问优化 
    var timer=$interval(function(){
        // $scope.image = $scope.image ? '' : "resource/image/frame" + i + ".png";
        //路径同名  浏览器不会重新加载图片
        var yyy = getTheDate("yyyyMMddhhmm", -1000);
        var ss = parseInt(getTheDate("ss", -1000));
        var sss = parseInt(ss / 10);
        $scope.image = "resource/image/frame" + yyy + sss + ".png";
        i++;
    },10000);   //间隔2秒定时执行

    timer.then(function(){ info('定时器创建成功')},
    function(){ info('定时器创建不成功')} );
    $scope.image = "resource/image/test.png";
    $scope.video = "resource/video/198.MP4"; 






}]) 