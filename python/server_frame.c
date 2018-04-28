
#项目组件架构   Tomcat    python-web<GPIO>   python-socket  
#nginx          链接代理转发请求  并提供 图片/视频流推送-服务
#运行环境       PC  Raspberry sqlite数据库

# socket-python ----  socket-java ---- socket-android1
                                  ---- socket-android2
                                  ---- socket-android3


#项目部署流程
//启动脚本 cd shell ./do start

<PC>

    tomcat 8080    
        tomcat/bin/start.sh
        #http://127.0.0.1:8088/BaseSSM/lunch/list.do
    socket-server 8086
    socket-web  app    
    http-web    app
    
<Raspberry>

//  web tornado         短连接     图片/视频流生成-加工
    python /help_note/python/server/server_web.py
    #http://127.0.0.1:8088/do/student/mm/a

//  socket-io           长连接-web
    python /help_note/python/server/server_socket.py
    #127.0.0.1:8087 emit onMsg

//  socket              长连接-socket
    python /help_note/python/server/server_socket.py
    #127.0.0.1:8086 emit onMsg

    python GPIO opencv  工具控制类  供python通信服务器调用 控制设备行为

//  Nginx  8088     <Raspberry>
    静态路由    前端页面    静态资源
    app/html-angular
    app/resource
    http://127.0.0.1:8088/app/#

    后台路由
    ->Tomcat
    ->Python
        -web
        -socketIo server 
        -socket client
 




监控设计

自定义实现： 
    图片采集 加工 定时覆盖 前端轮循短连接 介于浏览器同url不重新加载问题 规定时间轴取整 命名 定时更新前后端同步
                  定时推送 socket长连接

                  写入         流         前端video流加载
                            管道/文件                  

rtmp直播点播系统？














##################################################################################

#user  nobody;
worker_processes  1;

error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;


    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #Tomcat 
    upstream base {
        server 127.0.0.1:8080 weight=1;    
    }  
    #RaspBerry python tornado
    upstream python {
        server 127.0.0.1:8086 weight=1;    
    }  
    #python socket
    upstream socket {
        server 127.0.0.1:8087 weight=1;    
    }  
     
    server {
        listen 8088;
        server_name localhost;
        
        
        location /app {
            root E:/help_note/python;
            autoindex on;
        }
        location /do { 
            proxy_pass http://python;
        }
        location /BaseSSM { 
            proxy_pass http://base;
        }
        location / {
            root E:/help_note;
        }
    }

    
    

}

































