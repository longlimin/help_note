 
angular.module('com.student')

.controller('com.student.pageCtrl', ['$scope', '$rootScope', '$state', 'studentService', function ($scope, $rootScope, $state, studentService) {
    //嵌套路由 scope可访问 <任意module> 的上层html的 ctrl/scope
     
  
    $scope.goHome = function(){ 
        $state.go('main.student.list');
    }
    $scope.goAdd = function(){ 
        $state.go('main.student.add');
    }
    $scope.goUpdate = function(id){
        var params = {"id":id};
        $state.go('main.student.update', params);
    }
   

    $('#charttimefrom').datetimepicker();
    $('#charttimeto').datetimepicker(); 
    $scope.chart = {}; //查询 
    $scope.chart.TIMEFROM = "2015";
    $scope.chart.TIMETO = "2017";
    $scope.statis = function(){ 
        //debugger; 
        var params = $scope.chart;  
          //按月统计，每月注册人数 
        studentService.statis(params).then(
        function (data) { 
            // debugger;
            info(data);
            //data.option = $.extend({"yAxis":{}}, data.option )
            toolSetChart("echarts", data.option);
        }, function(error){
            alert("eeeeeeeeeeeee");
        });  
    };
    $scope.statis();
 
  




}])
.controller('com.student.addCtrl', ['$scope', '$rootScope', 'studentService', function ($scope, $rootScope, studentService) {
    

    $('#time').datetimepicker();
    $scope.ajaxSubmit = function(){ 
        var params =  $scope.httpget;
        studentService.update(params).then(
            function (data) {
                info("操作数据:" + data.res + "条");
                $scope.goHome();
        }, error); 
    };
}])
.controller('com.student.updateCtrl', ['$scope', '$rootScope', '$stateParams', 'studentService', function ($scope, $rootScope, $stateParams, studentService) {
    

    $scope.params = $stateParams;
    info("stateParams"); 
    info($scope.params); 
    var params = $scope.params;
    studentService.get(params).then(        
        function (data) {
            $scope.httpget = data; 
        }, error); 
 

    $('#time').datetimepicker();
    $scope.ajaxSubmit = function(){  
        var params = $scope.httpget;
        studentService.update(params).then(
            function (data) {
                info("操作数据:" + data.res + "条");
                $scope.goHome(); 
            }, error);  

    };
}])
.controller('com.student.listCtrl', ['$scope', '$rootScope', '$state', 'studentService', function ($scope, $rootScope, $state, studentService) { 
    

    //bootstrap日期插件使用方式 
    $('#timefrom').datetimepicker();
    $('#timeto').datetimepicker(); 
    
    $scope.search = {}; //查询
    $scope.orderType = 'id'; 
    $scope.order = '-';
    $scope.changeOrder = function(type){
        $scope.orderType = type;
        if($scope.order === ''){
            $scope.order = '-';
        }else{
            $scope.order = '';
        }
    };
    $scope.list = function(){ 
        //debugger;
        var PAGE = $scope.PAGE;
        var search = $scope.search;
        params = $.extend({}, PAGE, search); 
        studentService.list(params).then(
            function (data) {
                $scope.httplist = data.res;
                $scope.PAGE = data.PAGE; 
                $scope.ppp = calcPage($scope.PAGE);
        }, error);  

    };
    $scope.list();

    $scope.ajaxDelete = function(id){ 
        var params = {"ID":id};
        studentService.del(params).then(
            function (data) { 
                info("操作数据:" + data.res + "条");
                $scope.list(); 
        }, error);  

    }  
}])


