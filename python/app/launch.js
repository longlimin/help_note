/*
    程序入口
    AppCtrl
    AppModule
    配置root路由
*/
 
var easyuiTheme = "metro-blue";//指定如果用户未选择样式，那么初始化一个默认样式 

var subModules = [ // 需要加载的子模块集合
    //系统模块
    'ui.router',  
    
    //自定义模块
    'com.common', 
    'com.login',
    'com.tomcat', 
    'com.student', 
    'com.main',
    'com.file',
    'com.table', 
    'com.lunch', 
    'com.dinner',


    'com.system'
    //'com.config',
]; 


/* 使用ui-router来进行路由定义，需要注入ui.router模块 */
var app = angular.module('App', subModules);
app

//常量集合 配置文件
.constant('$SOCKET_ADDR', '127.0.0.1:8087')  
.constant('$ADDR_LOCAL', 'http://127.0.0.1:8088/app')  
.constant('$PROJECT', 'BaseSSM')  


/* 注入$stateProvider，$urlRouterProvider */
.config(['$stateProvider', '$urlRouterProvider', function ( $stateProvider, $urlRouterProvider ) {
   
    //使用when来对一些不合法的路由进行重定向  
    $urlRouterProvider.when('', '/main')   
    /**
     * 默认跳转到主页面
     */
   // $urlRouterProvider.otherwise('/main');
    //通过$stateProvider的state()函数来进行路由定义   
    $stateProvider.state('hello', {
        url: '/hello',
        template: '<h3>hello !</h3>'
    }).state('world', {
        url: '/world',
        template: '<h3> world!</h3><a ui-sref="world.world1" ui-sref-active="active">/world/world1</a> <div ui-view></div>'
    }).state('world.world1', {
        url: '/world/world1',
        template: '<h3>This is a World 1</h3>'
    }).state('world2', {
        url: '/world/world2',
        template: '<h3>world2并不依赖于world，在我们点击它的时候，他会替换掉index.html中的<div ui-view></div></h3>'
    })

}])
// 系统事件处理
.run(['$rootScope', 'Socket', 
function ($rootScope, Socket) { 
  // 用户登录成功
  $rootScope.$on('system:login', function () {
      info("收到事件system:login")
      info("发出事件socket:connect")
      $rootScope.$broadcast('socket:connect');
  });

  // 用户退出
  $rootScope.$on('system:logout', function () {
      info("收到事件system:logout")
      $rootScope.isLogined = false;
      Socket.disconnect(); 
  });

  // 恢复应用
  $rootScope.$on('system:resume', function () {
      info("收到事件system:resume")
      $rootScope.$broadcast('socket:connect');
  });

  // 登录消息服务器
  $rootScope.$on('socket:connect', function () {
      info("收到事件socket:connect")
      Socket.connect();
  }); 
}])
/*
首先，和原生ng-route路由模块相似的是，必须先把ui-route注入。然后再进行具体的配置。与原生的ng-route不同的是，ui-route用state() 代替了原生的when() ，它在when()，的基础上新增了一个参数，这里是index，用以区分这部分路由对哪一个命令进行响应。
回到之前的<div><a ui-sref = "index">首页</a></div> ，大概就知道他们视图和它之间的关系了。ui-view 代替了以往的ng-view ，ui-sref 替换掉了以前的ng-href，而它也不再是指向链接，而是指向“导航”的名字。
其中的url属性可以唯一标识改路由的后续地址，用以跟后面的路由进行区分。
*/
.controller('AppCtrl', ['$scope', '$rootScope', '$state', function ($scope, $rootScope, $state ) {  
    console.log("test execute service,provider,factory"); 
    $rootScope.isLogined = $rootScope.isLogined == null ? false:$rootScope.isLogined;
    info($rootScope.isLogined); 
 
    $rootScope.isLogined = true;
    //$rootScope.$broadcast('system:login');




}])











