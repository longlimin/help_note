
#项目组件架构   Tomcat    python-web<GPIO>   python-socket  
#nginx          链接代理转发请求  并提供 图片/视频流推送-服务
#运行环境       PC  Raspberry sqlite数据库

# socket-python ----  socket-java ---- socket-android1
                                  ---- socket-android2
                                  ---- socket-android3
24:0A:64:14:55:0D

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




推送流工具
采集流 - cv处理 - 输出流 - 推送工具/部署站点 《 《 《 访问地址获取流
              文件读取流 - 推送工具/部署站点 《 《 《 访问地址获取流







自定义实现？： 
    图片采集 加工 定时覆盖 前端轮循短连接 介于浏览器同url不重新加载问题 规定时间轴取整 命名 定时更新前后端同步
                  定时推送 socket长连接

                  写入         流         前端video流加载
                            管道/文件                  

//nginx-rtmp直播点播系统

rtmp { # 配置RTMP模块
    server { # 服务器
        listen 1935; # 监听端口, 默认为1935
        chunk_size 4000; # 数据块大小 4000
        
        application hls {     
            live on;    
            hls on;    
            hls_path E:/nginx-rtmp/hls;    #文件存放地址,/tmp/hls
        }
        
        application myapp { # 应用名称, 可理解为直播房间的名称
            live on; # 直播 [on]开启
        }

    }
} 
http配置地址跳转 直播
location /hls {    
    types {    
        application/vnd.apple.mpegurl m3u8;    
        video/mp2t ts;    
    }    
    root E:/nginx-rtmp;    
    add_header Cache-Control no-cache;    
} 

//vlc播放地址
rtmp://127.0.0.1:1935/myapp/test1
//可用推送地址
ffmpeg -re -i test.mp4 -c copy -f flv rtmp://127.0.0.1:1935/myapp/test1

//hls模式
相对于常见的流媒体直播协议，例如RTMP协议、RTSP协议、MMS协议等，HLS直播最大的不同在于，直播客户端获取到的，并不是一个完整的数据流。HLS协议在服务器端将直播数据流存储为连续的、很短时长的媒体文件（MPEG-TS格式），而客户端则不断的下载并播放这些小文件，因为服务器端总是会将最新的直播数据生成新的小文件，这样客户端只要不停的按顺序播放从服务器获取到的文件，就实现了直播。由此可见，基本上可以认为，HLS是以点播的技术方式来实现直播。由于数据通过HTTP协议传输，所以完全不用考虑防火墙或者代理的问题，而且分段文件的时长很短，客户端可以很快的选择和切换码率，以适应不同带宽条件下的播放。不过HLS的这种技术特点，决定了它的延迟一般总是会高于普通的流媒体直播协议。
rtmp://127.0.0.1:1935/hls/test2
ffmpeg -re -i test.mp4 -c copy -f flv rtmp://127.0.0.1:1935/hls/test2

//采集视频
1、列表本机的视音频设备 
ffplay -list_devices true -f dshow video=0
"Integrated Camera"
"Internal Microphone (Conexant SmartAudio HD)"
这句话列出了我电脑上的摄像头和音频设备
2、窗口播放  不配置-i则窗口播放
ffplay -f dshow video="Integrated Camera"
这句话打开了我的摄像头 -i 输出文件流
3、捕获  
ffmpeg -f dshow -i video="Integrated Camera" e:/nginx-rtmp/get.mp4 
这句话开始采集视频。音频部分未加上。

ffmpeg -f dshow -i video="Integrated Camera" flv rtmp://127.0.0.1:1935/myapp/test1


ffmpeg -f dshow -i video="Integrated Camera" -s 640x360 -vcodec libx264 -b:v 1000k   -ab 128k -f flv rtmp://127.0.0.1:1935/myapp/test1
//10s延时 无配置采集推送rtmp
ffmpeg -f dshow -i video="Integrated Camera" -s 320x240 -f flv rtmp://127.0.0.1:1935/myapp/test1 
ffmpeg -f dshow -i video="Integrated Camera" -f flv rtmp://127.0.0.1:1935/myapp/test1 
ffplay -f dshow video="Integrated Camera"  


