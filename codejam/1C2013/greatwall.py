import sys

#def solve(attacks,wall):


def cmp_func(a,b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    return 0
T = int(sys.stdin.readline().strip())
for _ in xrange(T):
    attacks = []
    n_tribes = int(sys.stdin.readline().strip())
    for _ in xrange(n_tribes):
        d,n,w,e,s,day_interval,distance,s_change = map(int,sys.stdin.readline().strip().split())
        for i in xrange(n):
            attacks.append( (d+day_interval*i,s+s_change*i,[w+distance*i,e+distance*i]) )
    
    
    #build wall
    wall = {}
    for i in xrange(-199,201):
        wall[(i-1,i)] = 0        
    attacks = sorted(attacks,cmp=cmp_func)
    print attacks
