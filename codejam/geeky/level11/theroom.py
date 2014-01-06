import sys
def merge_value_to_list(list_vl, value):
    last = 1
    for i in xrange(len(list_vl)):
        if value <= it:
            list_vl.insert(i,value)
            last = 0
            break
    if last == 1:
        list_vl.append(value)
    return list_vl
             


def get_combination(length,number,present):
    prototype = ['-1' for i in xrange(length)]
    cb = []
    state = []
    for i in xrange(length):
        t = prototype[:]
        t[i] = number
        state.append((t,i))
    cb.append(state)
    for i in xrange(2,present+1):
        last_state = cb[-1]
        new_state = []
        for it,start in last_state:
            for j in xrange(start+1,length):
                t = it[:]
                t[j] = number
                new_state.append((t,j))
        cb.append(new_state)
    return cb
                                   

def get_number(rs,bt,index,gr,count,length):
    it = bt[index]
    for i in xrange(it[1]+1):
        gr.append((it[0],i))
        if count + i == length and index == len(bt)-1:
            t = gr[:]
            gr.remove((it[0],i))
            return t
        elif index < len(bt)-1:
            t = get_number(rs,bt,index+1,gr,count+i,length)
            if t != None:
                rs.append(t)
        gr.remove((it[0],i))     
    return None

def make_a_group_combination(cb,group,length):
    rs = []
    for number,present in group:
        if present == 0:
            continue
        new = cb[number][present-1]
        if not rs:
            for x,start in new:
                rs.append(x)
        else:
            new_rs = []
            for a in rs:
                for b,start in new:
                    temp = []
                    flag = 0
                    for x,y in zip(a,b):
                        if (x != '-1' and y != '-1'):
                            flag = 1
                            break
                        else:
                            if x != '-1':
                                temp.append(x)
                            elif y != '-1':
                                temp.append(y)
                            else:
                                temp.append('-1')
                    if flag == 0:
                        new_rs.append(temp)
            rs = new_rs[:]  
    return rs        
def make_combination(cb,groups,length):
    rs = []
    for group in groups:
        a = make_a_group_combination(cb,group,length)
        rs.extend(a)
    return rs        
    
buttons = ["1,2,3", "4,5,6", "7,8,9", "*,0,#"]
bt = []
#file = open(sys.argv[1])
length = int(sys.stdin.readline())#int(file.readline()) #int(sys.stdin.readline())
for i in xrange(4):
    button = buttons[i].split(",")
    bmap = map(int,sys.stdin.readline().split())#file.readline().split())#sys.stdin.readline().split())
    for j in xrange(len(bmap)):
        if bmap[j] > 0:
            bt.append((button[j],bmap[j]))

cbs = {}
for number,present in bt:
    cb = get_combination(length,number,present)   
    cbs[number] = cb        
groups = []
get_number(groups,bt,0,[],0,length)

#print "Done stage1"
rs = make_combination(cbs,groups,length)
#print len(rs)
#print rs
list_value = []
for a in rs:
    list_value.append(" ".join(a))
list_value.sort()
#print list_value
print "\n".join(list_value)
    

