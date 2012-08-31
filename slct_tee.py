#!/usr/bin/python

# Code Description
#   slct_tee.py
#   SLCT python simple version

#Author: 
#   Teebone Ding @Graduate Institute of Networking and Multimedia, National Taiwan University

#Latest Update Date:
#   2012 AUG 31

#Modify History: 
#   2012 AUG 31: add code description and comments
#   2012 JUL 25: latest code

import sys
import getopt


# create word dictionary and parse support threshold
def create_word_table(fptr,s):
    word_table = {}
    proc_table = {}
    line_count = 0
    for line in fptr:
        proc = line.split()[0]
        if proc_table.has_key(proc):
            proc_table[proc] += 1
        else:
            proc_table[proc] = 1
        # add words to dictionary, ignore 1st word due to process name should be fixed
        line = line.split()[1:]
        for w in line:
            if word_table.has_key(w):
                word_table[w] += 1
            else:
                word_table[w] = 1 
        line_count+=1
    print >> sys.stderr ,"%s command line arguments"%line_count
    # parse SUPPORT
    if s == 0:
        pass
    elif s[-1] == "%":
        if int(s[:-1]) > 100:
            print >> sys.stderr, "support threshold error: more than 100%%"
            sys.exit()
        s = int(float(s[:-1])*line_count/100)
    else:
        s = int(s)
    return word_table,proc_table,s 


# if word count < SUPPORT, delete from word_table
def find_frequent_words(word_table,s):
    new_table = {}
    for k in word_table:
        if word_table[k] >= s:
            new_table[k] = word_table[k]
    return new_table


"""
 try to aggregate commands to clusters
 data structure:
 clusters:
    an array of clusters.
    in each element, [array of (freq words,position),support,cmd length]
"""
def find_cluster_candidates(fptr,word_table,tok):
    clusters = []
    for line in fptr:
        tmp = []
        lines = line.split()
        tmp.append((lines[0],0))
        pos = 1
        for w in lines[1:]:
            if word_table.has_key(w):
                tmp.append((w,pos))
            pos +=1
        found = 0        
        for c in clusters:
            if c[:-2] == tmp:
                found = 1
                c[-2] += 1
                break
            # do token permutation
            elif len(c)-2 == len(tmp) and c[0] == tmp[0] and tok:
                correct = 1
                for i in range(1,len(tmp)):
                    for j in range(1,len(c)-2):
                        if tmp[i][0] == c[j][0]:
                            correct += 1
                if correct == len(c)-2:
                    found = 1
                    c[-2] += 1
                    break
        if not found:
            # append support number and command length in the end of the cluster candidate
            l = len(lines)
            tmp.append(1) #support
            tmp.append(l) #cmd length
            clusters.append(tmp)
    return clusters


# preserve clusters that exceed support threshold, also print outliers
def find_clusters(clusters,word_table,s,f,o,tok):
    new_clusters = []
    for c in clusters:
        if c[-2] >= s:
            new_clusters.append(c)

    # find outliers (cmd NOT included in new_clusters)
    for line in f:
        tmp = []
        lines = line.split()
        tmp.append((lines[0],0))
        pos = 1
        for w in lines[1:]:
            if word_table.has_key(w):
                tmp.append((w,pos))
            pos +=1
        found = 0        
        for c in new_clusters:
            if c[:-2] == tmp:
                found = 1
                break
            # do token permutation
            elif len(c)-2 == len(tmp) and c[0] == tmp[0] and tok:
                correct = 1
                for i in range(1,len(tmp)):
                    for j in range(1,len(c)-2):
                        if tmp[i][0] == c[j][0]:
                            correct += 1
                if correct == len(c)-2:
                    found = 1
                    break
        if not found:
            # write out to outliers
            o.write(line)
    return new_clusters


HELP_STR = """Usage: %s 
    -f(--file) <input_file> 
    -s(--support) <support(%%)> 
    -o(--outlier) <outlier> 
    -t(--token)"""%sys.argv[0]
def help():
    print >> sys.stderr, HELP_STR


def parse_opts():
    INPUT = OUTLIER = ""
    SUPPORT = 0
    TOKEN = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hf:s:o:t",["help","file=","support=","outlier=","token"])
    except getopt.GetoptError:
        help()
        sys.exit()
    if len(opts) == 0:
        help()
        sys.exit()
    for o,a in opts:
        if o in ("-h","--help"):
            help()
            sys.exit()
        if o in ("-f","--file"):
            INPUT = a
        if o in ("-o","--outlier"):
            OUTLIER = a
        if o in ("-s","--support"):
            SUPPORT = a 
        if o in ("-t","--token"):
            TOKEN = 1
    return (INPUT,OUTLIER,SUPPORT,TOKEN)


def print_clusters(clusters):
    #print "There is/are %d cluster(s)."%len(clusters)
    for c in clusters:
        cmd_len = c[-1]
        word_cnt = 0
        for w in c[:-2]:
            if w[1] == word_cnt:
                print "%s"%w[0],
            else:
                for i in range(w[1]-word_cnt):
                    print "*",
                    word_cnt += 1
                print "%s"%w[0],
            word_cnt += 1
        for i in range(cmd_len-word_cnt):
            print "*",
        print ""
        print "SUPPORT:%d\n"%c[-2]


def main():
    # parse opts
    INPUT,OUTLIER,SUPPORT,TOKEN = parse_opts()
    # open input file
    f = open(INPUT,"r")

    # 1st pass, word count
    WORDS,PROCS, SUPPORT = create_word_table(f,SUPPORT)
    f.close()

    #return frequent words in a table
    WORDS = find_frequent_words(WORDS,SUPPORT)
    print >> sys.stderr ,"Word count: %d frequent words"%len(WORDS)
    print >> sys.stderr ,"%d different processes"%len(PROCS)
    print >> sys.stderr ,"support s:%d"%SUPPORT
    print >> sys.stderr ,""
    #print PROCS

    # do clustering
    f = open(INPUT,"r")
    CLUSTERS = find_cluster_candidates(f,WORDS,TOKEN)
    f.close()
    # print results
    print >> sys.stderr ,"Before refine, there is/are %d cluster(s).\n"%len(CLUSTERS)

    # refine cluster candidates with support threshold and write out outliers
    f = open(INPUT,"r")
    # TODO: delete file if OUTLIER exists.
    o = open(OUTLIER,"w")
    CLUSTERS = find_clusters(CLUSTERS,WORDS,SUPPORT,f,o,TOKEN)
    f.close()
    o.close()
    print >> sys.stderr ,"After refine, there is/are %d cluster(s).\n"%len(CLUSTERS)
    # print results
    print_clusters(CLUSTERS)

if __name__ == "__main__":
    main()
