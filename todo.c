
##########################################################################
综合企业级项目架构实施！！！
功能 
主页展示 介绍
数据库数据通用展示 管理 接口
服务器 监 控
权限管理模块

webservice 封装 

路由层
1.  基于 spirng 路由功能
2.  支持 http协议中 GET/POST/DELTE/PUT等方法
3.  支持REST风格请求及普通http请求
控制器层
1.  支持Controller及RestController
2.  请求参数形式多样化
3.  参数格式统一转换为json
业务逻辑层
1.  接收json格式数据，处理业务逻辑，调用数据访问层。
数据访问层
2.  业务逻辑持久化数据的中间层。调用数据库或文件系统
持久化层
1.基于MyBatis持久化框架
2.结合sharding-jdbc分表分库
3.支持多数据库



前后端完全分离 ajax 和 socket
//前端架构 angular
//数据库集成 连接池 Redis 缓存 可配置
//MVC 抽离controller 通用 spring mvc restful

socket 通信 http 临界资源 进程通信

socket 模块 
实现 中转站 多队列 任务线程数量限制

数据库 及缓存模块

文件模块
通用 浏览器http 移动端http 文件上传工具
swfupload

权限模块

监控模块

性能测试



SOA服务框架：Dubbo、zookeeper、Proxy、RestFul
缓存：Redis、ehcache
分布式消息中间件：KafKa+Flume+ZookeeperKeepalived+Nginx+Proxy
负载分布式文件：FastDFS
SSO框架：CAS单点登录
模块化管理：Maven
数据库连接池：Alibaba Druid
核心框架：Spring framework
安全框架：Apache Shiro
视图框架：Spring MVC
富文本：CKEcitor
动态页签：Jerichotab、对话框：jQuery jBox
树结构控件：jQuery zTree报表：Echarts、JasperReports
服务端验证：Hibernate Validator
布局框架：SiteMesh
工作流引擎：Activiti 5.15
任务调度：quartz 1.8.5
持久层框架：MyBatis
日志管理：SLF4J 1.7、Log4j
前端框架：Bootstrap 4 metronic
客户端验证：JQuery Validation



//后台开发学习//////////////////////////////////////////////////////////////////////////////////
《深入理解计算机系统》，《tcp/ip详解 卷一、二、三》，《数据结构与算法》

Java IO nio 多线程
Spring、SpringMVC、iBatis/MyBatis 应用经验 了解到它的原理和机制
分布式SOA服务框架：Dubbo、zookeeper、Proxy、RestFul
rpc rmi
Redis、ehcache


Sql优化理论

JVM 原理  
分布式 多线程 高性能 大数据-高并发经验

//Linux vi 搜索 行号 awk文本格式化 


1、Java基础，熟悉io、多线程、集合等基础框架，了解分布式、缓存、消息、搜索等机制；  
2、具备系统调优、性能调优等技能， jvm
3、对设计模式非常熟悉，有一定的实战经验，需要具备良好的建模能力，对领域模型设计了解甚佳；  
4、Spring、SpringMVC、iBatis等开源框架有应用经验者优先， 了解到它的原理和机制

多线程及高性能的设计与编码及性能调优；有高并发应用开发经验
//部分源码解析博客 netty sort springMVC 注解
//数据库MongloDB

//接口----------------

百度文本语音转换
京东Alpha人工智能接口

//项目开发-----------------
nginx文件服务器

多服务器 启动-关闭-日志-监控 批量统一配置管理系统
AServer:
    ssh登录
    start shell http start 
    stop shell  kill pid
    log         cat log.file


#第三方推送平台服务器
#设计跳板机 socket 路由表 路由器


#TCP/IP socket/应用层协议/mqtt/http/自己的协议@
Android 进程 jni 从底层向上 模拟系统信息 工具连点器
Android 设备控制器 - 设备socket - socketServer<net> - 终端socket
设备端 socket适配管理



//Linux-------------------------------------
Shell多进程 管道 同步 队列 生产者 消费者 进程通信
内核驱动编写test


//Java学习----------------------------------看书 Thinking in Java---------------------
#thread 并发 同步锁 几种方式
看书 通读 详细  
#ThreadLocal Context上下文 全局变量 
#线程池 - 单/多线程池队列 -> 高并发 - 定时任务调度《队列 生产者 消费者模型》
#进程通信 远程调用RPC 共享内存IPC
#classloader 注入原理 工具



//设备-------------------------------------------------------------------------------------------------
$外形造型设计
$图像流处理 传输
3d打印机
外观 组件 设计 结合传感器 和 输出 设备 ############# 


    pi端
    
结合python opencv rtmp模块 树莓派摄像头 推送直播 监控系统
           简易识别物体 保存照片 并 推送消息

//实时监控视频有困难 延时 帧率 图像处理cpu压力  传输带宽 速度 
解决方案：
    自定义压缩 灰度图 缩小 压缩字节 socket传输 自定义解码显示层    

    
    手机端
        http访问静态 图片资源
        socket交互控制系统 并 获取推送 并 去主动获取高质量关键图片 获取系统环境监控信息并展示
        rtmp直播地址监控
        
红外 避障 测距 模块实现
自移动 地图探测 推送远程地图识别

//输入
--监控 输入
指令 控制 端口 
指令 控制 行为 <移动 组合开关>

--自发输入 传感器检测 状态 监控 
自学习地图探测生成

录像 ##
录音 ##

光
声音
湿度
烟雾
红外


//分析 加工
--图像处理 opencv
图像视频流合成 加工 分析结果 反馈监控

--机器学习

//输出
动力
终端监控传输 图像 声音 文本

额外反馈 警报 终端 
避障碍
开关状态 传感器

 