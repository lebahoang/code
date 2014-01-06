import os
import sys
import pprint

def longest(arr,left,right,string1,string2,i,j):
    if left > right:
        return -1
    mid = (left+right)/2
    if i+1-arr[mid] < 0 or j+1-arr[mid] < 0:
        return longest(arr,left,mid-1,string1,string2,i,j)
    if string1[ i+1-arr[mid]:i+1  ] == string2[ j+1-arr[mid]:j+1  ] and string1[ i-arr[mid]:i+1 ] != string2[ j-arr[mid]:j+1 ]:
        return arr[mid]
    if string1[ i+1-arr[mid]:i+1 ] == string2[ j+1-arr[mid]:j+1 ] and string1[ i-arr[mid]:i+1 ] == string2[ j-arr[mid]:j+1 ]:
        return longest(arr,mid+1,right,string1,string2,i,j)
    elif string1[ i+1-arr[mid]:i+1 ] != string2[ j+1-arr[mid]:j+1 ]:
        return longest(arr,left,mid-1,string1,string2,i,j)
        
def longest_sub_common(s1,s2,k):
    dp = {}
    arr = [i for i in xrange(k,1000)]
    for i in xrange(len(s1)):
        max_of_i = 0
        pos = []
        for j in xrange(len(s2)):
            flag = flag2 = 0
            rs = 0
            if i-1 >= 0:
                rs = dp[(i-1,j)]
                flag = 1
            if j-1 >= 0:
                if rs < dp[(i,j-1)]:
                    rs = dp[(i,j-1)]
                flag2 = 1
            s = 0
            t = -1
            if s1[i] == s2[j]:
                #s += 1
                t = longest(arr,0,len(arr)-1,s1,s2,i,j)
                #print i,j,t
                if t != -1:
                    s += t
            if t != -1 and i-t >= 0 and j-t >= 0:
                s += dp[(i-t,j-t)]
            if rs < s:
                rs = s   
            dp[(i,j)] = rs   
    pprint.pprint(dp)
    return dp[(len(s1)-1,len(s2)-1)]

#print longest_sub_common("lovxxelyxxxxx","xxxxxxxlovely",2)
print longest_sub_common("aaabaaa","aaaaaa",3)
