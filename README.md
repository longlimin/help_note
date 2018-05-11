# help_note
这是在下的学习旅途中所涉及到的 脚本类的各种语言(cmd,shell,python...) 各种帮助文档(正则,wireshark,nginx,makefile,git,gcc,ffmpeg,opencv,mysql,oracle,redis...) 及demo案例以及工具(个人项目git同步,差异制作补丁,cmd启动常用软件...)

# 项目路径结构
    

## cmd
把该路径添入到windows环境变量path中，便可以根据该路径下的脚本名快捷调用bat
* ss.bat
    * windows开机后，使用该脚本快速一口气启动常用的全部软件，就不用再到处点点点了（虽然也可设置软件开机启动的说，但是个人比较排斥启动项）
* ls.bat
    * 实际上是调用的dir，因为习惯了ls ll，cmd环境下没有很难受
* ...
## shell
* do
    * 各种do_*.sh文件的启动入口，其实因为老是./*还要写个sh后缀，比较懒，所以没后缀
* do_git.sh
    * 个人的各git仓库路径配置，实现./do update/push/init 来达到初始化 更新 推送所有配置的项目
* help_git.sh
    * 工作所需要的 仓库a提交后需要差异同步到仓库b
* shell_help.c
    * shell学习中整理的和遇到的一些常识性问题介绍
* shell_coding.c
    * shell编程学习中整理的常用的语法规则 if for function 数组 字符串等操作



