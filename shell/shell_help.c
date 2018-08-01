uname -a  //查看系统信息
cat /proc/version //正在运行的内核版本。
cat /etc/issue //显示的是发行版本信息
cat /proc/cpuinfo | more
cat /proc/meminfo 
fdisk -l //查看磁盘信息
ethtool eth0 //网卡信息
//查看文件大小 占用
du -sh *
touch test.txt //创建文件

//基本命令
{

    find / -name librtmp.so.1
    whereis 
    which
    ls -d /imgs/        只显示目录
    ls -F | grep '/$'
    ls -I | grep '^d'
    type ls 查看命令位置
    $uname -m -r
    $uname -mr
    date --version / -v   --引领一整个英文单词
    date --set="1999-01-01 08:00:00"
    whatis ls   简述
    man ls 帮助文档
    info ls 更详细的文档
    $history    历史 
    (1)CTRL+Z挂起进程并放入后台
　　(2) jobs 显示当前暂停的进程 ###########################################
　　(3) bg %N 使第N个任务在后台运行(%前有空格)
　　(4) fg %N 使第N个任务在前台运行
　　  默认bg,fg不带%N时表示对最后一个进程操作!
    vim :set number 设置行号 
    :set nu
    id  查看当前用户组及其他状态
	apt-cache madison python-rpi.gpio	查看安装 的软件版本
	sudo killall -9 nginx
    tar -xvf 解压
    tar -zvf 
    unzip opencv-2.4.13.zip
    cd opencv-2.4.13/
    cmake -D WITH_GTK_2_X=ON -D CMAKE_INSTALL_PREFIX=/usr/local .
    make    # make -j4表示开4个线程来进行编译
    make install
    通配符 星号”*”
    命令行历史 history
    目录~,.& ..
    ./startup.sh & 后台运行命令 & 终端相关/注销则终止
    wait 等待所有&执行完毕
    nohup ./startup.sh & 守护进程？无关终端 忽略所有挂断（SIGHUP）信号 无视注销/关闭终端
    ldconfig 通常在系统启动时运行，加载新的动态链接库时，就需要手工运行这个命令。 
    ln -s source     dist     #建立软连接 快捷方式
    ln     source     dist     #建立硬连接 硬链接不能连接两个不同文件系统上的文件 类似拷贝副本
    
    chown -R wasup:wasgrp com 修改用户及组权限

    #去掉控制台颜色代码##########
    top | sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g"

    设置时间
    sudo ntpd -s -d  //自动同步 
    sudo date --s="2014-08-21 12:33:22" //手动设置
    配置服务
    sudo vim /etc/ntpconf
    # You do need to talk to an NTP server or two (or three).
    # server ntp.your-provider.example
    在下面添加以下内容，是一些亲测可用的ntp服务器。第一行最后的perfer表示优先使用此服务器，也就是复旦大学的ntp服务器。添加之后按Ctrl+X保存退出。
    server ntp.fudan.edu.cn iburst perfer
    server time.asia.apple.com iburst
    server asia.pool.ntp.org iburst
    server ntp.nict.jp iburst
    server time.nist.gov iburst
    sudo /etc/init.d/ntp restart    //重启

    

////////////////////////////////////////////////////////eval xargs
st="ls | more"
`$st`   //将 | 和 more 看成了参数，而不是将文件按页显示
eval $st      //双次解析 一次解析变量 二次 放置执行？ 同js php shell

xargs 
#杀死指定规则进程
ps -ef | grep /usr/local/apache-tomcat-document/ | grep -v grep | cut -c 9-15 | xargs kill -9
ps -ef | grep 'mccp.conf' | grep -v grep | cut -c 9-15 | xargs kill -9
kill -9 25718 25719 25811 25812 一次排在后边
killall nginx #删除所有依据名字
ps -elf | grep <-v反转> 'aaa'
ps - ef”是Red Hat 里查看所有进程的命令。这时检索出的进程将作为下一条命令“grep LOCAL=NO”的输入。
　  grep LOCAL=NO”的输出结果是，所有含有关键字“LOCAL=NO”的进程，这是Oracle数据库中远程连接进程的共同特点。
　　grep -v grep”是在列出的进程中去除含有关键字“grep”的进程。
　　cut -c 9-15”是截取输入行的第9个字符到第15个字符，而这正好是进程号PID。
　　xargs kill -9”中的xargs命令是用来把前面命令的输出结果（PID）作为“kill -9”命令的参数，并执行该令。    

xargs的默认命令是echo，空格是默认定界符
cat test.txt | xargs -n3 //多行
cat test.txt | xargs -d'S' //设定分隔符
arg.txt : 
    file1.txt
    file2.txt
cat arg.txt | xargs -I {} cat -p {} -l  //{}占位符 替换
->
cat -p file1.txt -l
cat -p file2.txt -l



日期date格式化
1.date "+%Y-%m-%d"  
2.2013-02-19  
3.[root@root ~]# date "+%H:%M:%S"  
4.13:13:59  
5.[root@root ~]# date "+%Y-%m-%d %H:%M:%S"  
6.2013-02-19 13:14:19  
7.[root@root ~]# date "+%Y_%m_%d %H:%M:%S"    
8.2013_02_19 13:14:58  
9.[root@root ~]# date -d today   
10.Tue Feb 19 13:10:38 CST 2013  
11.[root@root ~]# date -d now  
12.Tue Feb 19 13:10:43 CST 2013  
13.[root@root ~]# date -d tomorrow  
14.Wed Feb 20 13:11:06 CST 2013  
15.[root@root ~]# date -d yesterday  
16.Mon Feb 18 13:11:58 CST 2013  

//源配置
{
sudo vim /etc/apt/sources.list                                                 
deb http://mirrors.aliyun.com/raspbian/raspbian/ stretch main contrib non-free rpi 


# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
}
sudo apt-get update  更新源

//apt-get
{
sudo apt autoremove 自动删除无依赖包
sudo apt-get update  更新源
sudo apt-get install package 安装包
sudo apt-get remove package 删除包
sudo apt-cache search package 搜索软件包
sudo apt-cache show package  获取包的相关信息，如说明、大小、版本等
sudo apt-get install package --reinstall  重新安装包
sudo apt-get -f install  修复安装
sudo apt-get remove package --purge 删除包，包括配置文件等
sudo apt-get build-dep package 安装相关的编译环境
sudo apt-get upgrade 更新已安装的包
sudo apt-get dist-upgrade 升级系统
sudo apt-cache depends package 了解使用该包依赖那些包
sudo apt-cache rdepends package 查看该包被哪些包依赖
sudo apt-get source package  下载该包的源代码
sudo apt-get clean && sudo apt-get autoclean 清理无用的包
sudo apt-get check 检查是否有损坏的依赖
//指定版本安装
apt-cache madison <<package name>>
将列出所有来源的版本。如下输出所示：
apt-cache madison vim
   vim | 2:7.3.547-1 | http://debian.mirrors.tds.net/debian/ unstable/main amd64 Packages
   vim | 2:7.3.429-2 | http://debian.mirrors.tds.net/debian/ testing/main amd64 Packages
   vim | 2:7.3.429-2 | http://http.us.debian.org/debian/ testing/main amd64 Packages
   vim | 2:7.3.429-2 | http://debian.mirrors.tds.net/debian/ testing/main Sources
   vim | 2:7.3.547-1 | http://debian.mirrors.tds.net/debian/ unstable/main Sources
apt-get install <<package name>>=<<version>>
sudo apt-get install openssh-client=1:6.6p1-2ubuntu1
}

//opencv
{
//这是win10下的子系统ubuntu终端使用的依赖
sudo apt-get install \ 
    libopencv-dev \         ##
    build-essential \ 
    checkinstall \ 
    cmake \ 
    pkg-config \ 
    yasm \ 
    libjpeg-dev \ 
    libpng-dev \ 
    libgphoto2-dev \ 
    libtiff5-dev \ 
    libjasper-dev \ 
    libavcodec-dev \ 
    libavformat-dev \ 
    libwebp-dev \
    libswscale-dev \ 
    libdc1394-22-dev \ 
    libxine2-dev \ 
    libgstreamer0.10-dev \ 
    libgstreamer-plugins-base0.10-dev \ 
    libv4l-dev \ 
    python-dev \ 
    python-numpy \ 
    libtbb-dev \ 
    libqt4-dev \    ##
    libgtk2.0-dev \ 
    libfaac-dev \   #libfaad-dev
    libmp3lame-dev \ 
    libopencore-amrnb-dev \ 
    libopencore-amrwb-dev \ 
    libtheora-dev \ 
    libvorbis-dev \ 
    libxvidcore-dev \ 
    x264 \ 
    v4l-utils \ 
    ffmpeg \ 
    gstreamer-plugins-base-devel \ ##
    qt5-default \ 


//整理树形版本依赖! !!!!!!!!!!!!!
apt-cache madison vim
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!需要配置专业的源pi专用最新 自动识别依赖
// 安装build-essential、cmake、git和pkg-config
sudo apt-get install build-essential cmake git pkg-config
// 安装jpeg格式图像工具包
sudo apt-get install libjpeg8-dev  
// 安装tif格式图像工具包 
sudo apt-get install libtiff5-dev   
// 安装JPEG-2000图像工具包
sudo apt-get install libjasper-dev 
// 安装png图像工具包
sudo apt-get install libpng12-dev 
//再安装视频I/O包（注意最后一个包的数字“4”后面是“L”）：
sudo apt-get install ffmpeg libavcodec-dev libavformat-dev  libavdevice-dev libswscale-dev libv4l-dev
//下面安装gtk2.0（树莓派很可能下载错误，更换中科大或者清华源即可，ubuntu有可能出现包版本过高的情况，需要将依赖包降级安装）：
sudo apt-get install libgtk2.0-dev
//优化函数包：
sudo apt-get install libatlas-base-dev gfortran
 打开源码文件夹，这里以我修改文章时最新的3.4.1为例
//开始编译
cd opencv-3.4.1
之后我们新建一个名为release的文件夹用来存放cmake编译时产生的临时文件：
// 新建release文件夹
mkdir release
// 进入release文件夹
cd release
设置cmake编译参数，安装目录默认为/usr/local ，注意参数名、等号和参数值之间不能有空格，但每行末尾“\”之前有空格，参数值最后是两个英文的点：

// CMAKE_BUILD_TYPE是编译方式，CMAKE_INSTALL_PREFIX是安装目录，OPENCV_EXTRA_MODULES_PATH是加载额外模块，INSTALL_PYTHON_EXAMPLES是安装官方python例程，BUILD_EXAMPLES是编译例程（这两个可以不加，不加编译稍微快一点点，想要C语言的例程的话，在最后一行前加参数INSTALL_C_EXAMPLES=ON \）

sudo cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.3.0/modules \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D BUILD_EXAMPLES=ON ..

sudo cmake -D CMAKE_BUILD_TYPE=RELEASE \
 -D CMAKE_INSTALL_PREFIX=/usr/local \
 -D INSTALL_C_EXAMPLES=ON \
 -D INSTALL_PYTHON_EXAMPLES=ON \
 -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.3.0/modules \
 -D BUILD_EXAMPLES=ON ..

-- WARNING: Can't build ffmpeg test code ' 模块丢失
打开详细提示
So I uncommented cmake/OpenCVFindLibsVideo.cmake:238 :
message(FATAL_ERROR "FFMPEG: test check build log:\n${TRY_OUT}")
之后开始正式编译过程（如果之前一步因为网络问题导致cmake下载缺失文件失败的话，可以尝试使用手机热点，并将release文件夹删除掉，重新创建release文件夹并cmake）：

// 编译，以管理员身份，否则容易出错
sudo make
// 安装
sudo make install
// 更新动态链接库
sudo ldconfig 


sudo pip install --upgrade setuptools
sudo pip install numpy Matplotlib scipy
//////////////////////////////////////////////////////////
在release目录下寻找lib目录里的cv2.so，
这个是python需要的，将其拷贝到python的库目录里。一般情况下是在
“/usr/local/lib/python2.7/dist-packages”里。
sudo cp lib/cv2.so /usr/local/lib/python2.7/dist-packages/
 
默认pkg-config(笔者的安装版本） 只会寻找 
/usr/share/pkgconfig/*.pc 和 */
/usr/lib/pkgconfig/*.pc ， */
/usr/lib64/pkgconfig/*.pc 。 '*/
而我通过源码方式安装的时候， 
对应的库的pc文件 默认安装到了 
/usr/local/lib/pkgconfig/。
 所以pkg-config找不到，也就认为没有安    装了。 
 经过笔者测试，如果通过 yum 安装的方式，则pc文件会放到 /usr/lib 或者 /usr/lib64/ 里，所以就没有这个问题。
解决方法：
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig;$PKG_CONFIG_PATH

//需要清理build 重新cmake

sudo apt-get install gtk+-3.0 gstreamer-base-1.0 gstreamer-video-1.0 gstreamer-app-1.0 gstreamer-riff-1.0 gstreamer-pbutils-1.0 libdc1394-2 libdc1394 

sudo apt-get install libgphoto2-dev gstreamer0.10-* libdc1394-*
sudo apt-get install libgphoto2-dev
sudo apt-get install gstreamer0.10-*
sudo apt-get install libdc1394-*
// sudo apt-get install libopencv-dev //??????????自编译非此
// sudo apt-get install python-opencv
}

//////////////////////////////////////////////网站信息抓取//////////////////////////////////////////////////
//whatweb
sudo apt-get install whatweb
异常/usr/bin/whatweb: /usr/lib/ruby/vendor_ruby/rchardet/universaldetector.rb:39: invalid multibyte escape: /[\x80-\xFF]/ (SyntaxError)
解决
sudo vi /usr/lib/ruby/vendor_ruby/rchardet/universaldetector.rb
文件第一行加入
# encoding: US-ASCII

sudo apt-get install nmap  //渗透测试工具nmap:
//////////////////////////////////////////////网站信息抓取//////////////////////////////////////////////////










//php环境
{
sudo apt-get install nginx php7.0-fpm php7.0-cli php7.0-curl php7.0-gd php7.0-mcrypt php7.0-cgi
sudo apt-get install nginx php5.0-fpm php5.0-cli php5.0-curl php5.0-gd php5.0-mcrypt php5.0-cgi

}

//nginx搭建
http://blog.csdn.net/shuxiaogd/article/details/47662115
sudo apt-get install nginx  默认目录/usr/local/nginx。 
pi: /etc/nginx
ln -s /etc/nginx ~/nginx/nginx
代理静态html angularJs
转发后台请求python web tornado
配置/etc/nginx/nginx.conf server  upstream 



//设置DNS
{
    DNS是用来解析域名用的，平时我们访问网站都是直接输入一个网址，
    而dns把这个网址解析到一个IP。关于dns的概念，如果你很陌生的话，
    那就去网上查一下吧。在linux下面设置dns非常简单，
    只要把dns地址写到一个配置文件中即可。这个配置文件就是/etc/resolv.conf
1）一个IP后面可以跟多个域名，可以是几十个甚至上百个；
2）每行只能有一个IP，也就是说一个域名不能对应多个IP；
3）如果有多行中出现相同的域名（前面IP不一样），会按最前面出现的记录来解析。
    
}

//Linux 网络和监控命令
{
    ;/hostname
hostname 没有选项，显示主机名字
hostname –d 显示机器所属域名
hostname –f 显示完整的主机名和域名
hostname –i 显示当前机器的ip地址
     ;/ping
ping 将数据包发向用户指定地址。当包被接收，目标机器发送返回数据包。ping 主要有两个作用：
用来确认网络连接是畅通的。
用来查看连接的速度信息。
    ifconfig
查看用户网络配置。它显示当前网络设备配置。对于需要接收或者发送数据错误查找，这个工具极为好用。
    iwconfig
iwconfig 工具与 ifconfig 和ethtool类似。是用于无线网卡的 . 你可以用他查看设置基本的Wi-Fi 网络信息,例如 SSID, channel和encryption.还有其他很多配置你也可以查看和修改，, 包括 接收灵敏度, RTS/CTS, 发送数据包的分片大小,以及无线网卡的重传机制。
    ;/nslookup
nslookup 这个命令在 有ip地址时，可以用这个命令来显示主机名，可以找到给定域名的所有ip地址。而你必须连接到互联网才能使用这个命令。
例子. nslookup blogger.com
你也可以使用 nslookup 从ip获得主机名或从主机名获得ip。
    ;/traceroute
一个方便的工具。可用来查看数据包在提交到远程系统或者网站时候所经过的路由器的IP地址、跳数和响应时间。同样你必须链接到互联网才能使用这个命令
    finger
查看用户信息。显示用户的登录名字、真实名字以及登录终端的名字和登录权限。这是unix一个很老的命令，现在已很少使用了。
    telnet
通过telnet协议连接目标主机，如果telnet连接可以在任一端口上完成即代表着两台主机间的连接良好。
telnet hostname port - 使用指定的端口telnet主机名。这通常用来测试主机是否在线或者网络是否正常。
    ethtool
ethtool允许你查看和更改网卡的许多设置（不包括Wi-Fi网卡）。你可以管理许多高级设置，包括tx/rx、校验及网络唤醒功能。下面是一些你可能感兴趣的基本命令：
ethtool -i 显示一个特定网卡的驱动信息，检查软件兼容性时尤其有用
ethtool -p 启动一个适配器的指定行为，比如让适配器的LED灯闪烁，以帮助你在多个适配器或接口中标识接口名称
ethtool -s 显示网络统计信息
ethtool speed <10|100|1000> 设置适配器的连接速度，单位是Mbps
    ;/netstat
发现主机连接最有用最通用的Linux命令。你可以使用"netstat -g"查询该主机订阅的所有多播组（网络）
netstat -nap | grep port 将会显示使用该端口的应用程序的进程id
netstat -a  or netstat –all 将会显示包括TCP和UDP的所有连接
netstat --tcp  or netstat –t 将会显示TCP连接
netstat --udp or netstat –u 将会显示UDP连接
netstat -g 将会显示该主机订阅的所有多播网络。

}

//Linux系统的进程间通信的方式
{ 
管道(pipe)：管道是一种半双工的通信方式，数据只能单向流动，而且只能在具有亲缘关系的进程间使用(进程的亲缘关系通常是指父子进程关系)。
命名管道(named pipe)：命名管道也是半双工的通信方式，但是它允许无亲缘关系进程间的通信。
信号量(semophore)：信号量是一个计数器，可以用来控制多个进程对共享资源的访问。它常作为一种锁机制，防止某进程正在访问共享资源时，其他进程也访问该资源。因此，主要作为进程间以及同一进程内不同线程之间的同步手段。
消息队列(message queue)：消息队列就是一个消息的链表，存放在内核中并由消息队列标识符标识。消息队列克服了信号传递信息少、管道只能承载无格式字节流以及缓冲区大小受限等缺点。
信号(sinal)：信号是一种比较复杂的通信方式，用于通知接收进程某个事件已经发生。
共享内存(shared memory)：共享内存就是映射一段能被其他进程所访问的内存，这段共享内存由一个进程创建，但多个进程都可以访问。共享内存是最快的IPC方式，它是针对其他进程间通信方式运行效率低而专门设计的。它往往与其他通信机制，如信号配合使用，来实现进程间的同步和通信。
套接字(socket)：套接字也是一种进程间通信机制，与其他通信机制不同的是，它可用于不同主机间的进程通信。
}

//Linux终端管理进程
{
    通配符 星号”*”
    命令行历史 history
    目录~,.& ..
    后台运行命令 &
    条件执行 && ||
    
    
    |less 命令对输出进行管道，这样你就可以按你的速度滚动阅读：
top命令是一个常用的查看系统资源使用情况和查看占用系统资源最多的进程
htop命令是top的改进版 Linux发行版本都没有安装htop——   sudo apt-get install htop     
ps命令可以列出正在运行的进程。以下命令列出所有在你系统上运行的命令： ps -A 
pstree  以显示进程信息。它以树的形式显示
kill 可以根据进程ID来杀死进程。你可以使用ps -A，top,或者grep命令获取到进程ID。 kill pid 
pgrep 会返回所有匹配这个关键词的进程ID。例如，你可以使用以下命令寻找Firefox的PID: pgrep firefox 
pkill & killall pkill和killall命令可以根据进程的名字杀死一个进程。使用以下任一方法都可以杀死Firefox进程： pkill firefox  killall firefox 
renice 用来改变进程的nice值。nice值代表进程的优先级。renice 19 pid    -19的nice值是非常高的优先级，相反，19是非常低的优先级。0是默认的优先级。
xkill 可以轻易杀死图形程度的命令。运行它之后，你的光标会变成x符号。点击相应的图形程序的窗口就可以杀死该程序。如果你中途要放弃操作，你可以点击鼠标右键取消。

ps -ef|grep LOCAL=NO|grep -v grep|cut -c 9-15|xargs kill -9
　　管道符“|”用来隔开两个命令，管道符左边命令的输出会作为管道符右边命令的输入。下面说说用管道符联接起来的

几个命令：
     “ps - ef”是Red Hat 里查看所有进程的命令。这时检索出的进程将作为下一条命令“grep LOCAL=NO”的输入。
　  “grep LOCAL=NO”的输出结果是，所有含有关键字“LOCAL=NO”的进程，这是Oracle数据库中远程连接进程的共同特点。
　　“grep -v grep”是在列出的进程中去除含有关键字“grep”的进程。
　　“cut -c 9-15”是截取输入行的第9个字符到第15个字符，而这正好是进程号PID。
　　“xargs kill -9”中的xargs命令是用来把前面命令的输出结果（PID）作为“kill -9”命令的参数，并执行该令。    
“kill -9”会强行杀掉指定进程，这样就成功清除了oracle的所有远程连接进程。其它类似的任务，只需要修改“grep LOCAL=NO”中的关键字部分就可以了。
 
ps -ef|grep /usr/local/apache-tomcat-document/|grep -v grep|cut -c 9-15|xargs kill -9

}
//telnet 通过 cmd 依靠ip/端口/用户名密码 远程登录
{
     sudo service openbsd-inetd start  
     /etc/init.d/openbsd-inetd restart
    
您的位置: Linux系统教程 > Ubuntu系统 >
ubuntu 14.04中打开telnet服务步骤
时间:2016-01-15来源:linux网站 作者:Linux_ever

 
1、首先查看telnet运行状态
#netstat -a | grep telnet
输出为空，表示没有开启该服务

2、安装openbsd-inetd
#apt-get install openbsd-inetd
如果已经安装过了，会提示已经安装过了，直接执行下面的步骤就可以了。

3、安装telnetd
#apt-get install telnetd
安装完之后，查看/etc/inetd.conf的内容会多了一行telnet    stream  tcp     nowait  telnetd /usr/sbin/tcpd  /usr/sbin/in.telnetd
#cat /etc/inetd.conf  | grep telnet
输出： telnet     stream  tcp     nowait  telnetd /usr/sbin/tcpd  /usr/sbin/in.telnetd

4、重启openbsd-inetd
# /etc/init.d/openbsd-inetd restart
输出：* Restarting internet superserver inetd

5、查看telnet运行状态
#netstat -a | grep telnet
输出：tcp　　0　　0 *:telnet　　*:*　　LISTEN
此时表明已经开启了telnet服务。
    
    Telnet 客户端命常用命令：
　　open : 使用 openhostname 可以建立到主机的 Telnet 连接。
　　close : 使用命令 close 命令可以关闭现有的 Telnet 连接。
　　display : 使用 display 命令可以查看 Telnet 客户端的当前设置。
　　send : 使用 send 命令可以向 Telnet 服务器发送命令。支持以下命令：
　　ao : 放弃输出命令。
　　ayt : “Are you there”命令。
　　esc : 发送当前的转义字符。
　　ip : 中断进程命令。
　　synch : 执行 Telnet 同步操作。
　　brk : 发送信号。
　　上表所列命令以外的其他命令都将以字符串的形式发送至 Telnet 服务器。例如，sendabcd 将发送字符串 abcd 至 Telnet 服务器，这样，Telnet 会话窗口中将出现该字符串。
　　quit
　　使用 quit 命令可以退出 Telnet 客户端。


}

//ssh 通过winscp 和 putty<终端>  依靠ip/端口/用户名密码 远程登录
{
    
在计算机之间传递文件（使用scp）
X-forwarding – 连接到远端的机器，并且开启一个GUI应用，看起来它们就像在本地开启的一样，即使远端的机器并没有提供X服务。
端口转发 – 将到本地端口的连接转发到远端机器的端口，或者将到远端机器端口的连接转发到本地端口
SOCKS 代理 – 允许你将一个支持SOCKET代理的应用上的所有连接转发到远端机器。这对于如何更安全使用公共wifi浏览网络和绕过严格的防火墙是很有用的。
在本地机器输入一次密码，然后就可以通过ssh的key代理来使用安全身份登陆其余的远端机器，而不需要重复输入你的密码了。


  sudo service ssh start   
 /etc/init.d/ssh restart
下列软件包有未满足的依赖关系： 版本
 openssh-server : 依赖: openssh-client (= 1:6.6p1-2ubuntu1)
E: 无法修正错误，因为您要求某些软件包保持现状，就是它们破坏了软件包间的依赖关系。
sudo apt-get install openssh-client=1:6.6p1-2ubuntu1
openssh-server是依赖于openssh-clien的,那ubuntu不是自带了openssh-client吗?原由是自带的openssh-clien与所要安装的openssh-server所依赖的版本不同,这里所依赖的版本是

//免密码登录ssh
对于debian/ubuntu系统来说，安装方式很简单：
sudo apt-get install sshpass
对于其他的linux,可以编译sshpass的源码安装：
wget http://sourceforge.net/projects/sshpass/files/sshpass/1.05/sshpass-1.05.tar.gz  
tar xvzf sshpass-1.05.tar.gz  
./configure 
make  
sudo make install
sshpass -p "XXX" ssh user@IP
//首次需要ssh 直接登录一次 
//之后才能使用sshpass登录?
}

//管道 多进程 并发
{
1.1. linux后台进程 
Unix是一个多任务系统，允许多用户同时运行多个程序。shell的元字符&提供了在后台运行不需要键盘输入的程序的方法。输入命令后，其后紧跟&字符，该命令就会被送往到Linux后台执行，而终端又可以继续输入下一个命令了。 
比如： 
sh a.sh & 
这三个命令就会被同时送往linux后台执行，在这个程度上，认为这三个命令并发执行了。
1.2. linux文件描述符
文件描述符（缩写fd）在形式上是一个非负整数。实际上，它是一个索引值，指向内核为每一个进程所维护的该进程打开文件的记录表。当程序打开一个现有文件或者创建一个新文件时，内核向进程返回一个文件描述符。每一个unix进程，都会拥有三个标准的文件描述符，来对应三种不同的流：
文件描述符	名称
0	Standard Input
1	Standard Output
2	Standard Error
每一个文件描述符会对应一个打开文件，同时，不同的文件描述符也可以对应同一个打开文件；同一个文件可以被不同的进程打开，也可以被同一个进程多次打开。

在/proc/PID/fd中，列举了进程PID所拥有的文件描述符，例如

#!/bin/bash
source /etc/profile;

# $$表示当前进程的PID
PID=$$

# 查看当前进程的文件描述符指向
ll /proc/$PID/fd
echo "-------------------";echo

# 文件描述符1与文件tempfd1进行绑定
( [ -e ./tempfd1 ] || touch ./tempfd1 ) && exec 1<>./tempfd1

# 查看当前进程的文件描述符指向
ll /proc/$PID/fd
echo "-------------------";echo; 
[ouyangyewei@localhost learn_linux]$ sh learn_redirect.sh 
total 0
lrwx------. 1 ouyangyewei ouyangyewei 64 Jan  4 22:17 0 -> /dev/pts/0
lrwx------. 1 ouyangyewei ouyangyewei 64 Jan  4 22:17 1 -> /dev/pts/0
lrwx------. 1 ouyangyewei ouyangyewei 64 Jan  4 22:17 2 -> /dev/pts/0
lr-x------. 1 ouyangyewei ouyangyewei 64 Jan  4 22:17 255 -> /home/ouyangyewei/workspace/learn_linux/learn_redirect.sh
-------------------

[ouyangyewei@localhost learn_linux]$ cat tempfd1 
total 0
lrwx------. 1 ouyangyewei ouyangyewei 64 Jan  4 22:17 0 -> /dev/pts/0
lrwx------. 1 ouyangyewei ouyangyewei 64 Jan  4 22:17 1 -> /home/ouyangyewei/workspace/learn_linux/tempfd1
lrwx------. 1 ouyangyewei ouyangyewei 64 Jan  4 22:17 2 -> /dev/pts/0
lr-x------. 1 ouyangyewei ouyangyewei 64 Jan  4 22:17 255 -> /home/ouyangyewei/workspace/learn_linux/learn_redirect.sh
-------------------
上述的例子中第12行，将文件描述符1与文件tempfile进行了绑定，此后，文件描述符1指向了tempfile文件，标准输出被重定向到了文件tempfile中。
1.3. linux管道
在Unix或类Unix操作系统中，管道是一个由标准输入输出链接起来的进程集合，因此，每一个进程的输出将直接作为下一个进程的输入，
linux管道包含两种：
匿名管道 命名管道
管道有一个特点，如果管道中没有数据，那么取管道数据的操作就会滞留，直到管道内进入数据，然后读出后才会终止这一操作；同理，写入管道的操作如果没有读取管道的操作，这一动作就会滞留。
1.3.1. 匿名管道
在Unix或类Unix操作系统的命令行中，匿名管道使用ASCII中垂直线|作为匿名管道符，匿名管道的两端是两个普通的，匿名的，打开的文件描述符：一个只读端和一个只写端，这就让其它进程无法连接到该匿名管道。
cat file | less
1
1
为了执行上面的指令，Shell创建了两个进程来分别执行cat和less。下图展示了这两个进程是如何使用管道的：
unix_unnamed_pipe 
有一点值得注意的是两个进程都连接到了管道上，这样写入进程cat就将其标准输出（文件描述符为fd 1）连接到了管道的写入端，读取进程less就将其标准输入（文件描述符为fd 0）连接到了管道的读入端。实际上，这两个进程并不知道管道的存在，它们只是从标准文件描述符中读取数据和写入数据。shell必须要完成相关的工作。

1.3.2. 命名管道（FIFO，First In First Out）

命名管道也称FIFO，从语义上来讲，FIFO其实与匿名管道类似，但值得注意：

在文件系统中，FIFO拥有名称，并且是以设备特俗文件的形式存在的；
任何进程都可以通过FIFO共享数据；
除非FIFO两端同时有读与写的进程，否则FIFO的数据流通将会阻塞；
匿名管道是由shell自动创建的，存在于内核中；而FIFO则是由程序创建的（比如mkfifo命令），存在于文件系统中；
匿名管道是单向的字节流，而FIFO则是双向的字节流；
比如，可以利用FIFO实现单服务器、多客户端的应用程序: 
unix_named_pipe

有了上面的知识准备，现在可以开始讲述，linux多进程并发时，如何控制每次并发的进程数。

// 正则表达式:
{
   是指一个用来描述或者匹配一系列符合某个句法规则的字符串的单个字符串。本文介绍如何使用grep及egrep命令。而扩展正则表达式比基本正则表达式拥有更强大的功能。  
grep的主要功能用于检索文件内容，字符串等的工具。可以根据用户指定的“模式（pattern）”对目标文本进行搜索过滤，显示出被“模式pattern”匹配到的行。 
 
grep [OPTIONS]PATTERN [FILE...] 
PATTERN:是文本字符和正则表达式的元字符组合而成的匹配条件，可用单引号‘ ’将pattern括起来以避免shell通配的影响，强引用不替换而显示字符本身。" " 双引号，字符串中的` ` ,$, \ 等特殊字符会被shell解释替换后，再传递给grep。对普通的字符串（没有特殊字符和空格的字符串）也可以不加引号，直接搜索。 
     OPTIONS：（这里给出常用的选项） 
 -i 忽略大小写 
 -c 显示被匹配到的行数 
-n 输出行号 
-v 反向选择，即找没有搜索字符串的行 
-o 仅显示匹配到的内容 
-w 匹配单词 
-A # 连同匹配行的下#行一并显示，#代表任意数字 
-B # 连同匹配行的上#行一并显示，#代表任意数字 
-C # 连同匹配行的上下#行一并显示，#代表任意数字 
-R或-r 递归搜索目录或子目录下匹配的字所在文件（可配合find命令 
-E  相当于egrep 支持扩展的正则表达式 
-F  相当于fgrep 不支持正则表达式 
--color对匹配的内容以颜色显示 
-V  显示grep版本 
正则表达式：            
默认匹配次数：贪婪模式，尽可能多的去匹配 
    . 匹配任意单个字符 
    \.表示.本身   \逃逸符 
     * 匹配其前面的字符任���次可为0次 
    .* 任意长度的任意字符 
    \? 匹配其前面字符1次或0次 
x\{m\}：匹配其前面的字符“x”m次(精确匹配) 
x\{m,\}：匹配其前面的字符“x”至少m次 
x\{m,n\}：匹配其前面的字符“x”至少m次，至多n次 
 \{1,\} 1次至无上限 \{0,3\}至少3次 
    ^ 锚定行首，此字符后面的任意内容必须出现在行首  
    $ 锚定行尾，次字符前面的任意内容必须出现在行尾  
    ^$表示空行 
    [ ] 匹配指定范围内的任意单个字符 
    [^ ] 匹配指定范围外的任意单个字符 
    \< 其后面的任意字符必须作为单词的首部出现  \b 
    \> 其前面的任意字符必须作为单词的尾部出现  \b 
    \<\> 锚定单词例如 \<root\> 
 纯数字 [[:digit:]]或[0-9] 
    小写字母 [[:lower:]]或[a-z] 
    大写字母 [[:upper:]]或[A-Z] 
    大小写字母 [[:alpha:]]或[a-zA-Z] 
    数字加字母 [[:alnum:]]或[0-9a-zA-Z] 
    空白字符 [[:space:]]  非空白字符[^[:space:]] 
    标点符号 [[:punct:]] 
    \d  匹配任何十进制数，相当于[0-9]     -P选项加上 
 \D 匹配任何非数字字符，相当于[^0-9]    -P选项加上 
 \s  匹配任何空白字符， 
  \S  匹配任何非空白字符， 
  \w  匹配任何字母数字字符，相当于[a-zA-Z0-9] 
 \W 匹配任何非字母数字字符，相当于[^a-zA-Z0-9]  ' 
 \\  匹配"\" 
 \( \) 分组后项引用  \1 引用第一个左括号以及与之对应的右括号所包括的所有内容。    \2 \3 … 
扩展正则表达式中增加了几个与正则表达式有区别的新内容： 
    +   匹配其前面的字符至少1次       \{1,\}正则中近似 
    ？ 匹配紧挨在其前面的字符0次或1次   \?正则中 
    {m,n}  匹配前面字符至少m次至多n次 {1，}表示1至无限 {0,3}表示0-3 
    （）分组  \1 \2 \3 … 
     |  或者  
}

//mv命令既可以重命名
{
    for i in `seq -w 10`; do touch stu\_$i\_linux.jpg ; done
    rename \_linux '' *.jpg
    rename '\_linux' '' *.jpg       
mv命令既可以重命名，又可以移动文件或文件夹。     '
例子：将目录A重命名为B
mv A B
例子：将/a目录移动到/b下，并重命名为c
mv /a /b/c
其实在文本模式中要重命名文件或目录，只需要使用mv命令就可以了，比如说要将一个名为abc的文件重命名为1234：
mv abc 1234
注意，如果当前目录下也有个1234的文件的话，这个文件是会将它覆盖的。
下面介绍Linux系统中另一个重命名命令 rename命令的用法。

rename版本如果是perl版本的，那rename命令是支持正则的；因此在perl版本的rename下，执行上述命令就可以成功，如果rename版本是c版本的，那么上述命令是不成功的。
这个是版本支持的问题，所以不必深究。
}
//软链接 硬链接
ln -s source     dist     #建立软连接 快捷方式
ln     source     dist     #建立硬连接 硬链接不能连接两个不同文件系统上的文件 类似拷贝副本

//sh ./ bash dash语法错误
的原因在于两次执行的不是同一种shell，在用./sample的方式执行的时候，系统会使用脚本首行声明的/bin/bash来解释脚本，而用sh方式执行的时候，系统会调用sh这个程序，在我的机器上看一下sh这个程序的来源：
snow@snow-desktop:~$ ll `which sh`  
lrwxrwxrwx 1 root root 4 11月  9 10:17 /bin/sh -> dash*  

ln -s /bin/bash /bin/sh
或者如下：
sudo dpkg-reconfigure dash
出现提示界面问是否要dash的时候，选No就行了。反馈如下：

//回响
///$ echo -e ${PATH////'\n'}
//邮件
安装 Evolution 
有PPA可用，支持 Ubuntu 14.04 及衍生系统。打开终端，输入以下命令： 
sudo add-apt-repository ppa:fta/gnome3 
sudo apt-get update 
sudo apt-get install evolution


//QQ
    sudo dpkg -i fonts-wqy-microhei_0.2.0-beta-2_all.deb  
    sudo dpkg -i ttf-wqy-microhei_0.2.0-beta-2_all.deb  
    sudo dpkg -i wine-qqintl_0.1.3-2_i386.deb   
    如果，最后一步报错。使用如下命令修复：
   [objc] view plain copy
    sudo apt-get -f install   
    sudo dpkg -i wine-qqintl_0.1.3-2_i386.deb  

//eclipse 启动
Eclipse运行时需要JRE的支持，因为Eclipse包里是不带JRE的，因此要使用Eclipse首先就要安装好JRE或JDK
然后给Eclipse做相应配置。
大致说来，配置Eclipse启动时使用JRE有四种方式：
一、把jre目录直接拷贝到eclipse目录下面
二、在eclipse.ini里面添加，例如：
-vm
G:\Program Files\Java\jre7\bin\javaw.exe
注意，一定要在-vmargs这一行的上面分两行添加(路径有无空格，正斜杠反斜杠均可，且不区分大小写)
三、使用快捷方式在其属性页设置或命令行直接输入启动参数-vm D:\jre\bin\javaw.exe(路径有无空格，正斜杠反斜杠均可，且不区分大小写)
四、在当前用户环境变量PATH或通用环境变量Path里设置D:\jre\bin(路径有无空格，正斜杠反斜杠均可，且不区分大小写，但是要确保eclipse.ini没有-vm的垃圾配置，否则启动会在此失败终止) 

//环境变量
export JAVA_HOME=/home/walker/software/jdk1.7.0_79
export CLASSPATH=$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/bin  
PATH=$PATH:$CLASSPATH
source /etc/profile

1、在/etc/profile文件中添加变量【对所有用户生效（永久的）】
      用VI在文件/etc/profile文件中增加变量，该变量将会对Linux下所有用户有效，并且是“永久的”。
      例如：编辑/etc/profile文件，添加CLASSPATH变量
      # vi /etc/profile
      export CLASSPATH=./JAVA_HOME/lib;$JAVA_HOME/jre/lib
      注：修改文件后要想马上生效还要运行# source /etc/profile不然只能在下次重进此用户时生效。
      2、在用户目录下的.bash_profile文件中增加变量【对单一用户生效（永久的）】
      用VI在用户目录下的.bash_profile文件中增加变量，改变量仅会对当前用户有效，并且是“永久的”。
      例如：编辑guok用户目录（/home/guok）下的.bash_profile
      $ vi /home/guok/.bash.profile
      添加如下内容：
      export CLASSPATH=./JAVA_HOME/lib;$JAVA_HOME/jre/lib
      注：修改文件后要想马上生效还要运行$ source /home/guok/.bash_profile不然只能在下次重进此用户时生效。
      3、直接运行export命令定义变量【只对当前shell（BASH）有效（临时的）】
      在shell的命令行下直接使用[export 变量名=变量值]
      定义变量，该变量只在当前的shell（BASH）或其子shell（BASH）下是有效的，shell关闭了，变量也就失效了，再打开新shell时就没有这个变量，需要使用的话还需要重新定义。
三、PATH声明，其格式为：
      PATH=$PATH:<PATH 1>:<PATH 2>:<PATH 3>:------:<PATH N>
      你可以自己加上指定的路径，中间用冒号隔开。环境变量更改后，在用户下次登陆时生效。
      如果想立刻生效，则可执行下面的语句：$source .bash_profile
      需要注意的是，最好不要把当前路径”./”放到PATH里，这样可能会受到意想不到的攻击。
      完成后，可以通过$ echo $PATH查看当前的搜索路径。这样定制后，就可以避免频繁的启动位于shell搜索的路径之外的程序了

//防火墙问题
      {
一、Linux下开启/关闭防火墙命令
1、永久性生效，重启后不会复原。
开启： chkconfig iptables on
关闭： chkconfig iptables off
2、 即时生效，重启后复原
开启： service iptables start
关闭： service iptables stop
需要说明的是对于Linux下的其它服务都可以用以上命令执行开启和关闭操作。
在当开启了防火墙时，做如下设置，开启相关端口，
修改/etc/sysconfig/iptables 文件，添加以下内容：
-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT
-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT
二、UBuntu关闭防火墙
iptables -A INPUT -i !   PPP0   -j ACCEPT
三、CentOS Linux 防火墙配置及关闭
执行”setup”命令启动文字模式配置实用程序,在”选择一种工具”中选择”防火墙配置”,然后选择”运行工具”按钮,出现防火墙配置界面,将”安全级别”设为”禁用”,然后选择”确定”即可.
或者用命令:
#/sbin/iptables -I INPUT -p tcp –dport 80 -j ACCEPT
#/sbin/iptables -I INPUT -p tcp –dport 22 -j ACCEPT
#/etc/rc.d/init.d/iptables save
这样重启计算机后,防火墙默认已经开放了80和22端口
这里应该也可以不重启计算机：
#/etc/init.d/iptables restart
关闭防火墙服务即可：
查看防火墙信息：
#/etc/init.d/iptables status
关闭防火墙服务：
#/etc/init.d/iptables stop
}
//解压问题
{
	
语法：tar [主选项+辅选项] 文件或者目录
使用该命令时，主选项是必须要有的，它告诉tar要做什么事情，辅选项是辅助使用的，可以选用。
主选项：
c 创建新的档案文件。如果用户想备份一个目录或是一些文件，就要选择这个选项。相当于打包。
x 从档案文件中释放文件。相当于拆包。
t 列出档案文件的内容，查看已经备份了哪些文件。
特别注意，在参数的下达中， c/x/t 仅能存在一个！不可同时存在！因为不可能同时压缩与解压缩。
辅助选项：
-z ：是否同时具有 gzip 的属性？亦即是否需要用 gzip 压缩或解压？ 一般格式为xx.tar.gz或xx. tgz
-j ：是否同时具有 bzip2 的属性？亦即是否需要用 bzip2 压缩或解压？一般格式为xx.tar.bz2  
-v ：压缩的过程中显示文件！这个常用
-f ：使用档名，请留意，在 f 之后要立即接档名喔！不要再加其他参数！
-p ：使用原文件的原来属性（属性不会依据使用者而变）
tar –xvf file.tar //解压 tar包 
tar -xzvf file.tar.gz //解压tar.gz 
tar -xjvf file.tar.bz2 //解压 tar.bz2 
tar –xZvf file.tar.Z //解压tar.Z 
unrar e file.rar //解压rar 
unzip file.zip //解压zip 
--exclude FILE：在压缩的过程中，不要将 FILE 打包！
范例一：将整个 /etc 目录下的文件全部打包成为 /tmp/etc.tar
[root@linux ~]# tar -cvf /tmp/etc.tar /etc　　　　<==仅打包，不压缩！
[root@linux ~]# tar -zcvf /tmp/etc.tar.gz /etc　　<==打包后，以 gzip 压缩
[root@linux ~]# tar -jcvf /tmp/etc.tar.bz2 /etc　　<==打包后，以 bzip2 压缩
# 特别注意，在参数 f 之后的文件档名是自己取的，我们习惯上都用 .tar 来作为辨识。
# 如果加 z 参数，则以 .tar.gz 或 .tgz 来代表 gzip 压缩过的 tar file ～
# 如果加 j 参数，则以 .tar.bz2 来作为附档名啊～
# 上述指令在执行的时候，会显示一个警告讯息：
# '『tar: Removing leading `/" from member names』那是关於绝对路径的特殊设定。 '
范例二：查阅上述 /tmp/etc.tar.gz 文件内有哪些文件？ 
[root@linux ~]# tar -ztvf /tmp/etc.tar.gz
# 由於我们使用 gzip 压缩，所以要查阅该 tar file 内的文件时，
# 就得要加上 z 这个参数了！这很重要的！
范例三：将 /tmp/etc.tar.gz 文件解压缩在 /usr/local/src 底下
[root@linux ~]# cd /usr/local/src
[root@linux src]# tar -zxvf /tmp/etc.tar.gz
# 在预设的情况下，我们可以将压缩档在任何地方解开的！以这个范例来说
# 我先将工作目录变换到 /usr/local/src 底下，并且解开 /tmp/etc.tar.gz
# 则解开的目录会在 /usr/local/src/etc ，另外，如果您进入 /usr/local/src/etc
# 则会发现，该目录下的文件属性与 /etc/ 可能会有所不同喔！
范例四：在 /tmp 底下，我只想要将 /tmp/etc.tar.gz 内的 etc/passwd 解开而已
[root@linux ~]# cd /tmp
[root@linux tmp]# tar -zxvf /tmp/etc.tar.gz etc/passwd
# 我可以透过 tar -ztvf 来查阅 tarfile 内的文件名称，如果单只要一个文件，
# 就可以透过这个方式来下达！注意到！ etc.tar.gz 内的根目录 / 是被拿掉了！
范例五：我要备份 /home, /etc ，但不要 /home/dmtsai
[root@linux ~]# tar --exclude /home/dmtsai -zcvf myfile.tar.gz /home/* /etc  */
另外：tar命令的C参数
　　$ tar -cvf file2.tar /home/usr2/file2
　　tar: Removing leading '/' from members names
　　home/usr2/file2
　　该命令可以将/home/usr2/file2文件打包到当前目录下的file2.tar中，需要注意的是：使用绝对路径标识的源文件，在用tar命令压缩后，文件名连同绝对路径（这里是home/usr2/，根目录'/'被自动去掉了）一并被压缩进来。使用tar命令解压缩后会出现以下情况：
　　$ tar -xvf file2.tar
　　$ ls
　　…… …… home …… ……
　　解压缩后的文件名不是想象中的file2，而是home/usr2/file2。
　　$ tar -cvf file2.tar -C /home/usr2 file2
　　该命令中的-C dir参数，将tar的工作目录从当前目录改为/home/usr2，将file2文件（不带绝对路径）压缩到file2.tar中。注意：-C dir参数的作用在于改变工作目录，其有效期为该命令中下一次-C dir参数之前。
　　使用tar的-C dir参数，同样可以做到在当前目录/home/usr1下将文件解压缩到其他目录，例如：
　　$ tar -xvf file2.tar -C /home/usr2
　　而tar不用-C dir参数时是无法做到的：
　　$ tar -xvf file2.tar /home/usr2
　　tar: /tmp/file: Not found in archive
　　tar: Error exit delayed from previous errors 
//对于.7z
支持 7Z,ZIP,Zip64,CAB,RAR,ARJ,GZIP,BZIP2,TAR,CPIO,RPM,ISO,DEB 压缩文件格式
安装： sudo apt-get install p7zip p7zip-full p7zip-rar
# 7z a yajiu.7z yajiu.jpg yajiu.png 将yajiu.jpg和yajiu.png压缩成一个7z包
# 7z a yajiu.7z *.jpg 将所有.jpg的文件压缩成一个7z包
# 7z a yajiu.7z yajiu 将文件夹yajiu压缩成一个7z包
# 7z e yajiu.7z 将yajiu.7z中的所有文件解压出来，e是解压到当前路径
# 7z x yajiu.7z 将yajiu.7z中的所有文件解压出来，x是解压到压缩包命名的目录下

}

//挂载ntfs磁盘问题
sudo apt-get install ntfsprogs
sudo ntfsfix /dev/sda5 



//用户组问题
adduser walker 新建用户
passwd walker 修改密码
userdel walker 删除用户
groupadd admin 用户组
groupdel admin 删除组
usermod -g 用户组 用户名
强行设置某个用户所在组
usermod -G 用户组 用户名
把某个用户改为 group(s)
usermod -a -G 用户组 用户名
把用户添加进入某个组(s）
su - 而不是su，这是因为su -和su的区别在于su - 拥有root的环境变量即 / 目录下的 .bash_profile和 .bashrc文件，而su只拥有当前用户环境
//修改用户名
usermod -l walker walkerdust
//初次登录ubuntu的root登录问题
输入 root 密码 安装时 设置的是用户密码 而不是root 密码 ununtu 只能调用 root 不能直接 root登录
设置root密码 方法如下：
1：输入 sudo passwd root
2：输入用户密码（安装时设置的）
3：输入想设置的root密码
4：再次输入root密码 enter结束 就成功了

ps 查看tty？
top来对进程排序，结束进程等.

//python-rtmp
{   
sudo pip install python-librtmp     //只需要此


sudo apt-get install gcc* python-dev libffi-dev* -y
git clone git://git.ffmpeg.org/rtmpdump
cd rtmpdump/librtmp
make && make install 
wget -S https://pypi.python.org/packages/83/3c/00b553fd05ae32f27b3637f705c413c4ce71290aa9b4c4764df694e906d9/cffi-1.7.0.tar.gz#md5=34122a545060cee58bab88feab57006d
cd cffi-1.7.0
sudo python setup.py install
wget -S https://pypi.python.org/packages/48/a6/33b1a5864e22de3e59dd29fcbc2602462511c04a31057b16baec639d7d4f/python-librtmp-0.3.0.tar.gz#md5=f7afe8d463214072281998fa84553927
cd python-librtmp-0.3.0
sudo python setup.py install 
python
import librtmp
find / -name librtmp.so.1
ldconfig    //自动统计导入so文件

}

//编译安装ffmpeg
{
        http://ffmpeg.org/releases/ffmpeg-2.8.11.tar.gz
wget -c http://ffmpeg.org/releases/ffmpeg-3.0.tar.bz2 
tar xvf ffmpeg-3.0.tar.bz2 
cd ffmpeg-3.0 
./configure --host-cppflags=-fPIC --host-cflags=-fPIC --enable-shared 

make 
sudo make install
}


//openssl安装
    这里需要特别的注意：openssl 版本不能太高，太高有些接口与libRTMP 的接口不一样，会导致libRTMP编译不能通过。我这里安装的是openssl-1.0.1f。
1、下载地址：http://www.openssl.org/source/ 下一个新版本的OpenSSL，我下的版本是：openssl-1.0.1f
2、在下载的GZ目录中，用命令执行：tar -xvf openssl-1.0.1f.tar.gz
3、进入解压的目录：openssl-1.0.1f  [.......]#cd openssl-1.0.1f
4、[.....openssl-1.0.1f]# ./config --prefix=/usr/local/openssl
5[...../openssl-1.0.1f]# ./config -t
6[...../openssl-1.0.1f]# make depend
7[...../openssl-1.0.1f]# cd /usr/local
8/usr/local]# ln -s openssl ssl
9 [...../openssl-1.0.1f]#sudo make install
10在/etc/ld.so.conf文件的最后面，添加如下内容：
/usr/local/openssl/lib
11...]# ldconfig
12添加OPESSL的环境变量：
在etc／的profile的最后一行，添加：
export OPENSSL=/usr/local/openssl/bin
export PATH=$OPENSSL:$PATH:$HOME/bin
13退出命令界面，再从新登录。
14、以上OPENSSL就安装完毕，下面进行一些检查。
15依次如下执行：
[root@localhost /]# cd /usr/local
[root@localhost local]# ldd /usr/local/openssl/bin/openssl
会出现类似如下信息：
        linux-vdso.so.1 =>  (0x00007fff2116a000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f378e239000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f378de7c000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f378e44f000)
16查看路径
...]# which openssl
/usr/local/openssl/bin/openssl
17查看版本
...]# openssl version
OpenSSL 1.0.1f 6 Jan 2014


