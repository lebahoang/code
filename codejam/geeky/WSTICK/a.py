import sys
import os
import copy
import pprint

print 5000
i = 1
j = 5000
arr = []
for _ in xrange(5000):
    arr.append(str(i))
    arr.append(str(j))
    i += 1
    j -= 1
print " ".join(arr)
