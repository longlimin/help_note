
// 自定义服务


angular.module('com.login')
.service('loginService',['baseService', function(baseService){ 
    this.name = 'this.name';   
 
    this.login = function(params){ 
        return baseService.test("/BaseSSM/angular/login.do", params, {"res":"ok"});
    }; 
    this.registe = function(params){ 
        return baseService.test("/BaseSSM/angular/login.do", params, {"res":"ok"});
    }; 
    
}]);

