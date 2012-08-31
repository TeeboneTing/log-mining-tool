#!/bin/bash

#Code Description:
#   A shell script to run 03_cpu_mem.py
#   Specify the input and output log files first

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date:
#   2012 AUG 31

#Modify History: 
#   2012 AUG 31: add code description and comments
#   2012 MAY 21: latest code

#months
for((j=5;j<=8;j=j+1))
do
    # No. of machines
    for((i=1;i<=15;i=i+1))
    do
        ./03_cpu_mem.py < 20110$j\_ps/20110$j.linux$i.log > local_result/20110$j\_ps_cpu_mem/20110$j.linux$i.cpumem.log
    done
done
