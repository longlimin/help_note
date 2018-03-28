 
angular.module('com.tomcat')
.controller('com.tomcat.indexCtrl', ['$scope', '$rootScope', '$state', 'tomcatService', function ($scope, $rootScope, $state, tomcatService) {
    //该index.html包含两个容器ui-view
    //跳转到下一个路由 state view会包含两个url 和 contrl
    $state.go('main.tomcat.index');
 
}])
.controller('com.tomcat.navCtrl', ['$scope', '$rootScope', '$state', 'tomcatService', function ($scope, $rootScope, $state, tomcatService) {
 
     
 
}])
.controller('com.tomcat.pageCtrl', ['$scope', '$rootScope', '$state', 'tomcatService', function ($scope, $rootScope, $state, tomcatService) {
    //嵌套路由 scope可访问 <任意module> 的上层html的 ctrl/scope
     
    $scope.goHome = function(){ 
        $state.go('main.tomcat');
    }  

    $scope.statis = function(){ 
        //debugger; 
        var params = {"URL":$scope.query};  
        //若有url参数则分时间段 分时统计该url访问耗时
        tomcatService.statis(params).then(
        function (data) {  
            info(data);
            //debugger; 
            $scope.option = data.option;
            if($scope.queryUrl == null){ 
                data.option.xAxis.data.push("");
                $scope.queryUrl =  data.option.xAxis.data;
            }
            toolSetChart("echarts", data.option);
        }, error);  

        //若有url参数则分时间段 分时统计该url访问耗时
        tomcatService.statisCount(params).then(
        function (data) {  
            info(data);
            //debugger; 
            $scope.option = data.option;
            if($scope.queryUrlCount == null){
                data.option.xAxis.data.push("");
                $scope.queryUrlCount =  data.option.xAxis.data;
            }
            toolSetChart("echarts_count", data.option);
        }, error);  
    };
    $scope.statis(); 
    $scope.urlChange = function(){
        $scope.statis();   
    };  
 
  

}]) 
