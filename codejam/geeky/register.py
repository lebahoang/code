import os
import sys
import md5


pi = sys.stdin.readline().strip().split(".")
print len(pi[1])
pi = pi[1][:524287]
md = md5.new()
md.update(pi)
print md.hexdigest()


