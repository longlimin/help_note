#!/bin/bash
###########################################
#git版本差异化 期间类补丁 文件覆盖制作
#
#
##-------------------------------- 
 
#app 下面复制到desktop下面 而git路径在echat_desktop下面所以需要路径转换映射
dirs_from=('/mnt/e/workspace/echat_desktop'     '/mnt/e/workspace/OBCP-Server'            )   #git目录
dirs_diff=('/mnt/e/workspace/echat_desktop/app' '/mnt/e/workspace/OBCP-Server'        )   #源路径截取 把源文件app下面的东西按照原有路径层次同步到目标路径
dirs_to=('/mnt/e/workspace/obcpweb/pro/desktop' '/mnt/e/workspace/obcpweb'            )   #覆盖同步路径
dir_open=''


# //git 日志格式化
# git log --pretty=format:"%H %an %cd %cr"
# git log --pretty=format:"%H %an %cd %cr" --after="2018-4-09 17:37:42" --before="2022-11-06 17:45:42"
# aa6492c71ea38371d95f26fc705ebc9be1edfd19 walker Wed Apr 11 10:41:03 2018 +0800 36 minutes ago
# e4514488d2772ea2acb8e62442eaea6e3331dbec walker Tue Apr 10 15:34:20 2018 +0800 20 hours ago
# e68d8075414572e8097e312dd02e2dfefc45a358 walker Mon Apr 9 18:42:27 2018 +0800 2 days ago
# //使用diff导出差异文件列表
# git diff aa6492c71ea38371d95f26fc705ebc9be1edfd19 e4514488d2772ea2acb8e62442eaea6e3331dbec --stat --name-only

# ./help_git.sh time_from time_to
function make(){
    dir_open=`pwd`  #记录使用脚本的路径

    time_from='2018-4-10'
    time_to='2099-11-06'
    dotype='default'
    if [ "$#" = "2" ]   #2018-4-10 2018-11-1
    then
        time_from=$1
        time_to=$2
    elif [ "$#" = "3" ]
    then
        time_from=$1
        time_to=$2
        dotype=$3
    else
        echo 'eg: ./help_git_branch.sh 339669 558353 <test/show测试并复制补丁到e/,>'
        exit
    fi
    echo 'diff '$time_from' -> '$time_to

    # echo ${#dirs_from[@]}
    for ((i=0; i<${#dirs_from[@]}; i++))
    do
        local dir_from=${dirs_from[$i]}
        local dir_diff=${dirs_diff[$i]}
        local dir_to=${dirs_to[$i]}   
        line
        echo '同步开始 '$dir_diff' -> '$dir_to 
        line
        log $dir_from $dir_diff $dir_to $time_from $time_to $dotype &   #异步同步等待 
        wait

        echo '同步完成 '$dir_diff' -> '$dir_to
        line
        echo
    done
    cd $dir_open    #回到当初位置
}

function log(){
    # echo $@
    local nowdir=$1
    local diffdir=$2
    local todir=$3
    local timefrom=$4
    local timeto=$5
    local dotype=$6
    cd $nowdir  #进入源目录
     
    diff $timefrom $timeto $nowdir $diffdir $todir $dotype   #比对分支差异文件并复制移动

}
function diff(){
    if [ "$#" = "6" ] 
    then
        local nowdir=$3
        local diffdir=$4
        local todir=$5
        local dotype=$6
        if [ "$dotype" = 'test' ]
        then
            todir='/mnt/e/make'
            echo '测试差异，处理文件到目录'$todir'，生成补丁文件夹'
            mkdir $todir -p
        fi   

        local diffdirLen=${#diffdir}+1  #/斜杠占位
        line
        local cmd="git diff $1 $2 --stat --name-only"
        echo $cmd
        local files=( `$cmd` )
        line
        echo '共计差异文件 '${#files[@]}' 个. '
        line
        #echo ${files[@]}
        echo '路径 '$diffdir' -> '$todir' '
        local delFileCount=0    # 差异删除文件数
        local cpFileCount=0     # 差异覆盖/添加文件数
        local delFileCountRel=0 # 实际删除文件数
        for ((i=0; i<${#files[@]}; i++))
        do
            local itemdiff=${files[$i]}                    #app/modules/chat/services/chatService.js
            local fileFromPath=$nowdir'/'$itemdiff         #/mnt/e/workspace/echat_desktop                 /app    /modules/chat/services/chatService.js 源文件真实路径
            local newItemDiff=${fileFromPath:$diffdirLen}  #                                                       /modules/chat/services/chatService.js 目标相对路径
            local fileToPath=$todir'/'$newItemDiff         #/mnt/e/workspace/obcpweb/pro/desktop                   /modules/chat/services/chatService.js 目标真实路径
            
            # echo $i' '$fileFromPath' -> '$fileToPath
            mkFileDir $fileToPath   #确保文件所在目录存在 否则cp失败
            if [ -f $fileFromPath ] # 源文件存在 
            then
                echo "$i cp $newItemDiff"
                cpFileCount=$[cpFileCount+1]
                # echo "cp $fileFromPath $fileToPath "
                cp $fileFromPath $fileToPath #-v    修改/添加文件 则覆盖文件
            else
                echo "$i rm $newItemDiff"
                delFileCount=$[delFileCount+1]
                # echo "rm $fileToPath"
                if [ -f $fileToPath ] # 目标文件存在 
                then
                    delFileCountRel=$[delFileCountRel+1]
                    rm $fileToPath  # 删除文件 源不存在了 目标存在的情况 就删除目标文件
                fi
            fi    
        done
        line
        echo "差异添加/修改: $cpFileCount  差异删除: $delFileCount  实际删除: $delFileCountRel"
    else
        echo '比对分支并移动需要 版本号from to 和 源路径 目标路径 args:'$@
    fi
}



function mkFileDir(){
    myPath=$1
    local fileDir=${myPath%/*}
    if [ ! -d $fileDir ]; then
        mkdir $fileDir -p
    fi
}

function line(){
    echo "---------------------------------"
}

function help(){
    echo "-------make --------"
}

function git_main(){
    echo
    ##########################do something yourself
    git_init $@
    echo
}

function git_init(){
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


# 单独执行文件时操作如下 引入时提示
_temp='help_git_branch.sh'
if [[ $0 =~ $_temp ]]
then
    # git_main $@
    make $@
else
    echo 'source '$_temp
fi 