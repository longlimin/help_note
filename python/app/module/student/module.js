 

 
angular.module('com.student', [])
.config(['$urlRouterProvider', '$stateProvider',  function ($urlRouterProvider, $stateProvider) {
        //$urlRouterProvider.when('', '/main/student');

        //定义层级路由 url路径 参数 绑定controller
        $stateProvider
        .state('main.student', {
            url: '/student',
            templateUrl: 'module/student/template/page.html',
            controller: 'com.student.pageCtrl'
        })
        .state('main.student.list', {
            url: '/list',
            templateUrl: 'module/student/template/list.html',
            controller: 'com.student.listCtrl' 
        })
        .state('main.student.add', {
            url: '/add',
            templateUrl: 'module/student/template/add.html',
            controller: 'com.student.addCtrl' 
        })
        .state('main.student.update', {
            url: '/update/:id',
            templateUrl: 'module/student/template/update.html',
            controller: 'com.student.updateCtrl' 
        })  
         ; 

}]);



 