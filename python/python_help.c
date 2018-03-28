#python help
#python nginx opencv 环境安装



sudo killall -9 nginx 
sudo nginx




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
sudo pip install eventlet
sudo pip install flask

查找Python 安装路径： THIS 
>>> from distutils.sysconfig import get_python_lib
>>> print(get_python_lib())




--   Python 2:
--     Interpreter:     /usr/bin/python2.7 (ver 2.7.12)
--     Libraries:       /usr/lib/x86_64-linux-gnu/libpython2.7.so (ver 2.7.12)
--     numpy:           /home/walker/.local/lib/python2.7/site-packages/numpy/core/include (ver 1.13.3)
--     packages path:   lib/python2.7/dist-packages

//opencv安装
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








