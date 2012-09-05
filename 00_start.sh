#!/bin/bash
#Code Descrition: 
#   Shell script for starting analysis log data
#   This script will start 01_anlysis_ps_map.py and 02_analysis_ps_reduce.py
#   A local MapReduce-like drver script.

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date: 
#   2012 SEP 05
#   2012 AUG 31

#Modify History: 
#   2012 SEP 05: remove date selection, only provide monthly process.
#   2012 AUG 31: latest code with adding code description and comments

# No. of machines
NO=20
#month
for((j=2;j<=7;j=j+1))
do
    (rm ./local_result/20120$j\_ps/*.log && echo "removing old Map intermediate file...")
    (rm ./local_result/20120$j\_ps_reduced/*.log && echo "removing old Reduce output file...")
    #date
    #for((k=19;k<=25;k=k+1))
    #do
        for((i=1;i<=$NO;i=i+1))
        do
            cat ./20120$j\_ps/20120$j-$k.linux$i.log \
            | ./01_analysis_ps_map.py \
            | sort -k 1,1 > ./local_result/20120$j\_ps/20120$j.linux$i.log 
            cat ./local_result/20120$j\_ps/20120$j.linux$i.log \
            | ./02_analysis_ps_reduce.py >> ./local_result/20120$j\_ps_reduced/20120$j.linux$i.log
        done
    #done
done
