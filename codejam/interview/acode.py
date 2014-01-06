import os
import sys

def count(code):
    dp = [0 for i in xrange(len(code))]
    max_index = len(code)-1
    dp[max_index] = 1 if code[max_index] != '0' else 0
    for i in xrange(max_index-1,-1,-1):
        dp[i] = 0
        if i+1 <= max_index:
            if code[i] > '0':
                dp[i] += dp[i+1]
        num = code[i] + code[i+1]
        if i+2 <= max_index:
            if num <= '26' and code[i] != '0':
                dp[i] += dp[i+2]
        else:
            if num <= '26' and code[i] != '0':
                dp[i] += 1
    return dp[0]
    
#25114
#1111111111
#3333333333
#10
#101
#110
#1101 
#101
#1022
#1010 
#a = ""
#for i in xrange(1000):
#    a += "11210"    

while True:
    code = sys.stdin.readline().strip()
    if code == '0':
        break
    print count(code)        