#定时任务
sudo crontab -e 
crontab -l
//Cron是Unix系统的一个配置定期任务的工具，用于定期或者以一定的时间间隔执行一些命令或者脚本；可执行的任务范围可以是每天夜里自动备份用户的home文件夹，也可以每个小时记录CPU的信息日志。
//crontab（cron table）命令用于编辑执行中的定期任务列表，并且操作是基于每个用户的，每一个用户（包括root用户）都拥有自己的crontab。
*/5 * * * * /usr/local/tomcat-6.0.41/tomcat_cardniu_stat/monitor.sh //每五分钟
0 0 * * *  /home/pi/backup.sh //每天
/etc/init.d/crond restart //重启服务
// service crond restart
service cron status
/etc/init.d/cron {start|stop|status|restart|reload|force-reload}.
*/4 * * * * /home/pi/project/python/foStart.sh
0 0 * * * /home/pi/project/python/foRestart.sh

其中排列意思为：
Bash
#    m    h    dom    mon    dow    user    command
#  分    时    日    月      周    用户    命令
#
#       m:表示分钟1～59 每分钟用*或者 */1表示
#       h:表示小时1～23（0表示0点）
#     dom:表示日期1～31
#     mon:表示月份1～12
#     dow:标识号星期0～6（0表示星期天）
#    user:表示执行命令的用户
# command:表示要执行的命令
#
#   * 代表任意数值
例程如下：
Bash
30 21 * * * /usr/local/etc/rc.d/lighttpd restart
#上面的例子表示每晚的21:30重启apache。
45 4 1,10,22 * * /usr/local/etc/rc.d/lighttpd restart
#上面的例子表示每月1、10、22日的4 : 45重启apache。
10 1 * * 6,0 /usr/local/etc/rc.d/lighttpd restart
#上面的例子表示每周六、周日的1 : 10重启apache。
0,30 18-23 * * * /usr/local/etc/rc.d/lighttpd restart
#上面的例子表示在每天18 : 00至23 : 00之间每隔30分钟重启apache。
0 23 * * 6 /usr/local/etc/rc.d/lighttpd restart
#上面的例子表示每星期六的11 : 00 pm重启apache。
* */1 * * * /usr/local/etc/rc.d/lighttpd restart
#每一小时重启apache
* 23-7/1 * * * /usr/local/etc/rc.d/lighttpd restart
#晚上11点到早上7点之间，每隔一小时重启apache
0 11 4 * mon-wed /usr/local/etc/rc.d/lighttpd restart
#每月的4号与每周一到周三的11点重启apache
0 4 1 jan * /usr/local/etc/rc.d/lighttpd restart
#一月一号的4点重启apache





