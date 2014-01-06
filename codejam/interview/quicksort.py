import resource
def partition(arr,l,h):
    pivot = arr[l]
    partition_index = l+1
    for i in xrange(l+1,h+1):
        if arr[i] < pivot:
            t = arr[i]
            #print arr[i],i,partition_index
            arr[i] = arr[partition_index]
            arr[partition_index] = t
            partition_index += 1
    t = arr[partition_index-1]
    arr[partition_index-1] = arr[l]
    arr[l] = t
    return partition_index-1

def quicksort1(arr,l,h):
    #print l, h,arr
    if l < h:
        p = partition(arr,l,h)
        quicksort1(arr,l,p-1)
        quicksort1(arr,p+1,h)
    return arr

#arr = [3,4,5,76,1,2,3,9,323,32]
import random
arr = []
for i in  xrange(10000):
    arr.append(random.randint(0,1000))
#print quicksort1(arr,0,len(arr)-1)

    
#arr = [3,1,3,5,2,1,7,5,5,6,7,4,34,65,8,2,3,2,2,2,1]
print quicksort(arr,0,len(arr)-1)
print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    
    
    

