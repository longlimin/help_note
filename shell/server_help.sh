#!/bin/bash
###########################################
#do
#一些常用简单功能脚本
#配置启动脚本命令cmd
#配置日志文件路径logfile
#./do start <help><stop><show><log><restart>

##-----------------------------------------
cmd='tail -n 10 -f do_git.sh'
# cmd='/opt/application/resin-3.1.12/bin/httpd.sh -conf /opt/application/resin-3.1.12/conf/mccp.conf'
logfile='/opt/resin/logs/log.log'
#shutdown the process by the grep pids by the cmd name  Warning ! the space
greparg='obcp_conf'

about='./server.sh method ( <log> <show> <start> <stop> <restart> : <params> ) '
taillog='tail -n 200 -f '"$logfile"
#如何将变量中的值取出来作为绝对字符串'' 所以暂用直接获取pids
pids=`ps -ef | grep "$greparg" | grep -v grep | cut -c 9-15`
#通过ps管道删除接收
# ps -ef | grep $greparg | grep -v grep | cut -c 9-15 | xargs kill -9
  
##------------------------------------------
function start(){
    ids=$pids
    if [[ "$ids" != "" ]]
    then
        show
    else
        line
        echo "$cmd  > $logfile &"
        line
        nohup $cmd  > $logfile &
        echo 'Server started'
        log
    fi
}
function stop(){    
    line
    echo "kill -9 $pids"
    line
    kill -9 $pids
    echo 'Server stop'
    pids='' #clear stoped pids
    line
}
function restart(){
    stop
    start
}

function log(){
    line
    echo "$taillog"
    line
    $taillog
    line
}

function show(){
    line
    ids=$pids
    echo "ps -ef | grep $greparg | grep -v grep | cut -c 9-15"
    line
    if [[ "$ids" != "" ]]
    then
        echo 'Have been started, Pids:'
        echo $ids
    else
        echo 'Stoped ! '
    fi
    line
}
function help(){
    line
    echo 'Eg:'
    echo $about
    line
}
function line(){
    echo "---------------------------------"
}

function do_main(){
    echo
    ##########################do something yourself
    do_init $@
    echo
}

function do_init(){
    method=$1
    if [[ "$method" != "" ]]
    then
        rootParams=($@)
        params=(${rootParams[@]:1})
        $method ${params[@]}
    else
        help 
    fi
} 


#start
do_main $@