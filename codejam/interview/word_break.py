import os
import sys

def solve(dict, string):
    dp = []
    t = ""
    for i in string:
        t += i
        flag = False
        if t in dict:
            flag = True
        else:
            for j in xrange(len(dp)):
                if dp[j] == True:
                    if t[j+1:] in dict:
                        flag = True
                        break
        dp.append(flag)
    print dp
    return dp[-1]
def solve2(dict,string):
    dp = []
    t = ""
    for i in string:
        t += i
        flag = False
        words = []
        if t in dict:
            flag = True
            words.append(t)
            
        for j in xrange(len(dp)):
            if dp[j][0] == True:
                if t[j+1:] in dict:
                    flag = True
                    for word in dp[j][1]:
                        words.append(word+" "+t[j+1:])
                    
        dp.append((flag,words))
    return dp[-1]   
dict = {"i":1, "like":1, "sam":1, "sung":1, "samsung":1, "mobile":1, "and":1, "ice":1, "cream":1, "icecream":1, "man":1, "go":1, "mango":1}
string = "ilikesamsung"
string1 = "ilikesamsungmobileandicecream"
print solve2(dict,string1)
