 

 
angular.module('com.file', [])
.config(['$urlRouterProvider', '$stateProvider',  function ($urlRouterProvider, $stateProvider) {
    
        //定义层级路由 url路径 参数 绑定controller
        $stateProvider
        .state('main.file', {
            url: '/file',
            templateUrl: 'module/file/template/page.html',
            controller: 'com.file.pageCtrl'
        })
        .state('main.file.list', {
            url: '/list',
            templateUrl: 'module/file/template/list.html',
            controller: 'com.file.listCtrl' 
        })
        .state('main.file.add', {
            url: '/add',
            templateUrl: 'module/file/template/add.html',
            controller: 'com.file.addCtrl' 
        })
        .state('main.file.update', {
            url: '/update:id',
            templateUrl: 'module/file/template/update.html',
            controller: 'com.file.updateCtrl' 
        })  
         ; 

}]);



 