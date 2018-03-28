 

angular.module('com.main', []) 
.config(['$stateProvider', function ($stateProvider) {

    $stateProvider.state('main',{
        url: '/main',
        templateUrl: 'module/main/template/page.html', 
        controller: 'com.main.pageCtrl'
    }).state('main.home',{
        url: '/home',
        templateUrl: 'module/main/template/home.html', 
        controller: 'com.main.homeCtrl'
    }).state('main.home.morestudent',{
        url: '/morestudent',
        templateUrl: 'module/student/template/list.html', 
    }) 


    ;


}]); 