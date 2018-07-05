#python help
#python nginx opencv 环境安装



sudo killall -9 nginx 
sudo nginx

//指定版本降级安装
sudo apt-get install libffi6=3.1-2+deb8u1

//nginx
sudo apt-get install nginx
vim /etc/nginx/nginx.conf //配置映射路径
Linux下1024以下端口号，需要root权限所启动的程序才能绑定监听


 
//安装python环境
sudo apt-get install pip
sudo pip install Tornado 
sudo pip install chardet
sudo pip install psutil
numpy//数学 矩阵
scipy//科学计算工具
sklearn//基本机器学习库 KNN-k临近 SVM-向量机 决策树
keras//深度学习库 高层神经网络 CNN-卷积神经网络 RNN-循环神经网络 DNN-深度神经网络 cpu/gpu
    tensorflowKeras//keras并不处理如张量乘法、卷积等底层操作。这些操作依赖于某种特定的、优化良好的张量操作库。Keras依赖于处理张量的库就称为“后端引擎”。Keras提供了三种后端引擎Theano/Tensorflow/CNTK，并将其函数统一封装，使得用户可以以同一个接口调用不同后端引擎的函数
    h5py
opencv//源码安装 cv2 knn 图形视觉库 图形处理
BeautifulSoup   //格式化html soup工具
//没有pip
wget "https://pypi.python.org/packages/source/p/pip/pip-1.5.4.tar.gz#md5=834b2904f92d46aaa333267fb1c922bb" --no-check-certificate
unzip 
python setup.py install
//缺少 setuptool
下载http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg
chmod +x
sudo ./xxxegg
https://github.com/miguelgrinberg/python-socketio/

sudo pip install python-socketio
sudo pip install socketIO-client 
sudo pip install -U socketIO-client
手动安装
https://files.pythonhosted.org/packages/12/d4/abeb2596c2f16276c66910362b27d04b8d2cf12a746dcccf1d00de3f691b/socketIO-client-0.7.2.tar.gz
//https://pypi.org/project/socketIO-client/
sudo pip install eventlet
sudo pip install flask
sudo pip install twisted //socket frame of python
// sudo apt-get install python-twisted
sudo pip install json2yaml==1.0.1 
// python推流rtmp 
sudo pip install python-librtmp
//pip安装失败解决方案
修改源方法：
linux: 修改 ~/.pip/pip.conf (没有就创建一个)， 内容如下：
[global]
index-url = http://pypi.mirrors.ustc.edu.cn/simple/

阿里云 http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣(douban) https://pypi.douban.com/simple/
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术  http://pypi.mirrors.ustc.edu.cn/simple/

pip升级
python -m pip install -U pip
查找Python 安装路径： THIS 
>>> from distutils.sysconfig import get_python_lib
>>> print(get_python_lib())



//nginx rtmp 依赖环境
wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.38.tar.gz
wget http://www.openssl.org/source/openssl-1.0.1c.tar.gz
wget http://www.zlib.net/zlib-1.2.11.tar.gz
cd nginx-1.10.1 
./configure --sbin-path=/usr/local/nginx/nginx --conf-path=/usr/local/nginx/nginx.conf --pid-path=/usr/local/nginx/nginx.pid --with-http_ssl_module --with-pcre=../pcre-8.38 --with-zlib=../zlib-1.2.11 --with-openssl=../openssl-1.0.1c --with-http_stub_status_module --add-module=../nginx-rtmp-module-master
makez
make install
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
--prefix                       #nginx安装目录，默认在/usr/local/nginx
--conf-path=/usr/local/nginx/nginx.conf  #nginx。配置路径名
--pid-path=/usr/local/nginx/nginx.pid    #pid问件位置，默认在logs目录
--lock-path                    #lock问件位置，默认在logs目录
--with-http_ssl_module         #开启HTTP SSL模块，以支持HTTPS请求。
--with-http_dav_module         #开启WebDAV扩展动作模块，可为文件和目录指定权限
--with-http_flv_module         #支持对FLV文件的拖动播放
--with-http_realip_module      #支持显示真实来源IP地址
--with-http_gzip_static_module #预压缩文件传前检查，防止文件被重复压缩
--with-http_stub_status_module #取得一些nginx的运行状态
--with-mail                     #允许POP3/IMAP4/SMTP代理模块
--with-mail_ssl_module          #允许POP3／IMAP／SMTP可以使用SSL／TLS
--with-pcre=../pcre-8.11        #注意是未安装的pcre路径
--with-zlib=../zlib-1.2.5       #注意是未安装的zlib路径
--with-debug                    #允许调试日志
--http-client-body-temp-path    #客户端请求临时文件路径
--http-proxy-temp-path          #设置http proxy临时文件路径
--http-fastcgi-temp-path        #设置http fastcgi临时文件路径
--http-uwsgi-temp-path=/usr/local/nginx/uwsgi #设置uwsgi 临时文件路径
--http-scgi-temp-path=/usr/local/nginx/scgi   #设置scgi 临时文件路径
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