1、将文件当做直播送至live
ffmpeg -re -i localFile.mp4 -c copy -f flv rtmp://server/live/streamName
2、将直播媒体保存至本地文件
ffmpeg -i rtmp://server/live/streamName -c copy dump.flv
3、将其中一个直播流，视频改用h264压缩，音频不变，送至另外一个直播服务流
ffmpeg -i rtmp://server/live/originalStream -c:a copy -c:v libx264 -vpre slow -f flv rtmp://server/live/h264Stream
4、将其中一个直播流，视频改用h264压缩，音频改用faac压缩，送至另外一个直播服务流
ffmpeg -i rtmp://server/live/originalStream -c:a libfaac -ar 44100 -ab 48k -c:v libx264 -vpre slow -vpre baseline -f flv rtmp://server/live/h264Stream
5、将其中一个直播流，视频不变，音频改用faac压缩，送至另外一个直播服务流
ffmpeg -i rtmp://server/live/originalStream -acodec libfaac -ar 44100 -ab 48k -vcodec copy -f flv rtmp://server/live/h264_AAC_Stream
6、将一个高清流，复制为几个不同视频清晰度的流重新发布，其中音频不变
ffmpeg -re -i rtmp://server/live/high_FMLE_stream -acodec copy -vcodec x264lib -s 640×360 -b 500k -vpre medium -vpre baseline rtmp://server/live/baseline_500k -acodec copy -vcodec x264lib -s 480×272 -b 300k -vpre medium -vpre baseline rtmp://server/live/baseline_300k -acodec copy -vcodec x264lib -s 320×200 -b 150k -vpre medium -vpre baseline rtmp://server/live/baseline_150k -acodec libfaac -vn -ab 48k rtmp://server/live/audio_only_AAC_48k
7、功能一样，只是采用-x264opts选项
ffmpeg -re -i rtmp://server/live/high_FMLE_stream -c:a copy -c:v x264lib -s 640×360 -x264opts bitrate=500:profile=baseline:preset=slow rtmp://server/live/baseline_500k -c:a copy -c:v x264lib -s 480×272 -x264opts bitrate=300:profile=baseline:preset=slow rtmp://server/live/baseline_300k -c:a copy -c:v x264lib -s 320×200 -x264opts bitrate=150:profile=baseline:preset=slow rtmp://server/live/baseline_150k -c:a libfaac -vn -b:a 48k rtmp://server/live/audio_only_AAC_48k
8、将当前摄像头及音频通过DSSHOW采集，视频h264、音频faac压缩后发布
ffmpeg -r 25 -f dshow -s 640×480 -i video=”video source name”:audio=”audio source name” -vcodec libx264 -b 600k -vpre slow -acodec libfaac -ab 128k -f flv rtmp://server/application/stream_name
9、将一个JPG图片经过h264压缩循环输出为mp4视频
ffmpeg.exe -i INPUT.jpg -an -vcodec libx264 -coder 1 -flags +loop -cmp +chroma -subq 10 -qcomp 0.6 -qmin 10 -qmax 51 -qdiff 4 -flags2 +dct8x8 -trellis 2 -partitions +parti8x8+parti4x4 -crf 24 -threads 0 -r 25 -g 25 -y OUTPUT.mp4
10、将普通流视频改用h264压缩，音频不变，送至高清流服务(新版本FMS live=1)
ffmpeg -i rtmp://server/live/originalStream -c:a copy -c:v libx264 -vpre slow -f flv “rtmp://server/live/h264Stream live=1〃







##################################################################################

#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}

rtmp { # 配置RTMP模块
    server { # 服务器
        listen 1935; # 监听端口, 默认为1935
        chunk_size 4000; # 数据块大小 4000
        

        application hls {     
            live on;    
            hls on;    
            hls_path E:/nginx-rtmp/hls;    #文件存放地址,/tmp/hls
        }
        
        application myapp { # 应用名称, 可理解为直播房间的名称
            live on; # 直播 [on]开启
        }

    }
}   



http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    #Tomcat 
    upstream base {
        server 127.0.0.1:8085 weight=1;    
    }  
    #RaspBerry python tornado
    upstream python {
        server 127.0.0.1:8086 weight=1;    
    }  
    #RaspBerry python socket
    upstream socket {
        server 127.0.0.1:8087 weight=1;    
    }  
    
     
    server {
        listen 8088;
        server_name localhost;
        
        # rtmp hls http直播
        location /hls {    
            types {    
                application/vnd.apple.mpegurl m3u8;    
                video/mp2t ts;    
            }    
            root E:/nginx-rtmp;    
            add_header Cache-Control no-cache;    
        } 
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































