#!/bin/bash
###########################################


if [ -z "$1" ];then
    echo "./timer.sh './help.sh adjf' <5 s> "
    exit
fi
cmd=$1

deta=5
if [ ! -z $2 ];then
    deta=$2
fi
count=999999
if [ ! -z $3 ];then
    count=$3
fi


echo "Interval sleep $deta sec, count $count start "

for ((i=0; i<$count; i++))
do
    echo "----------------"
    echo `date "+%Y-%m-%d %H:%M:%S" `" now $i/$count sleep $deta run ! " 
    $cmd 
    sleep $deta
done

