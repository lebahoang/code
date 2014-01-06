import os
import sys


t = int(sys.stdin.readline().strip())
for _ in xrange(t):
    c,k,w = map(int,sys.stdin.readline().strip().split(" "))
    if c*w > k:
        print "no"
    else:
        print "yes"
