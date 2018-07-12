::grunt tool  s 

::npm install grunt-cli
::npm install grunt 
::grunt install
::grunt

E:
cd workspace\echat_desktop
::覆盖配置文件为压缩需要的文件
copy coverage\config-tar.js app\config.js /Y
::压缩
grunt
::还原配置文件为自启动node需要的文件
copy coverage\config-node.js app\config.js /Y

