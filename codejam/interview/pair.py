import os
import sys


arr = [5,5,5,5,6,6]
k = 2
a = b = 0
arrk = [[] for i in xrange(k-1)]
for i in arr:
    if i % k == 0:
        a += 1
    else:
        b += 1
        mod = i % k
        arrk[mod-1].append(i)

print arrk        
if b % 2 != 0:
    print False
else:
    flag = 1
    i = 0
    j = len(arrk)-1
    while i < j:
        if len(arrk[i]) != len(arrk[j]):
            print False
            flag = 0
            break
        i += 1
        j -= 1
    if flag == 1:
        print True
