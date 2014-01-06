import os
import sys


def cmp_method(a,b):
    if a[0] != b[0]:
        return a[0]-b[0]
    else:
        return a[1] - b[1]
        
def check_order(stick):
    t = stick[0]
    for it in stick[1:]:
        if t[1] > it[1]:
            t = it
        else:
            return True
    return False
t = int(sys.stdin.readline().strip())
for _ in xrange(t):
    n = int(sys.stdin.readline().strip())
    arr = map(int,sys.stdin.readline().strip().split(" "))
    stick = []
    for i in xrange(0,n*2,2):
        stick.append((arr[i],arr[i+1]))
    
    count = 0
    stick = sorted(stick,cmp=cmp_method)
    while stick:
        if check_order(stick) == False:
            count += len(stick)
            break
        count += 1
        first = stick.pop(0)
        new = []
        for it in stick:
            if first[1] <= it[1]:
                first = it
            else:
                new.append(it)
        
        stick = new[:]
        
    print count            
        
    
        
