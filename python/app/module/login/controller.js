 
angular.module('com.login')

.controller('com.login.pageCtrl', ['$scope', '$rootScope', '$state', 'loginService', function ($scope, $rootScope, $state, loginService) {
    //嵌套路由 scope可访问 <任意module> 的上层html的 ctrl/scope
    info("com.login.pageCtrl");
    $scope.goHome = function(){ 
        $state.go('main');
    }  
 
    $scope.login = function(){ 
        //debugger; 
        var params = $scope.form;  
          //按月统计，每月注册人数 
        loginService.login(params).then(
            function (data) { 
                debugger;
                info(data); 
                $('#loginModal').modal('hide');

                $rootScope.isLogined = true;
                $scope.goHome();
            }, error);  
    }; 
 
    $scope.registe = function(){ 
        //debugger; 
        var params = $scope.formr;  
          //按月统计，每月注册人数 
        loginService.registe(params).then(
            function (data) { 
                // debugger;
                info(data); 
                alert(data);
            }, error);  
    }; 



}]) 
