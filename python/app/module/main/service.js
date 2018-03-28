
// 自定义服务


angular.module('com.main')
.service('mainService',['baseService', function(baseService){ 
    this.name = 'this.name';  
    this.list = function(params){ 
        debugger;
        return baseService.post("/BaseSSM/angular/list.do", params);
    };   
    
}]);

