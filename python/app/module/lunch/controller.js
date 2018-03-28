 
angular.module('com.lunch')

.controller('com.lunch.pageCtrl', ['$scope', '$rootScope', '$state', 'lunchService', function ($scope, $rootScope, $state, lunchService) {
    //嵌套路由 scope可访问 <任意module> 的上层html的 ctrl/scope
    var mName = 'lunch';
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
        lunchService.statis(params).then(
        function (data) { 
            info(data);
            //data.option = $.extend({"yAxis":{}}, data.option )
            toolSetChart("echarts", data.option);
        },error);  
    };
    $scope.statis();

}])
.controller('com.lunch.addCtrl', ['$scope', '$rootScope', 'lunchService', function ($scope, $rootScope, lunchService) {
    $scope.httpget = {};

    $scope.httpget[$rootScope.cols[0]] = getDate('yyyy-MM-dd');

    var params = {};
    params[$rootScope.cols[0]] = getTheDay('yyyy-MM-dd', -1);
    lunchService.get(params).then(
        function (data) {
            $scope.httpget = data;
            $scope.httpget[$rootScope.cols[0]] = getDate('yyyy-MM-dd');
    }, error);

    $scope.ajaxSubmit = function(){
        var params =  $scope.httpget;
        lunchService.add(params).then(
            function (data) {
                info("操作数据:" + data.res + "条");
                $scope.goHome();
        }, error); 
    };
}])
.controller('com.lunch.updateCtrl', ['$scope', '$rootScope', '$stateParams', 'lunchService', function ($scope, $rootScope, $stateParams, lunchService) {

    $scope.httpget = {};

    $scope.params= $stateParams;
    info("stateParams:" + JSON.stringify($scope.params));

    var params = {};
    params[$rootScope.cols[0]] = $scope.params.id;
    lunchService.get(params).then(
        function (data) {
            $scope.httpget = data; 
    }, error);
 

    $scope.ajaxSubmit = function(){
        var params = $scope.httpget;
        lunchService.update(params).then(
            function (data) {
                info("操作数据:" + data.res + "条");
                $scope.goHome(); 
            }, error);  

    };
}])
.controller('com.lunch.listCtrl', ['$scope', '$rootScope', '$state', 'lunchService', function ($scope, $rootScope, $state, lunchService) { 
    $scope.refresh = true;
    var openLoading = function(){
        $scope.refresh = true;
    };
    var closeLoading = function(){
        $scope.refresh = false;
    };

    //加载页面
    var loadPage = function(){
        $scope.PAGE = {};
        $scope.PAGE.SHOWNUM = 31;
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
            lunchService.list(params).then(
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
            lunchService.del(params).then(
                function (data) { 
                    info("操作数据:" + data.res + "条");
                    $scope.list(); 
            }, error);  

        };

    };
    //加载表信息
    lunchService.cols().then(
        function (data) {
            $rootScope.cols = data.res;
            closeLoading();
            loadPage();
    }, error);


}])


