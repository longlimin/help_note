 

 
angular.module('com.tomcat', [])
.config(['$urlRouterProvider', '$stateProvider',  function ($urlRouterProvider, $stateProvider) {
        //$urlRouterProvider.when('', '/main/tomcat');

        //定义层级路由 url路径 参数 绑定controller
        $stateProvider
        .state('main.tomcat.index', {
            //abstract: true,
            url: '/index',  //子层级不需要包括父级路径
            views: {
                navView: {
                    templateUrl: 'module/tomcat/template/nav.html',
                    controller: 'com.tomcat.navCtrl'
                },
                contentView: {
                    templateUrl: 'module/tomcat/template/page.html',
                    controller: 'com.tomcat.pageCtrl'
                }
            }
        })
        .state('main.tomcat', {
            url: '/tomcat',
            templateUrl: 'module/tomcat/template/index.html',
            controller: 'com.tomcat.indexCtrl'
        }) 
        
        ;

}]);



 