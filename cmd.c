
dxdiag 查看direct 和 硬件设备信息 系统版本 windows10 专业版64(10.0, 版本 16299)


第一步：找到注册表的启动项位置：HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run主键
第二步：在另边点击右键：新建“字符串值”，取名“QQ”如下图：
第三步：找到你所要增加启动项的软件目录：
如我的QQ是目录是：D:\Program Files\Tencent\QQ\qq.exe
第三步：双击你刚新建军的"qq"字符串值项,即：
编辑字符串数值数据：将第三步找到的软件目录复制到下面图的“数值数据栏内” 
确定后，关闭注册表，OK，你的XP系统启动项设置成功了
P.S. 
1.Run键r
　　Run键是病毒最青睐的自启动之所，该键位置是[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run]和[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run]，其下的所有程序在每次启动登录时都会按顺序自动执行。
　　还有一个不被注意的Run键，位于注册表[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run]和[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run]，也要仔细查看。

　　2.RunOnce键
　　RunOnce位于[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce]和[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce]键，与Run不同的是，RunOnce下的程序仅会被自动执行一次。

　　3.RunServicesOnce键
　　RunServicesOnce键位于[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce]和[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce]下，其中的程序会在系统加载时自动启动执行一次

arp -a 输出所有ip？该命令显示和修改“地址解析协议 (ARP)”缓存中的项目。ARP 缓存中包含一个或多个表，它们用于存储 IP 地址及其经过解析的以太网或令牌环物理地址。 
ping -a ip	ping -a 将地址解析为计算机名。用户名
nbtstat -a ip 来获得更详细的信息，包括计算机的名称已经硬件Mac地址，这样不论他们怎么变化遁形，都逃不过你的法眼啦，赶紧试试吧。

ping 目标计算机名
nbtstat -a 目标计算机名（可以省去）
?////////////////////ip和用户名互转

runas /user:administrator "cmd /k"

netplwiz”打开“用户账户”面板

启动配置
msconfig


重置网络连接
netsh int ip reset
netsh winhttp reset proxy
ipconfig /flushdns
重置winsock
netsh winsock reset
1366X768
“开始”--输入“regedit”依次找到：
HKEY_LOCAL_MACHINE/SYSTEM/ControlSet001/Control/GraphicsDrivers/Configuration

然后右键点击Configuration，选择查找，输入Scaling，在右框内即可看到scaling，
右键scaling选择修改，将数值改为3即可。

"开始"-"运行"-"gpedit.msc"-"计算机配置"-"windows设置"-"安全设置"
端口开放 入站规则
-"软件设置策略",右击"软件设置策略"点"新建策略"-"其它规则"-右击"其它规则"-"新路径规则".把你要阻止的某些软件放在一个盘里面就OK了..

方法一：利用注册表
　　1、按下Win+R组合键，在运行命令中输入“regedit”回车。
　　2、在出现的注册表编辑器界面，依次展开
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet，点击选中Internet项目后，右侧窗口找到“EnableActiveProbing”值，双击打开编辑AWORD（32位）值对话框。
　　3、在编辑AWORD（32位）值对话框，将数值数据修改成“0（默认为1）”，完成后，点击确定保存即可，再次重启电脑，宽带连接成功后就不会再出现自动登陆的界面了！
　　方法二：利用本地组策略编辑器
　　原理是一样的，都是禁用Windows网络连接状态指示器活动测试。
　　1、按下Win+R组合键，在运行命令中输入“gpedit.msc”后回车（参考方法一）。
　　2、在本地组策略编辑器界面，依次展开计算机配置-》管理模板-》系统-》Internet通信管理，然后单击选中“Internet 通信设置”后，在右侧窗口找到并双击“关闭Windows网络连接状态指示器活动测试”。
　　3、在关闭Windows网络连接状态指示器活动测试对话框，点击选择左上角“已启用”，然后点击确定，退出设置界面即可。
　　以上就是Win8.1系统如何禁止连接宽带后自动打开微软网页的介绍了，使用这两个方法都能有效地防止微软网页自动打开
netstat -ano，列出所有端口的情况。在列表中我们观察被占用的端口
查看被占用端口对应的PID，：netstat -aon|findstr "49157"
输入tasklist|findstr "2720"，回车，查看是哪个进程或者程序占用了2720端口，结果是：svchost.exe
taskkill /f /t /im Tencentdl.exe。

Win+R，然后在弹出面板中输入“netplwiz”打开“用户账户”面板，接下来取消面板顶端的“要使用本计算机，用户必须输入用户名和密码”复选框并确定。这
cls

shutdown -h now 关闭系统(1) 
　　init 0 关闭系统(2) 
　　telinit 0 关闭系统(3) 
　　shutdown -h hours:minutes & 按预定时间关闭系统 
　　shutdown -c 取消按预定时间关闭系统 
　　shutdown -r now 重启(1) 
　　reboot 重启(2) 
　　logout 注销


