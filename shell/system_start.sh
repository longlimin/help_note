#!/bin/bash  
########################################### 
# the shell exe on the system boot

echo '##########################################'
date
echo 'Start the software on system boot'

arr=( 
'/home/walker/software/redis-5.0.3/src/redis-server'
'date' 

)

file='/home/walker/system_start.log'
echo `date` > $file 


for ((i=0; i<${#arr[@]}; i++))
do
    item=${arr[$i]}
    echo -e "Start $i \t $item"
    $item >> $file &
    
done

date
echo '##########################################'

