#!/bin/bash  
###########################################
#test *order* 1
###########################################


if [ -z $1 ]; then
    echo "./test *order* 1"
    exit
fi 
key=$1

deta=1
if [ ! -z $2 ]; then
    deta=$2
fi

for ((i=1; i>0; i++)) 
do
    echo -e "do $i \t `date`"
    ./help_redis.sh $key 
    sleep $deta 
done 
















