#!/usr/bin/python

#Code Description:
#   from reduced ps log to find original command arguments
#   Ie, find job name (original command arguments) in one of the workloads 
#   splited from any filter criteria.
#   Output to standard output.

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date:
#   2012 SEP 11

#Modify History:
#   2012 SEP 11: Copied and modified from 04_*.py 
#   2012 SEP 10: Find CPU 0/100% processes
#   2012 AUG 31: Add memory limit, time_limit2, and cpu_limit2 breakpoint
#   2012 AUG 31: Add code description and comments
#   2012 MAY 21: latest code

import sys
import os

#Please specify input ps reduced log file name here
INPUT='./statistics/2012_234567_sys_user.log'


inFile = open(INPUT)
line =  inFile.readline()
process = []

cnt = 0
while line:
    arr = line.split('\t')[1].split()
    #cpu = float(arr[0])
    mem = float(arr[4])
    #sys_user = int(arr[6])
    if mem == 0:
        #for s in line.split('\t')[1].split()[8:]:
        #    print s,
        #print ""
        print line,
    line = inFile.readline()

#print cnt    
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