--add-module=../nginx-rtmp-module-master



--   Python 2:
--     Interpreter:     /usr/bin/python2.7 (ver 2.7.12)
--     Libraries:       /usr/lib/x86_64-linux-gnu/libpython2.7.so (ver 2.7.12)
--     numpy:           /home/walker/.local/lib/python2.7/site-packages/numpy/core/include (ver 1.13.3)
--     packages path:   lib/python2.7/dist-packages

//python-rtmp
（一）openssl安装
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

（二）zlib安装
    安装的版本为zlib-1.2.11.tar.gz ,可直接安装
1 lcb@ubuntu:~/test/RTMP$ tar xvf zlib-1.2.11.tar.gz 
2 lcb@ubuntu:~/test/RTMP$ cd zlib-1.2.11/
3 lcb@ubuntu:~/test/RTMP/zlib-1.2.11$ sudo ./configure 
4 lcb@ubuntu:~/test/RTMP/zlib-1.2.11$ make
5 lcb@ubuntu:~/test/RTMP/zlib-1.2.11$ sudo make install

（三）libssl-dev 安装
    libssl-dev 的安装，可直接使用命令安装：
    sudo apt-get install libssl-dev

（四）编译libRTMP
1 添加openssl的头文件查找路径：在/etc/profile文件最后面添加上
C_INCLUDE_PATH=/usr/local/openssl/include/
export C_INCLUDE_PATH 
CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/local/openssl/include/
export CPLUS_INCLUDE_PATH
2 下载rtmpdump-2.3 可直接编译安装, rtmpdump主页： http://rtmpdump.mplayerhq.hu/
tar -xvf  rtmpdump-2.3.tgz
cd rtmpdump-2.3
make
make install

//opencv安装
//1.树莓派专用方式?
// 软件源更新
sudo apt-get update 
// 升级本地所有安装包，最新系统可以不升级，版本过高反而需要降级才能安装
sudo apt-get upgrade
// 升级树莓派固件，固件比较新或者是Ubuntu则不用执行
sudo rpi-update
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

sudo apt-get install libjpeg62-turbo-dev libtiff5-dev  libjasper-dev libpng12-dev 

//2.普通安装方式
{
//依赖
sudo apt-get install \ 
    libopencv-dev \ 
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
    libqt4-dev \ 
    libgtk2.0-dev \ 
    libfaac-dev \ 
    libmp3lame-dev \ 
    libopencore-amrnb-dev \ 
    libopencore-amrwb-dev \ 
    libtheora-dev \ 
    libvorbis-dev \ 
    libxvidcore-dev \ 
    x264 \ 
    v4l-utils \ 
    ffmpeg \ 
    gstreamer-plugins-base-devel \
    cmake \ 
    qt5-default \ 
    checkinstall

//cmake 编写makefile
 cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..

cmake -D CMAKE_BUILD_TYPE=RELEASE \
 -D CMAKE_INSTALL_PREFIX=/usr/local \
 -D INSTALL_C_EXAMPLES=ON \
 -D INSTALL_PYTHON_EXAMPLES=ON \
 -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
 -D BUILD_EXAMPLES=ON ..
  
-错误
- Found OpenEXR: /usr/lib/x86_64-linux-gnu/libIlmImf.so
-- Checking for module 'gtk+-3.0'
--   No package 'gtk+-3.0' found
-- Checking for module 'gstreamer-base-1.0'
--   No package 'gstreamer-base-1.0' found  


//失败 
-- Configuring incomplete, errors occurred!
See also "/home/walker/opencv-3.3.0/build/CMakeFiles/CMakeOutput.log".
See also "/home/walker/opencv-3.3.0/build/CMakeFiles/CMakeError.log".

//正常结果？？？？？？？？？？？？
-- Configuring done
-- Generating done 
-- Build files have been written to: /home/walker/opencv-3.3.0/build


//编译 make -jn 表示n个核心并发？
make -j2

//安装 
make install

//刷新链接库？        
ldconfig
//连接python加载模块so文件
su mv /usr/local/lib/python2.7/site-packages/cv2.so /usr/lib/python2.7/site-packages
或者 ln mv /usr/local/lib/python2.7/site-packages/cv2.so /usr/lib/python2.7/site-packages
或者 export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages


//测试
>>> import cv2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: libopencv_reg.so.3.3: cannot enable executable stack as shared object requires: Invalid argument
>>> quit()
//解决方案https://stackoverflow.com/questions/39136040/python3-4-error-cannot-enable-executable-stack-as-shared-object-requires-inva
sudo apt-get install execstack
sudo execstack -c /usr/local/lib/libopencv_*
    
import cv2
cv2.__version__
'3.3.0'
ok!

}








