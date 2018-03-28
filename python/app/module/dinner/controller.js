 
angular.module('com.dinner')

.controller('com.dinner.pageCtrl', ['$scope', '$rootScope', '$state', 'dinnerService', function ($scope, $rootScope, $state, dinnerService) {
    //嵌套路由 scope可访问 <任意module> 的上层html的 ctrl/scope
    var mName = 'dinner';
    $scope.mName = mName;
  
    $scope.goHome = function(){ 
        $state.go('main.' + mName + '.list');
    }
    $scope.goAdd = function(){ 
        $state.go('main.' + mName + '.add');
    }
    $scope.goUpdate = function(id){
        var params = {"id":id};
        $state.go('main.' + mName + '.update', params);
    }
   

    $('#charttimefrom').datetimepicker();
    $('#charttimeto').datetimepicker();
    var yyyymm = getDate('yyyy-MM');
    $scope.chart = {}; //查询
    $scope.chart.TIMEFROM = yyyymm;
    $scope.chart.TIMETO = yyyymm;
    $scope.statis = function(){ 
        var params = $scope.chart;
        dinnerService.statis(params).then(
        function (data) { 
            info(data);
            //data.option = $.extend({"yAxis":{}}, data.option )
            toolSetChart("echarts", data.option);
        },error);  
    };
    $scope.statis();

}])
.controller('com.dinner.addCtrl', ['$scope', '$rootScope', 'dinnerService', function ($scope, $rootScope, dinnerService) {
    $scope.httpget = {};

    $scope.httpget[$rootScope.cols[0]] = getDate('yyyy-MM-dd');

    var params = {};
    params[$rootScope.cols[0]] = getTheDay('yyyy-MM-dd', -1);
    dinnerService.get(params).then(
        function (data) {
            $scope.httpget = data;
            $scope.httpget[$rootScope.cols[0]] = getDate('yyyy-MM-dd');
    }, error);

    $scope.ajaxSubmit = function(){
        var params =  $scope.httpget;
        dinnerService.add(params).then(
            function (data) {
                info("操作数据:" + data.res + "条");
                $scope.goHome();
        }, error); 
    };
}])
.controller('com.dinner.updateCtrl', ['$scope', '$rootScope', '$stateParams', 'dinnerService', function ($scope, $rootScope, $stateParams, dinnerService) {

    $scope.httpget = {};

    $scope.params= $stateParams;
    info("stateParams:" + JSON.stringify($scope.params));

    var params = {};
    params[$rootScope.cols[0]] = $scope.params.id;
    dinnerService.get(params).then(
        function (data) {
            $scope.httpget = data; 
    }, error);
 

    $scope.ajaxSubmit = function(){
        var params = $scope.httpget;
        dinnerService.update(params).then(
            function (data) {
                info("操作数据:" + data.res + "条");
                $scope.goHome(); 
            }, error);  

    };
}])
.controller('com.dinner.listCtrl', ['$scope', '$rootScope', '$state', 'dinnerService', function ($scope, $rootScope, $state, dinnerService) { 
    $scope.refresh = true;
    var openLoading = function(){
        $scope.refresh = true;
    };
    var closeLoading = function(){
        $scope.refresh = false;
    };

    //加载页面
    var loadPage = function(){
        
        $scope.search = {}; //查询
        $scope.orderType = $rootScope.cols[0];
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
            var PAGE = $scope.PAGE;
            var search = $scope.search;
            params = $.extend({}, PAGE, search); 
            dinnerService.list(params).then(
                function (data) {
                    $scope.httplist = data.res;
                    $scope.PAGE = data.PAGE; 
                    $scope.ppp = calcPage($scope.PAGE);

                    $scope.sums =  listSums($scope.httplist, $rootScope.cols);

            }, error);   
        };
        $scope.list();
        $scope.keydown = function(event){
            if (event.keyCode == 13) {
                $scope.list();
            }   
        };
        $scope.ajaxDelete = function(id){
            var params = {};
            params[$rootScope.cols[0]] = id;
            dinnerService.del(params).then(
                function (data) { 
                    info("操作数据:" + data.res + "条");
                    $scope.list(); 
            }, error);  

        };

    };
    //加载表信息
    dinnerService.cols().then(
        function (data) {
            $rootScope.cols = data.res;
            closeLoading();
            loadPage();
    }, error);


}])


