#!/usr/bin/python

#Code Description:
#   from reduced ps log to find original command arguments
#   Ie, find job name (original command arguments) in one of the workloads 
#   splited from exe time(long/short) and cpu(high/low).
#   Output to standard output.

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date:
#   2012 AUG 31

#Modify History: 
#   2012 AUG 31: Add code description and comments
#   2012 MAY 21: latest code

import sys
import os

#Please specify input ps reduced log file name here
INPUT='./local_result/2012_2345.log'

#Determine the breakpoint here
time_limit = 234 # 3.9 mins
cpu_limit = 67 # 67%

inFile = open(INPUT)
line =  inFile.readline()
process = []
while line:
    arr = line.split('\t')[1].split()
    time = int(arr[4])
    cpu = float(arr[0])
    if cpu >= cpu_limit and time >= time_limit: 
        #print arr[-1]
        #process.append(line.split('\t')[0])
        for s in line.split('\t')[1].split()[5:]:
            print s,
        print ""
    line = inFile.readline()
    
    '''
    #outFile = open('./local_result/201108_ps/201108.linux1.log')
    for proc in process:
        str = "cat ./local_result/201107_ps/201107.linux%d.log | grep %s | uniq -f 6"%((i+1),proc)
        stdin, stdout = os.popen2(str)
        stdout.flush()
        line = stdout.read()
        print "%s "%line.split()[1],
        for s in line.split()[6:]:
            print "%s "%s,
        print ''
    '''
