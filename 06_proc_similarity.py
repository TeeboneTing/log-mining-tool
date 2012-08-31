#!/usr/bin/python
#Code Description:
#   Find command argument similarity per process by key word finding.
#   This process is replaced by SLCT-like algorithm, a frequent pattern clustering algorithm.

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date:
#   2012 AUG 31

#Modify History: 
#   2012 AUG 31: Add code description and comments
#   2012 JUL  4: latest code


import sys
similar = {}
for line in sys.stdin:
    #for JAVA,
    #1.find -jar
    #2.find -cp and -classpath
    #3. others (class)
    cnt = 0
    key = ''
    for s in line.split():
        if s == '-data':
            key = line.split()[cnt+1]
        if s == '-jar':
            key = line.split()[cnt+1]
        elif s == '-cp' or s == '-classpath':
            key = line.split()[cnt+1]
        cnt += 1

    line = line[:-1]
    if similar.has_key(key):
        similar[key].append(line)
    #elif key.endswith('model'):
    #    key = key[:-6] #truncate '.model' suffix
    #    if similar.has_key(key):
    #        similar[key].append(line)
    else:
        similar[key] = [line]


#print out "similar key"  and  "command argument list"
#sorted by length of command argument list
#for w in sorted(similar, key=len(similar.get), reverse=True):
    #for cmd in similar[w]:
        #print "%s\t%s"%(w, cmd)
    #print ""
print len(similar)
for k in similar:
    print k
    for v  in similar[k]:
        print v
    print ""
