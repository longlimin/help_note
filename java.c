
JAVA_HOME
C:\Program Files\Java\jdk-9
PATH
%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin


//反编译
javap -v ServiceImpl.class
javap -verbose ServiceImpl.class

eclipse启动jvm内存
eclipse启动程序 jvm 内存不够oom
Jdk edit 附加参数
-Xmx1024M


J2SE 8 = 52,
J2SE 7 = 51,
J2SE 6.0 = 50,
J2SE 5.0 = 49,
JDK 1.4 = 48,
JDK 1.3 = 47,
JDK 1.2 = 46,
JDK 1.1 = 45



性能分析

重启前需要收集的信息:
      #导出操作系统cpu信息
      ps H -eo user,pid,ppid,tid,time,%cpu --sort=%cpu > cpu.log
      #导出网络连接信息
      netstat -natl > netstat.log
      #获取服务器nmon日志
      #数据库连接池 进程等情况
      #redis信息快照  
      
      #导出线程信息
      $JAVA_HOME/bin/jstack ${pid} > jstack.log
      #导出内存快照
      jmap -dump:format=b,live,file=./jmap_dump ${pid}


pid=`ps -elf | grep javaagent | grep -v grep | awk '{print $4}' `
$JAVA_HOME/bin/jstack ${pid} > ~/logs/jstack.log
jmap -dump:format=b,live,file=~/logs/jmap_dump ${pid}

可重启后收集的信息：
      #获取was相关日志: System.out 或 自动生成的其他日志
      #获取服务业务日志
      
      
1. Provider: 服务提供者在启动时，向注册中心注册自己提供的服务。 Java项目
2. Consumer: 服务消费者在启动时，向注册中心订阅自己所需的服务。 Java项目
             从提供者地址列表中，基于软负载均衡算法，选一台提供者进行调用，如果调用失败，再选另一台调用。 
3. Registry: 注册中心返回服务提供者地址列表给消费者，如果有变更，注册中心将基于长连接推送变更数据给消费者。 zookeeper redis
4. Monitor : 服务消费者和提供者，在内存中累计调用次数和调用时间，定时每分钟发送一次统计数据到监控中心。    

//注册中心
zookeeper安装启动 port:2181
wget http://mirrors.shu.edu.cn/apache/zookeeper/stable/zookeeper-3.4.12.tar.gz
tar -xvf zookeeper-3.4.12.tar.gz
cd zookeeper-3.4.12
cp conf/zoo_sample.cfg conf/zoo.cfg
vi conf/zoo.cfg     #修改 数据路径 
    dataDir=~/log/zookeeper

bin/zkServer.sh start #</stop/status>
bin/zkCli.sh -server 127.0.0.1:2181  #测试
注意防火墙

//监控中心
下载 dubbo-admin-2.5.7.war

放入 tomcat/webapps/
dubbo-admin-2.5.7/WEB-INF/dubbo.properties 修改地址 默认本机
    dubbo.registry.address=zookeeper://127.0.0.1:2181
    
tomcat/bin/startup.sh 启动tomcat
http://127.0.0.1:8080/dubbo-admin-2.5.7/
root/root


如果还是连不上 防火墙？ 
/sbin/iptables -I INPUT -p tcp --dport 8080 -j ACCEPT
service iptables save
service iptables restar


      
      
      
