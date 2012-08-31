#!/usr/bin/python
#Code Description:
#   Count total job or single job repeat frequency from command arguments in 04's output

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date:
#   2012 AUG 31

#Modify History: 
#   2012 AUG 31: Add code description and comments
#   2012 AUG 30: latest code


import sys
freq = {}
#TRY for to find one kind of job repeat condition
#Uncomment code below if you want to find only one process repeated condition
#But somehow in the for loop there are some codes needed to modify
#try:
#    proc = sys.argv[1] #indicates which process would user like to break down.
#except:
#    print "usage: %s process name"%(sys.argv[0])
for line in sys.stdin:
    key = line.split()[0].split('/')[-1]
    line = line[:-1]
    #if key == proc:
    #    print line
    if freq.has_key(key):
        freq[key] += 1
    else:
        freq[key] = 1

#print out "job name"  and  "counts"
#sorted by counts
for w in sorted(freq, key=freq.get, reverse=True):
    print "%s\t%s"%(w, freq[w])
