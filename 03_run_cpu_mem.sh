#!/bin/bash

#Code Description:
#   A shell script to run 03_cpu_mem.py
#   Specify the input and output log files first

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date:
#   2012 AUG 31

#Modify History: 
#   2012 SEP 11: modify input directory/files
#   2012 AUG 31: add code description and comments
#   2012 MAY 21: latest code

#from 2012 08
#DATE
for((j=19;j<=19;j=j+1))
do
    # No. of machines
    for((i=1;i<=20;i=i+1))
    do
        ./03_cpu_mem.py < ./201208_ps/201208-$j.linux$i.log > local_result/201208_ps_cpu_mem/201208-$j.linux$i.cpumem.log
    done
done