cd /home 进入 '/ home' 目录' 
　　cd .. 返回上一级目录 
　　cd ../.. 返回上两级目录 
　　cd 进入个人的主目录 
　　cd ~user1 进入个人的主目录 
　　cd - 返回上次所在的目录 
　　pwd 显示工作路径 
　　ls 查看目录中的文件 
　　ls -F 查看目录中的文件 
　　ls -l 显示文件和目录的详细资料 
　　ls -a 显示隐藏文件 
　　ls *[0-9]* 显示包含数字的文件名和目录名 
　　tree 显示文件和目录由根目录开始的树形结构(1) 
　　lstree 显示文件和目录由根目录开始的树形结构(2) 
　　mkdir dir1 创建一个叫做 'dir1' 的目录' 
　　mkdir dir1 dir2 同时创建两个目录 
　　mkdir -p /tmp/dir1/dir2 创建一个目录树 
　　rm -f file1 删除一个叫做 'file1' 的文件' 
　　rmdir dir1 删除一个叫做 'dir1' 的目录' 
　　rm -rf dir1 删除一个叫做 'dir1' 的目录并同时删除其内容 
　　rm -rf dir1 dir2 同时删除两个目录及它们的内容 
　　mv dir1 new_dir 重命名/移动 一个目录 
　　cp file1 file2 复制一个文件 
　　cp dir/* . 复制一个目录下的所有文件到当前工作目录 
　　cp -a /tmp/dir1 . 复制一个目录到当前工作目录 
　　cp -a dir1 dir2 复制一个目录 
　　ln -s file1 lnk1 创建一个指向文件或目录的软链接 
　　ln file1 lnk1 创建一个指向文件或目录的物理链接 
　　touch -t 0712250000 file1 修改一个文件或目录的时间戳 - (YYMMDDhhmm)
文件搜索

find / -name file1 从 '/' 开始进入根文件系统搜索文件和目录 
　　find / -user user1 搜索属于用户 'user1' 的文件和目录 
　　find /home/user1 -name \*.bin 在目录 '/ home/user1' 中搜索带有'.bin' 结尾的文件 
　　find /usr/bin -type f -atime +100 搜索在过去100天内未被使用过的执行文件 
　　find /usr/bin -type f -mtime -10 搜索在10天内被创建或者修改过的文件 
　　find / -name \*.rpm -exec chmod 755 '{}' \; 搜索以 '.rpm' 结尾的文件并定义其权限 
　　find / -xdev -name \*.rpm 搜索以 '.rpm' 结尾的文件，忽略光驱、捷盘等可移动设备 
　　locate \*.ps 寻找以 '.ps' 结尾的文件 - 先运行 'updatedb' 命令 
　　whereis halt 显示一个二进制文件、源码或man的位置 
　　which halt 显示一个二进制文件或可执行文件的完整路径
文件系统

mount /dev/hda2 /mnt/hda2 挂载一个叫做hda2的盘 - 确定目录 '/ mnt/hda2' 已经存在 
　　umount /dev/hda2 卸载一个叫做hda2的盘 - 先从挂载点 '/ mnt/hda2' 退出 
　　fuser -km /mnt/hda2 当设备繁忙时强制卸载 
　　umount -n /mnt/hda2 运行卸载操作而不写入 /etc/mtab 文件- 当文件为只读或当磁盘写满时非常有用 
　　mount /dev/fd0 /mnt/floppy 挂载一个软盘 
　　mount /dev/cdrom /mnt/cdrom 挂载一个cdrom或dvdrom 
　　mount /dev/hdc /mnt/cdrecorder 挂载一个cdrw或dvdrom 
　　
　　mount -o loop file.iso /mnt/cdrom 挂载一个文件或ISO镜像文件 
　　mount -t vfat /dev/hda5 /mnt/hda5 挂载一个Windows FAT32文件系统 
　　mount /dev/sda1 /mnt/usbdisk 挂载一个usb 捷盘或闪存设备 
　　mount -t smbfs -o username=user,password=pass //WinClient/share /mnt/share 挂载一个网络共享
磁盘空间

df -h 显示已经挂载的分区列表 
　　ls -lSr |more 以尺寸大小排列文件和目录 
　　du -sh dir1 估算目录 'dir1' 已经使用的磁盘空间' 
　　du -sk * | sort -rn 以容量大小为依据依次显示文件和目录的大小 
　　rpm -q -a --qf '%10{SIZE}t%{NAME}n' | sort -k1,1n 以大小为依据依次显示已安装的rpm包所使用的空间 (fedora, redhat类系统) 
　　dpkg-query -W -f='${Installed-Size;10}t${Package}n' | sort -k1,1n 以大小为依据显示已安装的deb包所使用的 空间 (ubuntu, debian类系统)
2Windows命令

命令行（Command Processor）（CMD）是在OS / 2 ， Windows CE与Windows NT平台为基础的操作系统（包括Windows 2000，Windows XP，Windows Vista，Windows Server 2003，Windows 7， Windows 8 ，Windows 8.1 ，Windows 10）下的“MS-DOS 方式”。一般Windows 的各种版本都与其兼容，用户可以在Windows 系统下运行DOS命令，中文版Windows XP 中的命令提示符进一步提高了与DOS 下操作命令的兼容性，用户可以在命令提示符直接输入中文调用文件。命令行功能多于DOS。
命令信息
wmimgmt.msc 打开Windows管理体系结构（wmi)
wupdmgr Windows更新程序
wscriptWindows脚本宿主设置
write写字板
winmsd系统信息
wiaacmgr 扫描仪和照相机向导
winchatxp自带局域网聊天
mem.exe显示内存使用情况
msconfig.exe系统配置实用程序
mplayer2 简易widnows media player(媒体播放器）
mspaint画图板
mstsc远程桌面连接
mplayer2 媒体播放机
magnify放大镜实用程序
mmc 打开控制台
mobsync 同步命令
dxdiag 检查directx信息
drwtsn32 系统医生
devmgmt.msc设备管理器
dfrg.msc磁盘碎片整理程序
diskmgmt.msc磁盘管理实用程序
dcomcnfg 打开系统组件服务
ddeshare 打开dde共享设置
dvdplaydvd播放器
net stop messenger 停止信使服务
net start messenger 开始信使服务
notepad 打开记事本
nslookup 网络管理的工具向导
ntbackup 系统备份和还原
narrator屏幕“讲述人”
ntmsmgr.msc 移动存储管理器
ntmsoprq.msc 移动存储管理员操作请求
netstat -an （tc）命令检查接口
syncapp 创建一个公文包
sysedit系统配置编辑器
sigverif文件签名验证程序
sndrec32录音机
shrpubw 创建共享文件夹
secpol.msc 本地安全策略
syskey 系统加密，一旦加密就不能解开，保护Windows xp系统的双重密码
services.msc本地服务设置
sndvol32 音量控制程序
sfc.exe系统文件检查器
sfc /scannow windows文件保护 tsshutdn 60秒倒计时关机命令
tourstart xp简介（安装完成后出现的漫游xp程序）
taskmgr任务管理器
eventvwr事件查看器
eudcedit 造字程序
explorer 打开资源管理器
packager 对象包装程序
perfmon.msc计算机性能监测程序
progman 程序管理器
regedit注册表
rsop.msc组策略结果集
regedt32注册表编辑器
rononce -p15秒关机
regsvr32 /u *.dll 停止dll文件运行
regsvr32 /u zipfldr.dll 取消zip支持
cmd.execmd命令提示符
chkdsk.exechkdsk磁盘检查
certmgr.msc 证书管理实用程序
calc 启动计算器
charmap 启动字符映射表
cliconfg sql server客户端网络实用程序
clipbrd剪贴板查看器
conf 启动netmeeting
compmgmt.msc计算机管理
cleanmgr 垃圾整理
ciadv.msc 索引服务程序
osk 打开屏幕键盘
odbcad32 odbc数据源管理器
oobe/msoobe /a 检查xp是否激活
lusrmgr.msc 本机用户和组
logoff 注销命令
iexpress木马捆绑工具，系统自带
nslookup ip地址侦测器
fsmgmt.msc共享文件夹管理器
utilman辅助工具管理器
gpedit.msc组策略
Windows操作系统的常用运行命令
以下为Windows操作系统的常用运行命令，执行这些命令，就能打开系统对应的相关实用程序，如果大家能基本利用，就能检查并修复系统的最基本的故障，除注销，关闭系统命令外，其它所有命令，大家不妨一试！！
运行\输入CMD\输入对应的相关实用程序：
. 打开C:\Documents and Settings\XXX（当前登录Windows XP的用户名）
.. 打开Windows XP所在的盘符下的Documents and Settings文件夹
… 打开“我的电脑”选项。
accwiz.exe辅助工具向导
actmovie.exe直接显示安装工具
append.exe允许程序打开制定目录中的数据
arp.exe显示和更改计算机的IP与硬件物理地址的对应列表
at.exe 计划运行任务
atmadm.exeATM调用管理器统计
attrib.exe显示和更改文件和文件夹属性
autochk.exe检测修复文件系统（XP不可用）
autoconv.exe在启动过程中自动转化系统（XP不可用）
autofmt.exe 在启动过程中格式化进程（XP不可用）
autolfn.exe使用长文件名格式（XP不可用）
arp.exe 显示和更改计算机的IP与硬件物理地址的对应
calc.exe计算器
Bootvrfy.exe 通报启动成功
cacls.exe显示和编辑ACL
cdplayer.exeCD播放器
change.exe与终端服务器相关的查询（XP不可用）
charmap.exe字符映射表
chglogon.exe 启动或停用会话记录（XP不可用）
chgport.exe 改变端口（终端服务）（XP不可用）
chgusr.exe 改变用户（终端服务）（XP不可用）
chkdsk.exe磁盘检测程序
chkntfs.exe NTFS磁盘检测程序
cidaemon.exe组成Ci文档服务
cipher.exe在NTFS上显示或改变加密的文件或目录
cisvc.exe打开索引内容
ckcnv.exe 变换Cookie
cleanmgr.exe磁盘清理
cliconfg.exeSQL客户网络工具
clipbrd.exe剪贴簿查看器
clipsrv.exe运行Clipboard服务
clspack.exe 建立系统文件列表清单
cluster.exe 显示域的集群(XP不可用）
cmd.exe 进2000\XP DOS
cmdl32.exe自动下载连接管理
cmmgr32.exe 连接管理器
cmmon32.exe 连接管理器监视
cmstp.exe 连接管理器配置文件安装程序
comclust.exe 集群
comp.exe 比较两个文件和文件集的内容
conf 启动netmeeting聊天工具
control userpasswords2 XP密码管理.
compmgmt.msc 计算机管理
cprofile.exe 转换显示模式（XP不可用）
开始，运行，输入CMD\输入net config workstation计算机名\完整的计算机名\用户名
工作站处于活动状态（即网络描述）\软件版本（即软件版本号）\工作站域 工作站域的DNS 名称
登录域 \COM 打开时间超时（秒）\COM 发送量（字节）\COM 发送超时（msec)
CMD\输入net config workstation 更改可配置工作站服务设置。
CMD\输入net config server 可以显示不能配置的下服务器计算机名\服务器注释 \服务器版本（即软件版本号）
服务器处于活动状态（即网络描述） \服务器处于隐藏状态（即/hidden 设置）
最大登录用户数（即可使用服务器共享资源的最大用户数）
每个会话打开文件的最大数（即用户可在一个会话中打开服务器文件的最大数）
空闲会话时间（最小值）
chkdsk.exe磁盘检查.
Chkdsk /r 2000命令控制台中的Chkdsk /r命令检查修复系统文件
cleanmgr 垃圾整理
Clipbrd 剪贴板查看器
C:boot.ini打开启动菜单
compact.exe 显示或改变NTFS分区上文件的压缩状态
conime.exeIME控制台
control.exe控制面板
convert.exe NTFS 转换文件系统到NTFS
convlog.exe 转换ⅡS日志文件格式到NCSA格式
cprofile.exe 转换显示模式
cscript.exe较本宿主版本
csrss.exe客户服务器Runtime进程（XP不可用）
csvde.exe 格式转换程序（XP不可用）
dcpromo活动目录安装（XP不可用）
drwtsn32 系统医生
diskmgmt.msc磁盘管理器（和PowerQuest PartitionMagic 8.0)
dvdplay DVD 播放器
devmgmt.msc设备管理器（检查电脑硬件，驱动）
dxdiag 检查DirectX信息
dcomcnfg.exeDCOM配置属性（控制台根目录）
dcpromo.exe 安装向导（XP不可用）
ddeshare.exe DDE共享
debug.exe 检查DEBUG
dfrgfat.exeFAT分区磁盘碎片整理程序
dfrgntfs.exeNTFS分区磁盘碎片整理程序(XP不可用）
dfs_cmd_.exe 配置DFS树（XP不可用）
dfsinit.exe分布式文件系统初始化（XP不可用）
dfssvc.exe分布式文件系统服务器（XP不可用）
diantz.exe制作CAB文件
diskperf.exe磁盘性能计数器
dmremote.exe磁盘管理服务的一部分（XP不可用）
doskey.exe命令行创建宏
dosx.exe DOS扩展
dplaysvr.exe 直接运行帮助（XP不可用）
drwatson.exe华生医生错误检测
drwtsn32.exe华生医生显示和配置管理
dvdplay.exeDVD播放
dxdiag.exeDirect-X诊断工具
edlin.exe命令行的文本编辑
esentutl.exe MS数据库工具
eudcedit.exe造字程序
eventvwr.exe事件查看器
exe2bin.exe 转换EXE文件到二进制
expand.exe解压缩
extrac32.exe 解CAB工具
fsmgmt.msc 共享文件夹
fastopen.exe 快速访问在内存中的硬盘文件
faxcover.exe 传真封面编辑
faxqueue.exe 显示传真队列
faxsend.exe 发送传真向导
faxsvc.exe启动传真服务
fc.exe比较两个文件的不同
find.exe查找文件中的文本行
findstr.exe 查找文件中的行
finger.exe 一个用户并显示出统计结果
fixmapi.exe 修复MAPI文件
flattemp.exe 允许或者禁用临时文件目录（XP不可用）
fontview.exe 显示字体文件中的字体
forcedos.exe 强制文件在DOS模式下运行
ftp.exeFTP下载
gpedit.msc 组策略
gdi.exe 图形界面驱动
grpconv.exe转换程序管理员组
hostname.exe显示机器的Hostname
Internat输入法图标
iexpress 木马捆绑工具，系统自带
ieshwiz.exe自定义文件夹向导
iexpress.exeiexpress安装包
iisreset.exe 重启ⅡS服务（未安装ⅡS，不可用）
internat.exe键盘语言指示器（XP不可用）
ipconfig.exe查看IP配置
ipsecmon.exeIP安全监视器
ipxroute.exe IPX路由和源路由控制程序
irftp.exe无线连接
ismserv.exe安装或者删除Service Control Manager中的服务
jdbgmgr.exe Java4的调试器
jetconv.exe 转换Jet Engine数据库（XP不可用）
jetpack.exe 压缩Jet数据库（XP不可用）
jview.exeJava的命令行装载者
label.exe改变驱动器的卷标
lcwiz.exe 许可证向导（XP不可用）
ldifde.exe LDIF目录交换命令行管理（XP不可用）
licmgr.exe终端服务许可协议管理（XP不可用）
lights.exe显示连接状况（XP不可用）
llsmgr.exe Windows 2000 许可协议管理（XP不可用）
llssrv.exe启动许可协议服务器（XP不可用）
locator.exeRPC Locator 远程定位
lodctr.exe 调用性能计数
logoff.exe注销当前用户
lpq.exe显示远端的LPD打印队列的状态，显示被送到基于Unix的服务器的打印任务
lpr.exe 用于Unix客户打印机将打印任务发送给连接了打印设备的NT的打印机服务器。
lsass.exe 运行LSA和Server的DLL
lserver.exe指定默认Server新的DNS域（XP不可用）
lusrmgr.msc 本地账户管理
mmc 控制台
mplayer2 播放器
macfile.exe 管理MACFILES (XP不可用）
magnify.exe放大镜
makecab.exe 制作CAB文件
mem.exe显示内存状态
migpwd.exe迁移密码
mmc.exe控制台
mnmsrvc.exe远程桌面共享
mobsync.exe同步目录管理器
mountvol.exe 创建、删除或列出卷的装入点。
mplay32.exe Media Player媒体播放器
mpnotify.exe 通知应用程序
mqbkup.exe 信息队列备份和恢复工具
mqmig.exe MSMQ Migration Utility 信息队列迁移工具
mrinfo.exe使用SNMP多点传送路由
mscdexnt.exe 安装MSCD
msdtc.exe动态事务处理控制台
msg.exe 发送消息到本地或远程客户
mshta.exeHTML应用程序主机
msiexec.exe开始Windows安装程序
mspaint.exe打开画图板
mstask.exe任务计划表程序
mstinit.exe任务计划表安装
Msconfig.exe系统配置实用程序（配置启动选项，服务项等）
mem.exe 显示内存使用情况
mspaint 画图板
Net Stop Messenger 停止信使服务
Net Start Messenger 恢复信使服务
nslookup 网络管理的工具
Nslookup IP地址侦测器
ntbackup 系统备份和还原
nbtstat.exe 使用NBT（TCP/IP 上的NetBIOS）显示协议统计和当前 TCP/IP 连接。
nddeapir.exeNDDE API服务器端
netsh.exe用于配置和监控Windows 2000命令行脚本接口（XP不可用）
netstat.exe显示协议统计和当前的TCP/IP 网络连接。
nlsfunc.exe 加载特定国家的信息。Windows 2000 和MS-DOS子系统不使用该命令接受该命令只是为了与MS-DOS 文件兼容。
notepad.exe打开记事本
nslookup.exe该诊断工具显示来自域名系统(DNS)名称服务器的信息。
ntbackup.exe备份和故障修复工具
ntfrs.exeNT文件复制服务（XP不可用）
ntvdm.exe模拟16位Windows环境
nw16.exe NetWare转向器
nwscript.exe 运行Netware脚本
odbcad32.exe32位ODBC数据源管理（驱动程序管理)
odbcconf.exe命令行配置ODBC驱动和数据源
packager.exe 对象包装程序
pathping.exe包含Ping和Tracert的程序
pentnt.exe 检查Pentium的浮点错误
perfmon.exe系统性能监视器
ping.exe 验证与远程计算机的连接
posix.exe 用于兼容Unix
print.exe 打印文本文件或显示打印队列的内容。
progman.exe程序管理器
psxss.exePosix子系统应用程序
qappsrv.exe 在网络上显示终端服务器可用的程序
qprocess.exe 在本地或远程显示进程的信息（需终端服务）
query.exe 查询进程和对话（XP不可用）
quser.exe 显示用户登陆的信息（需终端服务）
qwinsta.exe 显示终端服务的信息
rononce -p 15秒关机
rasAdmin远程访问服务.
regedit.exe 注册表编辑器
rasadmin.exe 启动远程访问服务(XP不可用）
rasautou.exe建立一个RAS连接
rasdial.exe 宽带，拨号连接
ras.exe运行RAS连接（XP不可用）
rcp.exe 计算机和运行远程外壳端口监控程序rshd 的系统之间复制文件
rdpclip.exe终端和本地复制和粘贴文件
recover.exe 从坏的或有缺陷的磁盘中恢复可读取的信息。
redir.exe 运行重定向服务
regedt32.exe32位注册服务
regini.exe 用脚本修改注册许可
regwiz.exe 注册向导
replace.exe 用源目录中的同名文件替换目标目录中的文件。
rexec.exe rexec命令在执行指定命令前，验证远程计算机上的用户名，只有安装了TCP/IP 协议后才可以使用该命令。
risetup.exe 运行远程安装向导服务（XP不可用）
route.exe 控制网络路由表
rsh.exe 在运行RSH 服务的远程计算机上运行命令
rsnotify.exe 远程存储通知回显
runas.exe 允许用户用其他权限运行指定的工具和程序
rundll32.exe启动32位DLL程序
rwinsta.exe 重置会话子系统硬件和软件到最初的值
Sndvol32 音量控制程序
sfc.exe 或CMD\ sfc.exe 回车系统文件检查器
services.msc 网络连接服务
syskey 系统加密，（一旦加密就不能解开，保护windows xp系统的双重密码wupdmgr WINDOWS UPDATE)
SCANREG/RESTORE命令恢复最近的注册表
secedit.exe 自动化安全性配置管理
services.exe 控制所有服务
sethc.exe设置高对比
setver.exe 设置MS-DOS 子系统向程序报告的MS-DOS 版本号
sfc.exe 系统文件检查
shadow.exe 监控另外一台中端服务器会话
shrpubw.exe 建立和共享文件夹
sigverif.exe 文件签名验证
smlogsvc.exe性能日志和警报（XP不可用）
sndrec32.exe录音机
sndvol32.exe显示声音控制信息
snmp.exe简单网络管理协议(XP不可用）
snmptrap.exeSNMP工具（XP不可用）
srvmgr.exe 服务器管理器（XP不可用）
subst.exe 将路径与驱动器盘符关联
sysedit.exe系统配置编辑器
syskey.exeNT账号数据库加密工具
sysocmgr.exe > Windows 安装程序
systray.exe在低权限运行systray
taskmgr 任务管理器
tasklist /svc(CMD）了解每个SVCHOST进程到底提供了多少系统服务（2000\98不可用）
tlist -S(CMD) 了解每个SVCHOST进程到底提供了多少系统服务（
taskman.exe 任务管理器（XP不可用）
taskmgr.exe任务管理器
tcmsetup.exe电话服务客户安装
tcpsvcs.exeTCP服务
termsrv.exe终端服务
tftp.exe 将文件传输到正在运行TFTP 服务的远程计算机或从正在运行TFTP 服务的远程计算机传输文件
themes.exe桌面主题(XP不可用）
tlntadmn.exeAdministrator Telnet服务管理
tlntsess.exe显示当前的Telnet会话
tlntsvr.exe开始Telnet服务
tracert.exe诊断实用程序将包含不同生存时间（TTL) 值的Internet 控制消息协议（ICMP)回显数据包发送到目标，以决定到达目标采用的路由
tsadmin.exe Administrator 终端服务管理器（XP不可用）
tscon.exe 粘贴用户会话到终端对话
tsdiscon.exe断开终端服务的用户
tskill.exe 杀掉终端服务
tsprof.exe 用终端服务得出查询结果
tsshutdn.exe关闭系统
unlodctr.exe 性能监视器的一部分
upg351db.exe 升级Jet数据库（XP不可用）
ups.exeUPS service UPS服务
user.exe Windows核心服务
userinit.exe 打开我的文档
usrmgr.exe 域用户管理器
utilman.exe指定2000启动时自动打开那台机器
vwipxspx.exe调用IPX/SPXVDM
w32tm.exe时间服务器
wextract.exe 解压缩Windows文件
winchat.exe 打开Windows聊天工具
winhlp32.exe运行帮助系统
winmsd.exe 查看系统信息
winver.exe 显示Windows版本
wizmgr.exe Windows管理向导（XP不可用）
wjview.exeJava命令行调用Java
write.exe打开写字板
wscript.exe脚本工具
wupdmgr.exeWindows update 运行Windows update升级向导
winver 检查Windows版本
用命令行解决问题
有趣的是，在CMD中输入“telnet towel.blinkenlights.nl”，运行后是一段字母版的《星球大战》微电影。
系统修复

开始，运行，输入Msconfig系统配置实用工具配置启动选项，包括config.sys、autoexec.bat、win.ini、system.ini和注册表及程序菜单中的启动项。并可设置是否故障启动。
开始，运行，输入Regedit 注册表修改工具注册表编辑器，如果没有把握不要随意修改注册表！
开始，运行，输入Regsvr32 dll注册工具当提示找不到dll文件时，可用此来注册该动态连接库。
开始，运行，输入Regwiz 注册向导用于注册。校验系统文件，并可恢复系统文件。
如果启动时出现类似*.vxd文件错误，可用此恢复该vxd文件。
开始，运行，输入ipconfig可查看本主机IP地址
开始，运行，输入Scandskw磁盘扫描程序，用于扫描修复磁盘。如果磁盘或文件出现错误，可用来初步修复。
开始，运行，输入DxDiag DirectX诊断工具可用于检测DirectX运行是否正常。
开始，运行，输入NETSCAPE
命令键

ESC：清除当前命令行；
F7：显示命令历史记录，以图形列表窗的形式给出所有曾经输入的命令，并可用上下箭头键选择再次执行该命令。
F8：搜索命令的历史记录，循环显示所有曾经输入的命令，直到按下回车键为止；
F9：按编号选择命令，以图形对话框方式要求您输入命令所对应的编号（从0开始），并将该命令显示在屏幕上
Ctrl+H：删除光标左边的一个字符；
Ctrl+C Ctrl+Break，强行中止命令执行
Ctrl+M：表示回车确认键；
Alt+F7：清除所有曾经输入的命令历史记录
Alt+PrintScreen：截取屏幕上当前命令窗里的内容。
高级应用

病毒破坏了系统文件，请使用杀毒软件查杀病毒，然后利用Windows 2000提供的“命令控制台”中的Chkdsk /r命令检查修复系统文件即可。
按F8进入带命令行的安全模式模式，运行SCANREG/RESTORE命令恢复最近的注册表
按F8进入安全模式，在运行里输入SFC，系统文件检查
netstat -ano 看端口
命令提示符被禁用的解决办法
1.点击开始--运行--gpedit.msc
⒉在打开的组策略中点击--用户配置---管理模板---系统
⒊在右侧窗口中双击打开“阻止访问命令提示符”属性，在打开的窗口中，选“已启用” 就是禁用 “已禁用”就是启用 或者可以这样在记事本输入以下代码并另存为解除。reg（记得文件类型选为所有文件），打开就行了Windows Registry Editor Version 5.00 [HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\system] “DisableCMD”=- 方法2 新建（或者打开）一个记事本文件，输入：start cmd.exe 然后另存为bat为后缀的，文件名可以随便取，但是后缀名一定要为bat。双击bat批处理文件，运行的效果是打开C盘。start命令相当于“运行”，也可以输入：start command，而这个start其实就是个dos命令，批处理文件其实可以简单地理解成可以自动运行dos命令的文件.[1] 
3CMD命令提示符大全

calc-----------启动计算器 [2] 
chkdsk.exe-----Chkdsk磁盘检查
compmgmt.msc---计算机管理 conf-----------启动 netmeeting
control userpasswords2-----User Account 权限设置
devmgmt.msc--- 设备管理器
diskmgmt.msc---磁盘管理实用程序
dfrg.msc-------磁盘碎片整理程序
drwtsn32------ 系统医生
dvdplay--------启动Media Player
dxdiag-----------DirectX Diagnostic Tool gpedit.msc-------组策略编辑器
gpupdate /target:computer /force 强制刷新组策略
eventvwr.exe-----事件查看器
explorer-------打开资源管理器
logoff---------注销命令
lusrmgr.msc----本机用户和组 msinfo32---------系统信息
msconfig---------系统配置实用程序
net start (servicename)----启动该服务
net stop (servicename)-----停止该服务
notepad--------打开记事本
nusrmgr.cpl-------同control userpasswords，打开用户帐户控制面板
Nslookup-------IP地址侦测器
oobe/msoobe /a----检查XP是否激活
perfmon.msc----计算机性能监测程序
progman--------程序管理器
regedit----------注册表编辑器
regedt32-------注册表编辑器
route print------查看路由表
rononce -p ----15秒关机
rsop.msc-------组策略结果集
rundll32.exe
rundll32.exe %Systemroot%System32shimgvw.dll,ImageView_Fullscreen----启动一个空白的Windows 图片和传真查看器
刚接触电脑的时候是从DOS系统开始，DOS时代根本就没有Windows这样的视窗操作界面，只有一个黑漆漆的窗口，让你输入命令。所以学DOS系统操作，命令提示符是不可或缺的。笔者可以告诉大家，大多数的程序员牛人或计算机专家在DOS系统下的操作是非常了得的，所以菜鸟要想成为计算机高手，DOS命令是非学不可。
直到今天的Windows系统，还是离不开DOS命令的操作。学习DOS系统操作，首先了解命令提示符。先了解每个命令提示符的作用，然后才能够灵活运用。
下面是笔者在某个论坛收集整理的命令提示符大全，希望对菜鸟们有所帮助。
winver---------检查Windows版本
wmimgmt.msc----打开windows管理体系结构(WMI)
wupdmgr--------windows更新程序
wscript--------windows脚本宿主设置 write----------写字板 winmsd---------系统信息
wiaacmgr-------扫描仪和照相机向导 winchat--------XP自带局域网聊天
mem.exe--------显示内存使用情况 Msconfig.exe---系统配置实用程序
mplayer2-------简易widnows media player mspaint--------画图板
mstsc----------远程桌面连接 mplayer2-------媒体播放机 magnify--------放大镜实用程序 mmc------------打开控制台 mobsync--------同步命令
dxdiag---------检查DirectX信息 drwtsn32------ 系统医生 devmgmt.msc--- 设备管理器 dfrg.msc-------磁盘碎片整理程序 diskmgmt.msc---磁盘管理实用程序
dcomcnfg-------打开系统组件服务 ddeshare-------打开DDE共享设置 dvdplay--------DVD播放器 net stop messenger-----停止信使服务 net start messenger----开始信使服务 notepad--------打开记事本
nslookup-------网络管理的工具向导 ntbackup-------系统备份和还原 narrator-------屏幕“讲述人”
ntmsmgr.msc----移动存储管理器
ntmsoprq.msc---移动存储管理员操作请求 netstat -an----(TC)命令检查接口
syncapp--------创建一个公文包 sysedit--------系统配置编辑器 sigverif-------文件签名验证程序 sndrec32-------录音机
shrpubw--------创建共享文件夹 secpol.msc-----本地安全策略
syskey---------系统加密，一旦加密就不能解开，保护windows xp系统的双重密码 services.msc---本地服务设置 Sndvol32-------音量控制程序 sfc.exe--------系统文件检查器
sfc /scannow---windows文件保护
tsshutdn-------60秒倒计时关机命令
tourstart------xp简介（安装完成后出现的漫游xp程序） taskmgr--------任务管理器 eventvwr-------事件查看器 eudcedit-------造字程序
explorer-------打开资源管理器 packager-------对象包装程序
perfmon.msc----计算机性能监测程序 progman--------程序管理器 regedit.exe----注册表
rsop.msc-------组策略结果集 regedt32-------注册表编辑器 rononce -p ----15秒关机
cmd.exe--------CMD命令提示符 chkdsk.exe-----Chkdsk磁盘检查 certmgr.msc----证书管理实用程序 calc-----------启动计算器
charmap--------启动字符映射表
cliconfg-------SQL SERVER 客户端网络实用程序 Clipbrd--------剪贴板查看器 conf-----------启动netmeeting compmgmt.msc---计算机管理 cleanmgr-------垃圾整理 ciadv.msc------索引服务程序 osk------------打开屏幕键盘
odbcad32-------ODBC数据源管理器 oobe/msoobe /a----检查XP是否激活 lusrmgr.msc----本机用户和组
logoff---------注销命令
iexpress-------木马捆绑工具，系统自带 Nslookup-------IP地址侦测器 fsmgmt.msc-----共享文件夹管理器 utilman--------辅助工具管理器
gpedit.msc-----组策略
4Windows

cd 改变当前目录
dir 显示文件列表
diskcopy 复制软盘
format 格式化磁盘
md 建立子目录
type 显示文件内容
rd 删除目录
ren 改变文件名
……
cls 清屏
正在执行命令的命令提示符
正在执行命令的命令提示符
〔适用场合〕 屏幕上太乱了，或是屏幕上出现乱码了，清除屏幕上显示内容但不影响电脑内部任何信息
〔用法〕 cls+回车
move 移动文件，改目录名
〔适用场合〕 移动文件到别的目录
〔用 法〕 move 文件名 目录[\文件] 移动文件至新目录下
move 目录 目录名 改目录名
〔例 子〕 c:\>move c:\autoexec.bat c:\old
移动autoexec.bat文件至old目录下
c:\>move c:\config.sys c:\old
移动config.sys文件至old目录下
more 分屏显示
〔适用场合〕 当输出很多一屏显示不下时采用，几乎适合所有命令，尤其是type等命令时很有用。使用more时磁盘不能有写保护，也不适合光驱。
〔用法〕 命令 | more 分屏显示文件内容
more < [文件名] 分屏显示文件内容
〔例 子〕C:\>type msdos.w40 | more
xcopy 加强版复制
〔适用场合〕 在进行连同子目录一起拷贝时很有用，在拷贝大量文件时比COPY命令要快得多
〔用 法〕 xcopy [文件名] [目录] 将指定文件拷贝到指定目录
xcopy [源目录] [目的目录] 将源目录连子目录拷到目的目录下
xcopy *.* [目录] /s 将文件与非空子目录拷贝到指定目录
其它常用参数还有：v 拷贝后校验，会影响速度
e 与s 相似，但即使子目录是空的也会拷贝
帮助

〔适用场合〕 当想具体了解DOS命令的使用方法时使用
〔用 法〕 help 提供所有DOS命令帮助
help （+DOS命令）提供有关（DOS）命令的帮助
如果你只大致记得某个命令，可以在提示符后直接输入help命令，然后将出现下面的画面：
attrib 设置文件属性
〔适用场合〕想对文件做较特殊的处理时
〔用法〕 attrib 显示所有文件的属性
attrib +r或-r [文件名] 设置文件属性是否为只读
attrib +h或-h [文件名] 设置文件属性是否隐含
attrib +s或-s [文件名] 设置文件属性是否为系统文件
attrib +a或-a [文件名] 设置文件属性是否为归档文件
attrib /s 设置包括子目录的文件在内的文件属性
〔例 子〕C:\TEST>attrib +r wina20.386
C:\>attrib +h *.* /s 隐含所有文件
date 显示及修改日期
〔适用场合〕 想知道或修改时间和日期
〔用 法〕 date 显示和改变当前日期
〔例 子〕C:\>date 09-20-1996 将日期改为1996年9月20日
C:\>date
Current date is Tue 08-20-1996
Enter new date (mm-dd-yy):09-20-1996
按月-日-年的顺序修改当前日期直接按回车键忽略修改日期
设置卷标

〔适用场合〕 用来为磁盘做个标记
〔用 法〕 label 显示磁盘卷标
label [盘符] [卷标名] 设定指定盘的卷标
〔例 子〕C:\>label
Volume in drive C is WANG
Volume Serial Number is 2116-1DD0
volume label （11 characters,Enter for none)?
可以输入卷标，直接回车后
Delete current volume label (Y/N)?
按y删除旧卷标，按n不更改
碎片整理

〔适用场合〕磁盘读写次数很多，或磁盘使用时间很长了，可能需要使用这条命令整理磁盘。磁盘碎片并不是指磁盘坏了，而只是由于多次的拷贝和删除文件后，磁盘使用会很不连贯，致使速度变慢。
〔用 法〕1. C:\>defrag
⒉ 选择要整理的磁盘
⒊ 电脑分析磁盘状况，然后告诉我们磁盘有多少需整理。按Esc键
⒋ 选择Optimization Method(磁盘优化方法），选择"全部优化"或"仅优化文件"
⒌ 选择Begin Optimization 开始整理
⒍ 整理完后，按回车键
⒎ 按Esc退出。
调用建立

〔适用场合〕 经常需要输入重复的命令时，有非常大的用处
〔用 法〕 doskey
将doskey驻留内存，开辟出缓冲区，以后输入的命令都将保存在缓冲区中，可以随时调用
doskey [宏命令名]=[命令名]
将宏命令定义为命令，以后输入宏命令，电脑就会执行相应的命令
doskey /reinstall 重新安装doskey
doskey /bufsize= 设置缓冲区的大小
doskey /macros 显示所有doskey宏
doskey /history显示内存中所有命令
doskey /insert|overstrike 设置新键入的字符是否覆盖旧的字符
〔例 子〕C:\>DOSKEY
C:\>dir
C:\>copy C:\temp\*.* a:
C:\>del c:\temp\*.*
C:\>copy b:\*.* c:\temp
上述四条命令都已被保存，用光标控制键的上下可以依次选择使用或修改,也可以用F7键列出保存的所有命令
C:\>doskey di=dir/w/p 定义di为宏命令，意思是执行dir/w/p


cmd命令大全（第一部分）
　　winver---------检查Windows版本 
　　wmimgmt.msc----打开windows管理体系结构(WMI) 
　　wupdmgr--------windows更新程序 
　　wscript--------windows脚本宿主设置 
　　write----------写字板 
　　winmsd---------系统信息 
　　wiaacmgr-------扫描仪和照相机向导 
　　winchat--------XP自带局域网聊天
cmd命令大全（第二部分）
　　mem.exe--------显示内存使用情况 
　　Msconfig.exe---系统配置实用程序 
　　mplayer2-------简易widnows media player 
　　mspaint--------画图板 
　　mstsc----------远程桌面连接 
　　mplayer2-------媒体播放机 
　　magnify--------放大镜实用程序 
　　mmc------------打开控制台 
　　mobsync--------同步命令
cmd命令大全（第三部分）
　　dxdiag---------检查DirectX信息 
　　drwtsn32------ 系统医生 
　　devmgmt.msc--- 设备管理器 
　　dfrg.msc-------磁盘碎片整理程序 
　　diskmgmt.msc---磁盘管理实用程序 
　　dcomcnfg-------打开系统组件服务 
　　ddeshare-------打开DDE共享设置 
　　dvdplay--------DVD播放器
cmd命令大全（第四部分）
　　net stop messenger-----停止信使服务 
　　net start messenger----开始信使服务 
　　notepad--------打开记事本 
　　nslookup-------网络管理的工具向导 
　　ntbackup-------系统备份和还原 
　　narrator-------屏幕“讲述人” 
　　ntmsmgr.msc----移动存储管理器 
　　ntmsoprq.msc---移动存储管理员操作请求 
　　netstat -an----(TC)命令检查接口
cmd命令大全（第五部分）
　　syncapp--------创建一个公文包 
　　sysedit--------系统配置编辑器 
　　sigverif-------文件签名验证程序 
　　sndrec32-------录音机 
　　shrpubw--------创建共享文件夹 
　　secpol.m转载自电脑十万个为什么http://www.qq880.com，请保留此标记sc-----本地安全策略 
　　syskey---------系统加密，一旦加密就不能解开，保护windows xp系统的双重密码 
　　services.msc---本地服务设置 
　　Sndvol32-------音量控制程序 
　　sfc.exe--------系统文件检查器 
　　sfc /scannow---windows文件保护
cmd命令大全（第六部分）
　　tsshutdn-------60秒倒计时关机命令 
　　tourstart------xp简介（安装完成后出现的漫游xp程序） 
　　taskmgr--------任务管理器 
　　eventvwr-------事件查看器 
　　eudcedit-------造字程序 
　　explorer-------打开资源管理器 
　　packager-------对象包装程序 
　　perfmon.msc----计算机性能监测程序 
　　progman--------程序管理器 
　　regedit.exe----注册表 
　　rsop.msc-------组策略结果集 
　　regedt32-------注册表编辑器 
　　rononce -p ----15秒关机 
　　regsvr32 /u *.dll----停止dll文件运行 
　　regsvr32 /u zipfldr.dll------取消ZIP支持
cmd命令大全（第七部分）
　　cmd.exe--------CMD命令提示符 
　　chkdsk.exe-----Chkdsk磁盘检查 
　　certmgr.msc----证书管理实用程序 
　　calc-----------启动计算器 
　　charmap--------启动字符映射表 
　　cliconfg-------SQL SERVER 客户端网络实用程序 
　　Clipbrd--------剪贴板查看器 
　　conf-----------启动netmeeting 
　　compmgmt.msc---计算机管理 
　　cleanmgr-------垃圾整理 
　　ciadv.msc------索引服务程序 
　　osk------------打开屏幕键盘 
　　odbcad32-------ODBC数据源管理器 
　　oobe/msoobe /a----检查XP是否激活 
　　lusrmgr.msc----本机用户和组 
　　logoff---------注销命令 
　　iexpress-------木马捆绑工具，系统自带 
　　Nslookup-------IP地址侦测器 
　　fsmgmt.msc-----共享文件夹管理器 
　　utilman--------辅助工具管理器 
　　gpedit.msc-----组策略











