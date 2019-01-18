# !/bin/bash  
########################################### 
# ./do function <help>
# About:
# 
# 
###########################################
source constant.sh
source tools.sh



function do_start_sftware_start(){
    toolsLineLong

    out 'start linux software '
    local arr=( 
    '/home/walker/software/eclipse/eclipse ' 
    '/home/walker/software/smartgit/bin/smartgit.sh ' 
     )
    for ((i=0; i<${#arr[@]}; i++))
    do
        item=${arr[$i]}
        cmd='ps -lf | grep -v grep | grep '$item
        res=`eval $cmd`
        if [[ $res == "" ]]
        then
            call $item
        else
            out 'have started'
            out $res        
        fi
    done    
 

    
    out 'start linux software over '
    toolsLineLong
} 





function do_start_sftware(){
    echo $@
} 

# 单独执行文件时操作如下 引入时提示
_temp='do_start_software.sh'
if [[ $0 =~ $_temp ]]
then
    do_start_sftware_start $@
else
    echo 'source '$_temp
fi 
