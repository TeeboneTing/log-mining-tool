#!/usr/bin/env python
#Code Description:
#   Input from mapper intermediate file, after sorted by hash key
#   apply reducer funstion on each same hash key.
#   Reducer will calculate average CPU, memory, vsz, and rss usage.
#   Then execution duration will be determined by the maximum value in the same hash key pairs

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date:
#   2012 SEP 05

#Modify History: 
#   2012 SEP 05: add priority numer, process status, system user flag
#   2012 AUG 31: add code description and comments
#   2012 MAY 20: latest code

import sys
add = (lambda x,y:x+y)
max_exe_secs= 0
exe_secs = 0
current_key = None
current_val = None
cpu = [] #(cpu,exe_secs) sort by exe_secs
vsz = []
rss = []
mem = []
cmd = []
sysuser = None
proc_stat = None
pri = []

for line in sys.stdin:
    line = line.strip()
    key , values = line.split('\t')
    values = values.split()
    #try:
    exe_secs = int(values[7])
    #except ValueError:
    #    continue
    #cpu.append((values[2],values[0]))
    if current_key == key:
        cpu.append(float(values[0]))
        mem.append(float(values[1]))
        pri.append(float(values[2]))
        vsz.append(int(values[3]))
        rss.append(int(values[4]))
        proc_stat = int(values[5])
        sysuser = int(values[6])
        cmd = values[8:]
        #check exe_secs,find MAX exe_secs
        if exe_secs > max_exe_secs:
            max_exe_secs = exe_secs
            #DEBUG print
            #print 'max exec! %d'%max_exe_secs
    else:
        if current_key:
            cmd_s = ""
            for s in cmd:
                cmd_s = cmd_s + "%s "%s
            #Calculate average usage
            total_cpu = reduce(add,cpu)/len(cpu)
            total_mem = reduce(add,mem)/len(mem)
            total_pri = reduce(add,pri)/len(pri)
            total_vsz = reduce(add,vsz)/len(vsz)
            total_rss = reduce(add,rss)/len(rss)
            print "%s\t%.2f %.2f %d %d %d %d %d %d %s"%(current_key,total_cpu,total_mem,total_pri,total_vsz,total_rss,proc_stat,sysuser,max_exe_secs,cmd_s)
            cpu = []
            mem = []
            vsz = []
            rss = []
            cmd = []
            pri = []
            sysuser = None
            proc_stat = None
            max_exe_secs = 0
        current_key = key
        current_val = values
        cpu.append(float(values[0]))
        mem.append(float(values[1]))
        pri.append(float(values[2]))
        vsz.append(int(values[3]))
        rss.append(int(values[4]))
        proc_stat = int(values[5])
        sysuser = int(values[6])
        cmd = values[8:]
        #check exe_secs,find MAX exe_secs (execution duration)
        if exe_secs > max_exe_secs:
            max_exe_secs = exe_secs

#For the last key in reducer
if current_key:
    #Calculate average usage
    total_cpu = reduce(add,cpu)/len(cpu)
    total_mem = reduce(add,mem)/len(mem)
    total_vsz = reduce(add,vsz)/len(vsz)
    total_rss = reduce(add,rss)/len(rss)
    total_pri = reduce(add,pri)/len(pri)
    cmd_s = ""
    for s in cmd:
        cmd_s = cmd_s + "%s "%s
    print "%s\t%.2f %.2f %d %d %d %d %d %d %s"%(current_key,total_cpu,total_mem,total_pri,total_vsz,total_rss,proc_stat,sysuser,max_exe_secs,cmd_s)
