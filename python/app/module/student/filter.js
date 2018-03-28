
//diy过滤器  结合 ng-repeat实现本页面静态查询
angular.module('com.student')
.filter('filterQuery', function() { 
    return function (collection, params) {
        var res = [];
        // info("collection：");
        // info(collection);
        // info("params:");
        // info(params); 
        
        angular.forEach(collection, function (item) {
            //info(item);
            flag = 1;
            //debugger;
            //过滤数组中值与指定值相同的元素 
            /* if(item.TIME != null){ 
                flag = 0;
                if(params.TIMETO != null && params.TIMEFROM != null && item.TIME < parmas.TIMETO && item.TIME >= params.TIMEFROM){
                    flag = 1;
                }else if(params.TIMETO != null && params.TIMEFROM != null && item.TIME < params.TIMETO ){
                    flag = 1;
                }else if(params.TIMETO == null && params.TIMEFROM != null && item.TIME >= params.TIMEFROM ){
                    flag = 1;
                }else if(params.TIMEFROM == null && params.TIMETO == null ){
                    flag = 1;
                }
            } */
            if(flag == 1){
                res.push(item);
            }
        });
        return res;
    }
});
