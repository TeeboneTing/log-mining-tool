#!/bin/bash
#Code Description:
#   Merge each log files to 1 month log per workstation

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date: 
#   2012 SEP 05
#   2012 AUG 31

#Modify History: 
#   2012 SEP 05: canceled date selection, only provide monthly aggregation

# number of workstations
NO=20
# months
for j in 02 03 04 05 06 07;
do
    #for k in 19 20 21 22 23 24 25;
    #do
        # log input directory
        DIR=~/public_html/2012-${j}/*
        
        for((i=1;i<=$NO;i=i+1))
        do
            #find ${DIR} -name "*-${k}-ps.linux$i" -exec cat {} \; >> ./2012${j}_ps/2012${j}-${k}.linux${i}.log 
            find ${DIR} -name "*ps.linux$i" -exec cat {} \; >> ./2012${j}_ps/2012${j}.linux${i}.log 
            #find ${DIR} -name "*ps.linux$i" #| cat >> ./201108_ps/filename$i
        done
    #done
done
