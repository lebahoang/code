import os


def dfs(root,disc,low,parent,visited,adj,time,arti):
    visited[root] = True
    children = 0
    disc[root] = time
    time += 1
    for n in adj[root]:
        if visited[n] == False:
            parent[n] = root
            children += 1
            dfs(n,disc,low,parent,visited,adj,time,arti)
            if low[root] == -1 or low[root] > low[n]:
                low[root] = low[n]
        else:
            if n != parent[root]:
                if low[root] == -1 or low[root] > disc[n]:
                    low[root] = disc[n]
    
    if children >=2 or (children == 1 and (low[root] > disc[root] or low[root] == -1)):
        print "articulation node",root
        arti.append(root)
        
        
        
def print_articulation(nodes,visited,adj):
    arti = []
    disc = [-1 for i in nodes]
    low = [-1 for i in nodes]
    parent = [-1 for i in nodes]
    time = 0
    for i in nodes:
        if visited[i] == False:
            dfs(i,disc,low,parent,visited,adj,time,arti)
    for 
    for i in adj[root]:
            if low[i] == -1:
                print "edge %d--%d is bridge edge" %(root,i)        
            
nodes = [0,1,2,3,4,5]
adj = []
adj.append([1,2])
adj.append([3,4])
adj.append([5])
adj.append([])
adj.append([])
adj.append([])
visited = []
for node in nodes:
    visited.append(False)
    
print_articulation(nodes,visited,adj)

print "---------------"

nodes = [0,1,2,3]
adj = []
adj.append([1,2])
adj.append([0,3,2])
adj.append([0,1])
adj.append([1])
visited = []
for node in nodes:
    visited.append(False)
    
print_articulation(nodes,visited,adj)
