 

 
angular.module('com.lunch', [])
.config(['$urlRouterProvider', '$stateProvider',  function ($urlRouterProvider, $stateProvider) {
   
    var mName = 'lunch';

    //定义层级路由 url路径 参数 绑定controller
    $stateProvider
        .state('main.' + mName, {
            url: '/' + mName,
            templateUrl: 'module/' + mName + '/template/page.html',
            controller: 'com.' + mName + '.pageCtrl'
        })
        .state('main.' + mName + '.list', {
            url: '/list',
            templateUrl: 'module/' + mName + '/template/list.html',
            controller: 'com.' + mName + '.listCtrl' 
        })
        .state('main.' + mName + '.add', { 
            url: '/add',
            templateUrl: 'module/' + mName + '/template/add.html',
            controller: 'com.' + mName + '.addCtrl' 
        })
        .state('main.' + mName + '.update', {
            url: '/update:id',
            templateUrl: 'module/' + mName + '/template/update.html',
            controller: 'com.' + mName + '.updateCtrl' 
        })  
    ; 

}]);



 