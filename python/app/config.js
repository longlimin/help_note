/**
 * Created by chensheng on 16/8/30.
 */

(function () { 'use strict'; 


    /**
     * 注意：
     * 1、单独部署服务器需要启用反向代理，反向代理前缀为$ProxyPrefix的值，$Service在单独部署时需要用上，例如访问新闻页面就不能使用反向代理，否则样式会错乱
     * 2、和服务器部署在一起需要把$Service和$ProxyPrefix都置为空
     * 3、$UEDITOR_HOME_URL是富文编辑器的工作目录配置
     */
    angular.module('com.config', [])
        .constant('$ProxyPrefix', '/api') // 设为空字符串则取消反向代理
        .constant('$Service', 'http://cochat.cn/') // 默认服务器地址,有些地方需要用到，例如访问信息号下发的新闻
        .constant('$UEDITOR_HOME_URL', '/scripts/ueditor/') // 打包时改成'/desktop/scripts/ueditor/'
        .constant('$HomeStateName', 'com.student') // 默认主页
        .constant('$Title', '软虹科技工作平台') // 首页显示的title
        .constant('$Platform', 'DESKTOP') // 桌面版众信
        .constant('$Version', '2.5.1') // 众信桌面版本号
        .constant('$PlatformVersion', window.navigator.platform) // 浏览器平台
        .config(['$provide', function($provide) {
            $provide.decorator("$exceptionHandler", ['$delegate', '$injector', function($delegate, $injector) {
                return function(exception, cause) {
                    $delegate(exception, cause);
                    var $log = $injector.get('$log');
                    $log.error(exception.message + ', ' + exception.stack);
                };
            }]);
        }])
        .config(['$httpProvider', '$logProvider', function($httpProvider, $logProvider){
            $httpProvider.defaults.withCredentials = true;
            $httpProvider.interceptors.push('SecurityInterceptor'); // 权限拦截器
            $logProvider.debugEnabled(true);
        }])
        .run(['$rootScope', '$state', '$stateParams',
            function ($rootScope, $state, $stateParams) {
                // It's very handy to add references to $state and $stateParams to the $rootScope
                // so that you can access them from any scope within your applications.For example,
                // <li ng-class="{ active: $state.includes('contacts.list') }"> will set the <li>
                // to active whenever 'contacts.list' or one of its decendents is active.
                $rootScope.$state = $state;
                $rootScope.$stateParams = $stateParams;
            }
        ]);

})();