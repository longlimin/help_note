#!/bin/bash  
########################################### 
#./do dirfile <help>
#文件筛选
#全文件
#递归
###########################################
source constant.sh
source tools.sh 

##-----------------------------------------

function dirfile_main(){ 
    echo
    toolsShow $@
    ##########################do something yourself
    dirfile_init $@
    ##########################
    toolsLineLong 
    echo
}
dirfile_level='0'
dirfile_ifcop='0'
dirfile_reg='.*'
function dirfile_init(){
    echo '<<eg: ./do_dirfile.sh test<dir> reg<’^.*aaa.*‘> 0<show dir level> 0<if show file> '
    
    path=$1    
    
    if [ -n "$3" ] 
    then
        dirfile_level=$3
    fi 
    if [ -n "$4" ] 
    then
        dirfile_ifcop=$4
    fi 
    if [ -n "$2" ] 
    then
        dirfile_reg=$2
    fi 
    
    if [ ! -d "$path" ] 
    then
        echo '参数1为目录'
        return 1
    fi 
    realPath=`pwd`'/'$path
    echo 'rootPath: '$realPath 
    dirfile_showdir $realPath '1'
    
}
function dirfile_showdir(){
    #realPath=$1
    nowLevel=$2
    
    if [[ $nowLevel > $dirfile_level && $dirfile_level > 0 ]]  
    then
        return 0 
    fi
    
    if [ ! -d "$1" ] 
    then
        return 0 
    fi
    
    toolsMakestr '-' ${#1} #$nowLevel
    res=`cat $_toolsres`
    echo $1 #'    level:'$nowLevel'      dir_level:'$dirfile_level
    
    if [[ $dirfile_ifcop > 0 ]]
    then
        arr=(`ls $1`)
        len=${#arr[@]}
        echo ' file number: '$len
    else
        #echo $res'====file>>'
        for obj in `ls $1`
        do
            path=$1'/'$obj
            if [ -f "$path" ]
            then 
                if [[ $obj =~ $dirfile_reg ]] 
                then
                    echo $res''$obj
                fi  
            fi 
        done
    fi
    #echo $res'++++dire>>'
    for obj in `ls $1`
    do 
        path=$1'/'$obj 
        if [ -d "$path" ]
        then 
            #echo $path 
            nowLevel=`expr $nowLevel + 1`
            dirfile_showdir $path  $nowLevel
        fi 
    done 
}
 

function dirfile_show(){
    path=$1
    _rootDir=`pwd`
    realPath=$_rootDir'/'$path 
    echo "now path: "$realPath
    for obj in `ls  $realPath`
    do
        obj=$realPath'/'$obj
        if [ -f "$obj" ]
        then
            echo $obj" file"
        elif [ -d "$obj" ]
        then
            echo $obj" directory"
        else
            echo $obj" not file or directory"
        fi 
    done
}
 

function controlDir(){ 
    if [ ! -d "$1" ] 
    then
        return 0 
    fi
    path=$1
    for obj in `ls $1`
    do
        path=$1'/'$obj
        if [ -f "$path" ]
        then 
            if [[ $obj =~ $dirfile_reg ]] 
            then
                echo $res''$obj
            fi  
        fi 
    done
    for obj in `ls $1`
    do 
        path=$1'/'$obj 
        if [ -d "$path" ]
        then 
            dirfile_showdir $path  $nowLevel
        fi 
    done 
} 


# 单独执行文件时操作如下 引入时提示
_temp='do_dirfile.sh'
if [[ $0 =~ $_temp ]]
then
    dirfile_main $@
else
    echo 'source '$_temp
fi 


