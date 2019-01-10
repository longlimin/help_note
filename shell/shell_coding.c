//shell 编程

echo 
printf "% 3d"$res''$obj"\n" "$i"

//赋值
var=$(命令) 
var=`命令` # 注意此处不是普通的单引号
//变量
    函数变量 和 全局变量 冲突域 公用？ 递归注意？
    a=1     =不要空格
    str="abc" / '123' / `cat text.txt`      绝对字符串'' 可编译嵌入变量"" 命令返回结果``
    #shell中对变量的值添加单引号，双引号和不添加的区别：对类型来说是无关的，即不是添加了引号就变成了字符串类型，
    #单引号不对相关量进行替换，如不对$符号解释成变量引用，从而用对应变量的值替代，双引号则会进行替代
    echo $a"abc"'123'
    echo $[1+2]
    echo $[a+1]
    c=let $a+1 
    val=`expr 2 + 2`
    val=$((2 + 2))
    
//数组
    arr=(1 2 3)     一对括号表示是数组，数组元素用“空格”符号分割开
    echo $arr   /   ${a[*]}      *或者@ 得到整个数组内容
    len=${#arr[@]}  长度
    arr2=${arr[2]}  取值
    arr[2]=200      赋值
    unset arr[2]    删除某个元素    unset数组[下标] 可以清除相应的元素，不带下标，清除整个数据。
    echo ${a[@]:1:4}    截取数组输出
    arrChild=(${a[@]:1:4})  切片数组   
//字符串 
    len=${#str}     长度
    $value1=home
    $value2=${value1}"="
    echo $value2 

//字符串包含
    result=$(echo $strA | grep "${strB}")
    if [[ "$result" != "" ]] 包含
    if [[ $strA =~ $strB ]]
    if [[ $A == *$B* ]]

//字符串截取      # % 保留左右
    var=http://www.aaa.com/123.htm.  
    echo ${var#*//} # *// 删除匹配到的 *//之前
    即删除 http://
    结果是 ：www.aaa.com/123.htm
    echo ${var##*/} ## */删除 最后面 */ 之前 
    结果是 123.htm 
    echo ${var#*//} 用法
    #*/     删除最少匹配的*/
    ##*/    删除最多匹配*/
    %/*    倒数 删除最少的/*               */
    %%/*   倒数 删除最多的/*    */
        1、提取文件名
        [root@localhost log]# var=/dir1/dir2/file.txt
        [root@localhost log]# echo ${var##*/}
        file.txt
        2、提取后缀
        [root@localhost log]# echo ${var##*.}
        txt
        3、提取不带后缀的文件名，分两步
        [root@localhost log]# tmp=${var##*/}
        [root@localhost log]# echo $tmp
        file.txt
        [root@localhost log]# echo ${tmp%.*}
        file
        4、提取目录
        ;//[root@localhost log]# echo ${var%/*}
        /dir1/dir2
    echo ${var:0:5}
    其中的 0 表示左边第一个字符开始，5 表示字符的总个数。
    结果是：http:
    echo ${var:7}
    其中的 7 表示左边第8个字符开始，一直到结束。
    echo ${var:0-7:3}
    其中的 0-7 表示右边算起第七个字符开始，3 表示字符的个数。
     结果是：123
    echo ${var:0-7}
    表示从右边第七个字符开始，一直到结束。
    结果是：123.htm 
    

//字符串分割
    info='abcd;efgh'
    arr=(`echo $info|tr ";" "\n"`)

//字符串 命令 解释器
st="ls | more"
`$st`   //将 | 和 more 看成了参数，而不是将文件按页显示
eval $st      //双次解析 一次解析变量 二次 放置执行？ 同js php shell


//ll找不到 ll = ls -alF 
//if else  test  判断  
//[ ] 实际上是bash 中 test 命令 ，用于判断类型 -z -f -d -n
// [[ expr ]] 是bash中真正的条件判断语句 < > == != 
{
    #!/bin/sh 
    #测试各种字符串比较操作。 
    A="$1"
    B="$2"
    if (( $i < 5 )) 增强括号的用法, 常用于算术运算比较.
    #如果$a等于a*(字符匹配 全值),那么结果为true
    if [[ "$obj" =~ .*Test.*  $regular<'.*Test.*'> ]]     //正则匹配  .*a.*
    if [[ "$A" == a* ]];then                              //模式匹配  *a*
    if [[ "$A" == "a*" ]];then                            //字符串全值匹配  
    if [[ "$A" != "$B" ]];then 
    if [[ $A < $B ]];then  
    if [ -n "$A" ];then  #字符串不为空，长度不为0
    
    if [ -z "$A" ];then   #字符串为空.就是长度为0.
    # 这里的-d 参数判断$myPath是否存在 是否为目录
    if [ ! -d "$myPath"]; then
     mkdir "$myPath"
    fi 
    # 这里的-f参数判断$myFile是否存在 是否为文件
    if [ ! -f "$myFile" ]; then
     touch "$myFile"
    fi
}

//循环
{ 

    local i #局部变量
    //for循环的i除外是局部的 否则默认全局的
    for ((i=1; i<=8; i++))
    for i in {0..5}
    for i in ${arr[@]}  //*

    for i in a b c
    for i in `seq 1 10`
    do
        echo ''
    done
    while [[ "1" == "1" ]]
    do

    done
}
//文件读取 while read line

while read line
do
       …
done < file
read通过输入重定向，把file的第一行所有的内容赋值给变量line，循环体内的命令一般包含对变量line的处理；
然后循环处理file的第二行、第三行。。。一直到file的最后一行。还记得while根据其后的命令退出状态来判断是否执行循环体吗？
是的，read命令也有退出状态，当它从文件file中读到内容时，退出状态为0，循环继续惊醒；当read从文件中读完最后一行后，
下次便没有内容可读了，此时read的退出状态为非0，所以循环才会退出。
另一种也很常见的用法：
command | while read line
do
    …
done
如果你还记得管道的用法，这个结构应该不难理解吧。command命令的输出作为read循环的输入，
这种结构长用于处理超过一行的输出，当然awk也很擅长做这种事。
//函数
{

./do show pp
#$0<./do>-n取参数,$#<2>参数个数,$@<数组".do" "show" "pp">,$*<串"./do show pp">,$?<int0/1>函数返回值 
$$PID<59>

#不能为空函数!!!!!!!!!!!!!!!!!!!!!!!    
root=`cat toolsTemp.txt` 变量可以接受输出echo cat返回值 

    
}

#批量创建文件
{ 
[root@linuxidc net]# for i in `seq -w 10`
> do touch stu\_$i\_linux.jpg
> done 
-rw-r--r-- 1 root root 0 Oct 9 21:22 stu_01_linux.jpg
-rw-r--r-- 1 root root 0 Oct 9 21:22 stu_02_linux.jpg 
使用rename进行修改
[root@linuxidc net]# rename \_linux '' *.jpg
[root@linuxidc net]# sl
total 0
-rw-r--r-- 1 root root 0 Oct 9 21:22 stu_01.jpg
-rw-r--r-- 1 root root 0 Oct 9 21:22 stu_02.jpg 
注意，如果想要替换掉下划线，那么你不能加任何引号。
[root@linuxidc net]# for i in `seq -w 10`; do touch stu\_$i\_linux.jpg; done
[root@linuxidc net]# sl
total 0
-rw-r--r-- 1 root root 0 Oct 9 21:58 stu_01_linux.jpg
-rw-r--r-- 1 root root 0 Oct 9 21:58 stu_02_linux.jpg 
[root@linuxidc net]# rename '\_linux' '' *.jpg
[root@linuxidc net]# sl
total 0
-rw-r--r-- 1 root root 0 Oct 9 21:27 stu_01_linux.jpg
-rw-r--r-- 1 root root 0 Oct 9 21:27 stu_02_linux.jpg 
-rw-r--r--
}

//日期格式化
[root@root ~]# date "+%Y-%m-%d"  
2013-02-19  
[root@root ~]# date "+%H:%M:%S"  
13:13:59  
[root@root ~]# date "+%Y-%m-%d %H:%M:%S"  
2013-02-19 13:14:19  
[root@root ~]# date "+%Y_%m_%d %H:%M:%S"    
2013_02_19 13:14:58  
[root@root ~]# date -d today   
Tue Feb 19 13:10:38 CST 2013  
[root@root ~]# date -d now  
Tue Feb 19 13:10:43 CST 2013  
[root@root ~]# date -d tomorrow  
Wed Feb 20 13:11:06 CST 2013  
[root@root ~]# date -d yesterday  
Mon Feb 18 13:11:58 CST 2013  


//进程并发数控制 管道 同步
见pipe_maker.sh 案例

////////////////////////////自动化输入 expect
spawn ./update.sh
expect "Username for 'https://gitee.com'"
send -- "617772977@qq.com\n"
expect "Password for 'https://617772977@qq.com@gitee.com'"
send -- "这里替换成你自己的密码就好了\n"
interact
////////////////////////////自动化输入 管道
#! /bin/bash
read -p "enter number:" no
read -p "enter name:" name
echo you have entered $no, $name

// 管道输入
echo -e '222\nbbb' | ./exe_reader.sh

//文件管道输入
./exe_reader.sh < filename.txt







