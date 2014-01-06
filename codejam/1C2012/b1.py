import sys
import math
def solve(a,other,D):
    waiting = []
    for i in range(len(other)):      
        if other[i][1] <=D:
            t = other[i][0] - math.sqrt(other[i][1]/(0.5*a))
            if t > 0 :
                waiting.append(t)    
        else:
            if i >0:
                v = (other[i][1] - other[i-1][1])/(other[i][0] - other[i-1][0])
                t1 = other[i-1][0]+(D-other[i-1][1])/v
                t2 = math.sqrt(D/(0.5*a))
                t = t1 -t2
                if t >0:
                    waiting.append(t)  
            break 
    if not waiting:
        return math.sqrt(D/(0.5*a))
    t = max(waiting)
    return t + math.sqrt(D/(0.5*a))          
                
                                               

testcase = int(sys.stdin.readline().strip())
case = 1
for _ in range(testcase):
    D,N,A = sys.stdin.readline().strip().split()
    D = float(D)
    N = int(N)
    A = int(A)
    other = []
    accelerations = []
    for _ in range(N):
        t,x = sys.stdin.readline().strip().split()
        t = float(t)
        x = float(x)
        other.append((t,x)) 
    accelerations = map(float,sys.stdin.readline().strip().split())
    print "Case #%d:" %case
    for a in accelerations:
        rs = solve(a,other,D)
        print "%.6f" %(rs)
    case +=1
