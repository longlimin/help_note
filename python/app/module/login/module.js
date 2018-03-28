 

 
angular.module('com.login', [])
.config(['$urlRouterProvider', '$stateProvider',  function ($urlRouterProvider, $stateProvider) {
        //$urlRouterProvider.when('', '/main/student');

        //定义层级路由 url路径 参数 绑定controller
        $stateProvider
        .state('login', {
            url: '/login',
            templateUrl: 'module/login/template/page.html',
            controller: 'com.login.pageCtrl'
        }) 
         ; 

}]);



 