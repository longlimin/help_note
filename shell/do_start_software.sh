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


    local arr=( 
    '/home/walker/software/eclipse/eclipse ' 'echo aaa'     
    '/home/walker/software/smartgit/bin/smartgit.sh ' 
    
     )
     
    out 'start linux software '${#arr[@]}
    toolsLineLong
    for ((i=0; i<${#arr[@]}; i++))
    do
        local item=${arr[$i]}
        out 'Start '$i"\t"$item 
        local cmd='ps -elf | grep -v grep | grep '$item
        out $cmd
        local res=`eval $cmd`
        out $res        
        if [[ $res == "" ]]
        then
            call $item
        else
            cmd='ps -elf | grep -v grep | grep '$item" | awk '{print \$4}'"
            out $cmd
            pid=`eval $cmd`
            out 'have started pid '$pid

        fi
        toolsLineLong
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
