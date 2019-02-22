
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
      
      
      
