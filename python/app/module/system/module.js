 

 
angular.module('com.system', [])
.config(['$urlRouterProvider', '$stateProvider',  function ($urlRouterProvider, $stateProvider) {
        //$urlRouterProvider.when('', '/main/system');

        //定义层级路由 url路径 参数 绑定controller
        $stateProvider
        .state('main.system', {
            url: '/system',
            templateUrl: 'module/system/template/page.html',
            controller: 'com.system.pageCtrl'
        })
        .state('main.system.list', {
            url: '/list',
            templateUrl: 'module/system/template/list.html',
            controller: 'com.system.listCtrl' 
        })
        .state('main.system.add', {
            url: '/add',
            templateUrl: 'module/system/template/add.html',
            controller: 'com.system.addCtrl' 
        })
        .state('main.system.update', {
            url: '/update/:id',
            templateUrl: 'module/system/template/update.html',
            controller: 'com.system.updateCtrl' 
        })  
         ; 

}]);



 