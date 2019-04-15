#!/bin/bash
buer=0
while [ $buer -eq 0 ]
do
webget=$(curl -s --connect-timeout 5 -m 5 http://zsb.sdzk.cn)
        if [ "$webget" == "" ];then
                echo "未开启"
                buer=0
        else
                cd ~
                ./sendmail.py
                buer=1
        fi
done