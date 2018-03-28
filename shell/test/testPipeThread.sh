#! /bin/bash
  #  source /etc/profile;

    # -----------------------------

    tempfifo=$$.fifo        # $$表示当前执行文件的PID
    begin_date=0           # 开始时间
    end_date=100             # 结束时间
 
    # -----------------------------
    
#如果接收到Ctrl+C中断命令，则关闭文件描述符1000的读写，并正常退出 
#exec 1000>&-;表示关闭文件描述符1000的写
#exec 1000<&-;表示关闭文件描述符1000的读
#trap是捕获中断命令 
     trap "exec 1000>&-;exec 1000<&-;exit 0" 2
     mkfifo $tempfifo #创建一个管道文件
#将文件描述符1000与FIFO进行绑定，文件操作符只能使用 0-1023，系统运行起始，就相应设备自动绑定到了 三个文件操作符   分别为 0 1 2 对应 stdin ，stdout， stderr 。可自行定义的 就只能是 3-1023 了。
#<读的绑定，>写的绑定，<>则标识对文件描述符1000的所有操作等同于对管道文件$tempfifo的操作
    exec 1000<>$tempfifo #exec 指令自行定义、绑定文件操作符
#非匿名管道必须同时写入写出阻塞
     rm -rf $tempfifo #管道文件刚创建后就删除？也没问题但一定记得删除
#对文件描述符1000进行写入操作。通过循环写入8个空行，这个8就是我们要定义的后台并发的线程数。为什么是写空行而不是写其它字符？因为管道文件的读取，是以行为单位的
    for ((i=1; i<=8; i++))
    do
        echo >&1000
    done 
    
    while [[ $begin_date != $end_date ]]
    do
#的作用就是读取管道中的一行 在这里就是读取一个空行 每次读取管道就会减少一个空行
        read -u1000
        {
            echo "do at $begin_date "
            #hive -f kpi_report.sql --hivevar date=$begin_date
          
            sleep 1
#执行完后台任务之后，往文件描述符1000中写入一个空行。关键 由于read -u1000每次操作，都会导致管道减少一个空行，当linux后台放入了8个任务之后，由于文件描述符1000没有可读取的空行，将导致read -u1000一直处于等待。
            echo >&1000
        } & #它表示进程放到linux后台中执行

        #begin_date=`date -d "+1 day $begin_date" +"%Y-%m-%d"`
        begin_date=$[begin_date+1]
    done

    wait
     
    echo "done!!!!!!!!!!"
