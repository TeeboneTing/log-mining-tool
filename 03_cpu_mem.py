#!/usr/bin/python
#Code Description:
#   print out cpu and memory usage per 5 minutes from "ps aux" command log

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date:
#   2012 AUG 31

#Modify History: 
#   2012 SEP 11: minor modify (mem append from line.split()[8])
#   2012 AUG 31: add code description and comments
#   2012 MAY 21: latest code

import sys
cpu = []
mem = []
#print 'cpu\tmem'
for line in sys.stdin:
    #starts from USER...
    if len(line.split()) < 8 or line.startswith("USER"):
        if cpu and mem:
            #aggregate cpu , memory and output, zero the values
            cpu_total = reduce((lambda x,y: x+y),cpu)
            mem_total = reduce((lambda x,y: x+y),mem)
            print "%.2f\t%.2f"%(cpu_total,mem_total)
            cpu = []
            mem = []
    else:
        #append cpu and memory list
        #skip wrong CPU usage (more than 1600%, 16 cores per machine)
        try:
            if float(line.split()[3]) > 1600:
                continue
            else:
                cpu.append(float(line.split()[3]))
                mem.append(float(line.split()[8]))
        except:
            print line

#cpu_total = reduce((lambda x,y: x+y),cpu)
#mem_total = reduce((lambda x,y: x+y),mem)
#print "%.2f\t%.2f"%(cpu_total,mem_total)
