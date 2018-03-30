 
angular.module('com.common') 

.controller('com.common.pageCtrl', ['$scope', '$rootScope', '$state', 'service', function ($scope, $rootScope, $state, service) {
    //嵌套路由 scope可访问 <任意module> 的上层html的 ctrl/scope
     
    $scope.goHome = function(){ 
        $state.go('main.home');
    }
  
}]) 

