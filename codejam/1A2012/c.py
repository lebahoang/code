import sys

def solve(L,R,total,last_min):
    min_v = -1   
    flag = ""
    for i in range(len(L)-1):
        if L[i][0] > L[i+1][0]:
            t = (L[i+1][1]-5-L[i][1])/(L[i][0]-L[i+1][0])
            if min_v == -1 or (t < min_v and t >=0) or (t >= 0 and min_v < 0):
                flag="L" 
                min_v =t
                a=i
                b=i+1
    #print "x",min_v
    for i in range(len(R)-1):
        if R[i][0] > R[i+1][0]:
            t = (R[i+1][1]-5-R[i][1])/(R[i][0]-R[i+1][0])
            if min_v == -1 or (t < min_v and t >= 0) or (t >= 0 and min_v < 0):
                flag="R" 
                min_v =t
                a=i
                b=i+1
    #print L,R,min_v,flag,a,b
    if min_v < 0: 
        last_min = 0
        return (-1,last_min)
    elif min_v==0:
        if last_min ==1: # the last time , a collisional point of time is also 0 
            last_min = 0
            return (total,last_min)
        else: 
            last_min = 1
    else:
        last_min =0
        total += min_v
    for i in range(len(L)):
        L[i] = (L[i][0],L[i][0]*min_v+L[i][1])
    for i in range(len(R)):
        R[i] = (R[i][0],R[i][0]*min_v+R[i][1])
    
    #print L,R
    #print "----------------------------------------------------------"    
    if flag == "R":
        x = L[:]
        L = R[:]
        R = x[:]
    stop =0
    if len(R) ==0:
        stop=1
        t = L[:]
        t1 = R[:]
        t.pop(a)
        t1.insert(i+1,L[a])
        rs1,last_min = solve(t,t1,total,last_min)
        
        t = L[:]
        t1 = R[:]
        t.pop(b)
        t1.insert(i+1,L[b])
        rs2,last_min = solve(t,t1,total,last_min)
        if rs1 == -1 or rs2 ==-1: total =-1
        else: total = max(rs1,rs2)
        return (total,last_min)
    rs1 = rs2 = 0
    if L[a][1] + 5 <= R[0][1]:
        stop=1
        t = L[:]
        t1 = R[:]
        t.pop(a)
        t1.insert(0,L[a])
        rs1,last_min = solve(t,t1,total,last_min)
    if L[b][1] + 5 <= R[0][1]:
        stop=1
        t = L[:]
        t1 = R[:]
        t.pop(b)
        t1.insert(0,L[b])
        rs2,last_min = solve(t,t1,total,last_min)
    if stop ==1:
        if rs1 == -1 or rs2 ==-1: total =-1
        else: total = max(rs1,rs2)  
        return (total,last_min)
    for i in range(len(R)):
        rs1 = rs2 = 0
        if i < len(R)-1:
            if L[a][1] + 5 <= R[i+1][1] and R[i][1] + 5 <= L[a][1]:
                stop=1
                t = L[:]
                t1 = R[:]
                t.pop(a)
                t1.insert(i+1,L[a])
                rs1,last_min = solve(t,t1,total,last_min)
            if L[b][1] + 5 <= R[i+1][1] and R[i][1] + 5 <= L[b][1]:
                stop=1
                t = L[:]
                t1 = R[:]
                t.pop(b)
                t1.insert(i+1,L[b])
                rs2,last_min = solve(t,t1,total,last_min)
        else:
            if L[a][1] >= R[i][1]+5:
                stop=1
                t = L[:]
                t1 = R[:]
                t.pop(a)
                t1.insert(i+1,L[a])
                rs1,last_min = solve(t,t1,total,last_min)
            if L[b][1] >= R[i][1]+5:
                stop=1
                t = L[:]
                t1 = R[:]
                t.pop(b)
                t1.insert(i+1,L[b])
                rs2,last_min = solve(t,t1,total,last_min)
        if stop ==1:
            if rs1 == -1 or rs2 ==-1: total =-1
            else: total = max(rs1,rs2)  
            return (total,last_min)
    if stop ==0:
        return (total,last_min)      
    
testcase = int(sys.stdin.readline().strip())
case =1    
for _ in range(testcase):
    n = int(sys.stdin.readline().strip())
    L=[]
    R=[]
    for _ in range(n):
        lane,S,P = sys.stdin.readline().strip().split()
        if lane == "L":
            L.append((float(S),float(P)))
        elif lane == "R":
            R.append((float(S),float(P)))
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[i][1] > L[j][1]:
                t = L[i]
                L[i] = L[j]
                L[j] = t  
    for i in range(len(R)-1):
        for j in range(i+1,len(R)):
            if R[i][1] > R[j][1]:
                t = R[i]
                R[i] = R[j]
                R[j] = t      
    rs,last_min = solve(L,R,0.0,0)        
    if rs ==-1:
        print "Case #%d: Possible" %(case)
    else:
        print "Case #%d: %.5f" %(case,rs)
    case+=1        
            
            
