import os
import sys

def get_min_node(times,nodes):
    min_vl = -1.0
    rs = None
    for node in nodes:
        if times[node] != -1.0 and min_vl > times[node] or min_vl == -1:
            min_vl = times[node]
            rs = node
    return rs 

def calculate_going_time(spent_time,C,F,H,src,dest):
    going = 0
    if F[dest[0]][dest[1]] <= C[dest[0]][dest[1]] - 50.0 and F[src[0]][src[1]] <= C[dest[0]][dest[1]] - 50.0 and F[dest[0]][dest[1]] <= C[src[0]][src[1]] - 50.0: # going room must be passable
        water_level = H - 10.0*spent_time
        if water_level <= C[dest[0]][dest[1]] - 50.0:
            if water_level - F[src[0]][src[1]] >= 20.0:
                if water_level != H:
                    going += 1.0
            else:
                if water_level != H:
                    going += 10.0
        else:
            # calculate waiting time
            new_water_level = C[dest[0]][dest[1]] - 50.0
            need_wait_distance = water_level - new_water_level
            time = need_wait_distance/10.0
            if new_water_level - F[src[0]][src[1]] >= 20.0: 
                going += 1.0
            else:
                going += 10.0
            going += time
    else:
        # can not enter
        going = -1
    #print src,dest,going,spent_time
    return going+spent_time if going != -1 else -1.0  
                
            
        
    
      
def solve(nodes,visited,times,adj,C,F,H,stop,down_rate = 10):
    #print adj
    while nodes:
        node = get_min_node(times,visited)
        if node != None:
            visited[node] = 1
            #print node
            nodes.remove(node)
            for neighbor in adj[node]:
                adj[neighbor].remove(node)
                going_time = calculate_going_time(times[node],C,F,H,node,neighbor)
                if going_time != -1 and times[neighbor] > going_time or times[neighbor] == -1.0:
                    times[neighbor] = going_time
        else:
            return times[stop]
    return times[stop]                 




testcase = int(sys.stdin.readline().strip())
case = 1
for _ in xrange(testcase):
    times = {}
    visited = {}
    nodes = []
    adj = {}
    H,N,M = map(int,sys.stdin.readline().strip().split())
    C = [[] for _ in xrange(N)]
    F = [[] for _ in xrange(N)]
    
    for i in xrange(N):
        for j in xrange(M):
            times[(i,j)] = -1.0
            nodes.append((i,j))
            visited[(i,j)] = 0  
    times[(0,0)] = 0.0 # time to travel from (0,0) to x position   
    
    for i in xrange(N):
        col = map(int,sys.stdin.readline().strip().split())
        for j in xrange(len(col)):
            C[i].append(col[j])
    for i in xrange(N):
        col = map(int,sys.stdin.readline().strip().split())
        for j in xrange(len(col)):
            F[i].append(col[j])
       
    a = []
    b = []
    for i in xrange(N):
        if i == 0:
            a = [1]    
        elif i == N-1:
            a = [-1]
        else:
            a = [-1,1]
        for j in xrange(M):    
            if j == 0:
                b = [1]    
            elif j == M-1:
                b = [-1]
            else:
                b = [1,-1]
                
            for x in a:
                if i+x <= N-1:
                    if (i,j) in adj:
                        adj[(i,j)].append((i+x,j))
                    else:
                        adj[(i,j)] = [(i+x,j)]
            for y in b:
                if j+y <= M-1:
                    if (i,j) in adj:
                        adj[(i,j)].append((i,j+y))
                    else:
                        adj[(i,j)] = [(i,j+y)]
    rs = solve(nodes,visited,times,adj,C,F,H,(N-1,M-1))                       
    print "Case #%d: %.6f" %(case,rs)
    case += 1
            
        
