
// 自定义服务


angular.module('com.tomcat')
.service('tomcatService',['baseService', function(baseService){ 
    this.name = 'this.name';   
    this.list = function(params){ 
        return baseService.post("/BaseSSM/angular/list.do", params);
    };   
    this.get = function(params){ 
        return baseService.post("/BaseSSM/angular/get.do", params);
    }; 
    this.del = function(params){ 
        return baseService.post("/BaseSSM/angular/delete.do", params);
    };
    this.update = function(params){ 
        return baseService.post("/BaseSSM/angular/update.do", params);
    }; 
    this.do = function(url, params){ 
        return baseService.post(url, params);
    }; 
    this.statis = function(params){ 
        return baseService.post("/BaseSSM/tomcat/statis.do", params);
    }; 
    this.statisCount = function(params){ 
        return baseService.post("/BaseSSM/tomcat/statiscount.do", params);
    }; 
}]);

