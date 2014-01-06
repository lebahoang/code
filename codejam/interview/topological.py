import os
def dfs(root,visited,adj,sort):
    visited[root] = True
    for n in adj[root]:
        if visited[n] == False:
            dfs(n,visited,adj,sort)
    sort.append(root)
def print_topological_sort(visited,adj,nodes,sort):
    for i in nodes:
        if visited[i] == False:
            dfs(i,visited,adj,sort)


nodes = [0,1,2,3,4,5,6,7]
adj = []
adj.append([])
adj.append([])
adj.append([3])
adj.append([1])
adj.append([0,1])
adj.append([0,2])
adj.append([7])
adj.append([])
visited = []
for node in nodes:
    visited.append(False)
sort = []    
print_topological_sort(visited,adj,nodes,sort)
print sort


