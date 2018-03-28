
// 自定义服务


angular.module('com.dinner')
.service('dinnerService',['$PROJECT','baseService','cacheService', function($PROJECT,baseService,cacheService){

    //表名
    var mName = 'dinner';

     var service = {};
    //操作表名
    service.table = mName;

    service.setTable = function(tableName){
        service.table = tableName;
    };
    service.getTable = function(){
        return service.table;
    };

    service.make = function(params){
        if( ! params){ 
            params = {};
        }
        //params['TABLE_NAME'] = service.table;
        return params;
    }

    //获取表字段列表
    service.cols = function(params){ 
        params = service.make(params);
        return cacheService.post('/' + $PROJECT + '/' + mName + '/cols.do', params);
    };   

    service.list = function(params){ 
        params = service.make(params);
        return baseService.post('/' + $PROJECT + '/' + mName + '/list.do', params);
    };   
    service.listRecent = function(params){ 
        params = service.make(params);
        return baseService.post('/' + $PROJECT + '/' + mName + '/listrecent.do', params);
    }; 
    service.get = function(params){ 
        params = service.make(params);
        return baseService.post('/' + $PROJECT + '/' + mName + '/get.do', params);
    }; 
    service.del = function(params){ 
        params = service.make(params);
        return baseService.post('/' + $PROJECT + '/' + mName + '/delete.do', params);
    };
    service.update = function(params){ 
        params = service.make(params);
        return baseService.post('/' + $PROJECT + '/' + mName + '/update.do', params);
    };
    service.add = function(params){
        params = service.make(params);
        return baseService.post('/' + $PROJECT + '/' + mName + '/add.do', params);
    };
    service.statis  = function(params){
        params = service.make(params);
        return baseService.post('/' + $PROJECT + '/' + mName + '/statis.do', params);
    }; 

    
    service.do = function(url, params){ 
        return baseService.post(url, params);
    }; 

    return service;
    
}]);

