import sys
import os
import pprint
def calculate_coin(i,indexs,cells):
    #print indexs[i]-1,
    #print cells
    j = i
    while j>=0:
        if cells[indexs[j]-1] == -1:
            coin = (indexs[i]-1)-(indexs[j]-1)-1
            break
        j -= 1 
    if j == -1:
        coin = indexs[i]-1
    j = i
    while j<len(indexs):
        if cells[indexs[j]-1] == -1:
            coin += (indexs[j]-1)-(indexs[i]-1)-1
            break
        j += 1
    if j == len(indexs):
        coin += len(cells)-(indexs[i]-1)-1
    return coin
    


def solve(p,q,indexs,prisoner):
    cells = [1 for i in xrange(p)]
    dp = []
    init = []
    for i in indexs:
        new_cells = cells[:]
        new_cells[i-1] = -1
        left = indexs[:]
        left.remove(i)
        coin = p-1 
        a = (new_cells,left,coin)
        init.append(a)
    dp.append(init)
    for _ in xrange(1,q):
        last = dp[-1]
        new = []
        min = -1
        print last
        for _cells,left,coin in last:
            flag = 0
            for l in left:
                ex_coin = calculate_coin(prisoner[l],indexs,_cells)
                if min == -1 or min > coin+ex_coin:
                    min = coin+ex_coin
                    del new[:]
                    flag = 1
                elif min == coin+ex_coin:
                    flag = 1
                if flag == 1:
                    flag = 0
                    new_cells = _cells[:]
                    new_cells[l-1] = -1
                    new_left = left[:]
                    new_left.remove(l)
                    coin = min
                    a = (new_cells,new_left,coin)
                    new.append(a)
        dp.append(new)
        
    pprint.pprint(dp)



T = int(sys.stdin.readline())
case = 1
for _ in xrange(T):
    P,Q = map(int,sys.stdin.readline().split(" "))
    indexs = map(int,sys.stdin.readline().split(" "))
    prisoner = {}
    for i in xrange(Q):
        prisoner[indexs[i]] = i
    rs = solve(P,Q,indexs,prisoner)
    print "Case #%d: %d" %(case,1)
    case += 1
