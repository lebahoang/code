import os
import sys


def cmp_method(a,b):
    if a[0] != b[0]:
        return a[0]-b[0]
    else:
        return a[1] - b[1]
        
def binary_search(length_arr,l,r,value):
    #print length_arr,l,r,value
    if l == r-1:
        if length_arr[l] > value and length_arr[r] < value:
            return (l,1)
        else: 
            if value < length_arr[r]:
                return (r,1)
            elif value > length_arr[l]:
                return (l,-1)
            else:
                return (None,-2)
    elif l == r:
        if length_arr[l] > value:
            return (r,1)
        elif length_arr[l] < value:
            return (l,-1)
        else:
            return (None,-2)
    mid = (l+r)/2
    if length_arr[mid] < value:
        return binary_search(length_arr,l,mid-1,value)
    elif length_arr[mid] > value:
        return binary_search(length_arr,mid+1,r,value)
    else:
        return (None,-2)
    
def longest_decreasing_subsequence(arr):
    length_arr = [arr[0][1]]
    for i in xrange(1,len(arr)):
        x,sign = binary_search(length_arr,0,len(length_arr)-1,arr[i][1])
        if sign == 1:
            if len(length_arr) -1 == x:
                length_arr.append(arr[i][1])
            else:
                if arr[i] > length_arr[x+1]:
                    length_arr[x+1] = arr[i][1]
        elif sign == -1:
            length_arr[x] = arr[i][1]
    #print length_arr
    return len(length_arr)        
   
            
t = int(sys.stdin.readline().strip())          
for _ in xrange(t):
    n = int(sys.stdin.readline().strip())
    arr = map(int,sys.stdin.readline().strip().split(" "))
    stick = []
    for i in xrange(0,n*2,2):
        stick.append((arr[i],arr[i+1]))
    
    
    stick = sorted(stick,cmp=cmp_method)
    count = longest_decreasing_subsequence(stick)   
    print count            
        
    
        
