import os

def format_array(array):
    new_arr =[]
    cur = array[0]
    for vl in array[1:]:
        if cur < 0:
            if vl <= 0:
                cur += vl
            else:
                new_arr.append(cur)
                cur = vl
        else:
            if vl >= 0:
                cur += vl
            else:
                new_arr.append(cur)
                cur = vl
    new_arr.append(cur)            
    intervals = []
    i = -1
    for j in xrange(len(new_arr)):
        if new_arr[j] > 0:
            if i != -1:
                intervals.append((i,j))
            i = j
    if not intervals:
        intervals.append((i,i))
    return new_arr,intervals
                    
                    
def connect(arr,intervals):
    dp = {}
    for i,j in intervals:
        if arr[i] + arr[i+1] + arr[j] >= arr[i] and arr[i] + arr[i+1] + arr[j] >= arr[j]:
            dp[(i,j)] = ( arr[i] + arr[i+1] + arr[j],-1)
        else:
            if arr[i] > arr[j]:
                dp[(i,j)] = ( arr[i],1)
            else:
                dp[(i,j)] = ( arr[j],1)
    merge = intervals[0]
    for i,j in intervals[1:]:
        
        if dp[(merge[0],merge[1])][1] == -1 and dp[(i,j)][1] == -1:
            dp[(merge[0],j)] = (dp[(merge[0],merge[1])][0] + dp[(i,j)][0] - arr[i], -1)
        else:
            dp[(merge[0],j)] = (max( dp[merge][0],dp[(i,j)][0]), 1)
        merge = (merge[0],j)    
    print dp
    return dp[merge]


#[1,-3,5,-2,9,-14,4]  
arr,intervals = format_array([-5,1,2,3,-100,1,2,3,4])  
print connect(arr,intervals)
#print connect1([1,-300,100,-2000,900,-14,4],[(0,2),(2,4),(4,6)])    

        
            
