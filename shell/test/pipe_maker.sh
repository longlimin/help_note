#!/bin/bash  
###########################################
#do
#管道 生产者 写入管道
########################################### 

echo 'pipe maker start'
echo $$

tempfifo=$$'.fifo'


# exec 1000>&-;表示关闭文件描述符1000的写
# exec 1000<&-;表示关闭文件描述符1000的读
trap "exec 1000>&-;exec 1000<&-;exit 0" 2 #捕获中断命令 

mkfifo  $tempfifo # 创建一个管道文件
# 将文件描述符1000与FIFO进行绑定，<读的绑定，>写的绑定，<>则标识对文件描述符1000的所有操作等同于对管道文件$tempfifo的操作
exec 1000<>$tempfifo #创建文件标示符“5”，这个数字可以为除“0”、“1”、“2”之外的所有未声明过的字符，以读写模式操作管道文件；系统调用exec是以新的进程去代替原来的进程，但进程的PID保持不变，换句话说就是在调用进程内部执行一个可执行文件
rm -rf $tempfifo #清除创建的管道文件
for ((i=1; i<=8; i++))
do
    echo "count="$i >&1000

done



# read -u1000 读取行 阻塞
for ((i=1; i<=18; i++))
    readStr=`read -u1000`
    {
        echo "read: "$readStr
    } &
done


wait
echo 'pipe maker stop'

