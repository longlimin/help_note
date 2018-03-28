 
angular.module('com.table')

.controller('com.table.pageCtrl', ['$scope', '$rootScope', '$state', '$stateParams', 'tableService', function ($scope, $rootScope, $state, $stateParams, tableService) {
    //嵌套路由 scope可访问 <任意module> 的上层html的 ctrl/scope
    var mName = 'table';
    $scope.mName = mName;

    $scope.table = $stateParams.id;
    tableService.setTable($scope.table);

  
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
    $scope.show = function(){
        tableService.setTable($scope.table);
        var params = {"id" : $scope.table};
        $state.go('main.' + mName + '.list', params);  
        //跳转某子级 却传递父级的参数 如下 有用url: /#/main/tablelunch/list  会执行 父级和子级ctrl 且父级能收到参数 
    };

    $('#charttimefrom').datetimepicker();
    $('#charttimeto').datetimepicker();
    var yyyymm = getDate('yyyy-MM-dd');
    $scope.chart = {}; //查询
    $scope.chart.TIMEFROM = yyyymm;
    $scope.chart.TIMETO = yyyymm;
    $scope.statis = function(){ 
        var params = $scope.chart;
        tableService.statis(params).then(
        function (data) { 
            info(data);
            //data.option = $.extend({"yAxis":{}}, data.option )
            toolSetChart("echarts", data.option);
        },error);  
    };
    //$scope.statis();

}])
.controller('com.table.addCtrl', ['$scope', '$rootScope', 'tableService', function ($scope, $rootScope, tableService) {
    $scope.httpget = {};

    $scope.httpget[$rootScope.cols[0]] = getDate('yyyy-MM-dd');

    var params = {};
    params[$rootScope.cols[0]] = getTheDay('yyyy-MM-dd', -1);
    tableService.get(params).then(
        function (data) {
            $scope.httpget = data;
            $scope.httpget[$rootScope.cols[0]] = getDate('yyyy-MM-dd');
    }, error);

    $scope.ajaxSubmit = function(){
        var params =  $scope.httpget;
        tableService.add(params).then(
            function (data) {
                info("操作数据:" + data.res + "条");
                $scope.goHome();
        }, error); 
    };
}])
.controller('com.table.updateCtrl', ['$scope', '$rootScope', '$stateParams', 'tableService', function ($scope, $rootScope, $stateParams, tableService) {

    $scope.httpget = {};

    $scope.params= $stateParams;
    info("stateParams:" + JSON.stringify($scope.params));

    var params = {};
    params[$rootScope.cols[0]] = $scope.params.id;
    tableService.get(params).then(
        function (data) {
            $scope.httpget = data; 
    }, error);
 

    $scope.ajaxSubmit = function(){
        var params = $scope.httpget;
        tableService.update(params).then(
            function (data) {
                info("操作数据:" + data.res + "条");
                $scope.goHome(); 
            }, error);  

    };
}])
.controller('com.table.listCtrl', ['$scope', '$rootScope', '$state', 'tableService', function ($scope, $rootScope, $state, tableService) { 
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
            tableService.list(params).then(
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
            tableService.del(params).then(
                function (data) { 
                    info("操作数据:" + data.res + "条");
                    $scope.list(); 
            }, error);  

        };

    };
    //加载表信息
    tableService.cols().then(
        function (data) {
            $rootScope.cols = data.res;
            closeLoading();
            loadPage();
    }, error);


}])


