import os
import random
import pprint
def generate_hash_table(dictionary):
    map = {}
    max_len = -1
    f = open(dictionary)
    for line in f:
        line = line.strip()
        if max_len < len(line):
            max_len = len(line)
        t = []
        map[line] = "1"
        for i in xrange(len(line)):
            x = list(line)
            x[i] = "*"
            t.append((x,i))
            map["".join(x)] = "1"
        while t:
            x,i = t.pop()
            y = 5
            while i+y <= len(line)-1:
                xx = x[:]
                xx[i+y] = "*"
                t.append((xx,i+y))
                map["".join(xx)] = "1"
                y += 1
    return map,max_len

def compute(string,max_len,map):
    dp = [[] for i in string]
    dp_min = [-1 for i in string]
    for i in xrange(len(string)):
        s = 0 if i <= max_len else i-max_len+1
        flag = {} 
        for j in xrange(s,i+1):
            t = string[j:i+1]
            arr = []
            if t in map:
                arr.append((list(t),-1,-1,0))
            for k in xrange(len(t)):
                x = list(t)
                x[k] = "*"
                arr.append((x,k,k,1))
            min = -1
            while arr:
                it,start,end,count = arr.pop()
                if "".join(it) in map:
                    if j > 0:
                        #print it,start,j
                        #print dp[j-1]
                        
                        for add,last in dp[j-1]:
                            if start != -1:
                                if start + j - last >= 5 or last == -1:
                                    #print "xx",add,last
                                    if (add+count,end+j) not in flag:
                                        dp[i].append((add+count,end+j))
                                        flag[(add+count,end+j)] = "1"    
                                        if dp_min[i] == -1 or dp_min[i] > add+count:
                                            dp_min[i] = add+count
                            else:
                                #print it,start,end,count, "2"
                                if (add,last) not in flag:
                                    flag[(add,last)] = "1"
                                    dp[i].append((add,last))
                                    if dp_min[i] == -1 or dp_min[i] > add:
                                        dp_min[i] = add
                                        
                        #print "-------------------------------" 
                                    
                    else:
                        dp[i].append((count,end+j))
                        flag[(count,end+j)] = "1"
                        if dp_min[i] == -1 or dp_min[i] > count:
                            dp_min[i] = count                             
                                                                                 
            
                if end != -1:
                    y = 5
                    while end+y <= len(t)-1:
                        itt = it[:]
                        itt[end+y] = "*"       
                        arr.append((itt,start,end+y,count+1))
                        y += 1
    #print dp    
    #print dp_min
    return dp_min[len(string)-1]


#generate_hash_table("input1")

import time
s = int(round(time.time()))       
map,max_len = generate_hash_table("input.txt")
f = open("C-large-practice.in")
t = int(f.readline().strip())
case = 1
for _ in xrange(t):
    string = f.readline().strip()
    rs = compute(string,max_len,map)
    print "Case #%d: %d" %(case,rs)
    case += 1
#print compute("codejam",max_len,map)
e = int(round(time.time()))
#print "----------------------------------------"
#print e-s       
                
