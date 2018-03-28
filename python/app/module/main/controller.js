 
angular.module('com.main') 

.controller('com.main.pageCtrl', ['$scope', '$rootScope', '$state', function ($scope, $rootScope, $state) {
    //嵌套路由 scope可访问 <任意module> 的上层html的 ctrl/scope
    
    $scope.goHome = function(){ 
        $state.go('main.home');
    }
    $scope.goMoreStudent = function(){ 
        $state.go('main.student.list');  
    }

    var logined = $rootScope.isLogined ;
    if (logined == true) { // 已经登录 
       // $state.go('main'); 
    } else { // 没有登录   
       $state.go('login'); 
    }  

    info($state.current.name);




}]) 
.controller('com.main.homeCtrl', ['$scope', '$rootScope', '$state', 'studentService', function ($scope, $rootScope, $state, studentService) {
 
    var params = {"count":3};
    studentService.listRecent(params).then(
        function (data) {  
            info(data)
           // debugger;
            $scope.httplist = data; 
    });   

}]) 