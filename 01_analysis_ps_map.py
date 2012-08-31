#!/usr/bin/python
#Code Description:
#   A mapper function that input from "ps aux" and
#   calculate a hash value as "key" (hash from a user name, PID, and command line arguments)
#   A hash key represent a single process from a user.
#   "values" include CPU usage, Memory usage, vsz, rss, and execution duration on that time

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date:
#   2012 AUG 31

#Modify History: 
#   2012 AUG 31: add code description and comments
#   2012 MAY 20: latest code

import sys
import hashlib

# A function convert time format from DD-HH:MM:SS to seconds
def time_to_sec(time):
    sec = 0
    #check day
    time = time.split('-')
    if len(time) > 1:
        sec += int(time[0])*24*60*60
        time = time[1].split(':')
    #check hour,min,secs
    else:
        time = time[0].split(':')
    if len(time) == 3:
        sec += int(time[0])*60*60
        time = time[1:]
    if len(time) == 2:
        sec += int(time[0])*60
        time = time[1:]
    if len(time) == 1:
        sec += int(time[0])
    return sec

# Mapper function
def main():
    for line in sys.stdin:
        out = {}
        line_args = line.split()
        #print line_args
        if len(line_args) > 1:
            if line_args[0]=='USER':
                pass
            elif line_args[0]=='root' or line_args[0]=='wsmon':
                pass
            else:
                #print line_args
                out['usr']=line_args[0]
                out['pid']=int(line_args[2])
                out['cpu']=float(line_args[3])
                out['mem']=float(line_args[4])
                out['vsz']=int(line_args[7])
                out['rss']=int(line_args[8])
                out['time']=time_to_sec(line_args[12])
                out['cmd']=''
                for string in line_args[13:]:
                    out['cmd'] = out['cmd']+' '+string
                m=hashlib.md5()
                m.update(out['usr']+str(out['pid'])+str(out['cmd']))
                out['key']=m.hexdigest()
                print '%s\t%.2f %.2f %d %d %d %s'%(out['key'],out['cpu'],out['mem'],out['vsz'],out['rss'],out['time'],out['cmd'])
if __name__ == "__main__":
    main()
