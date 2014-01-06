import sys

def do(box,toy,total,store):
    #print box
    #print toy
    #print "---------------------------------------------"
   
    if len(box)==0 or len(toy)==0:
        #print str(box)+str(toy) , 0
        x=(len(box),len(toy))
        if len(box)>0: x+= (box[0][0],box[0][1])
        if len(toy)>0: x+=(toy[0][0],toy[0][1])
        store[x]=0
        return (store,0)
    stage_product =0 
    if box[0][1] == toy[0][1]:
        t=min(box[0][0],toy[0][0])
        total +=t
        box_t = box[:]
        toy_t = toy[:]
        if box[0][0] > t:
            box[0] = (box[0][0]-t,box[0][1])
        else:
            box.remove(box[0])
        if toy[0][0] >t:
            toy[0] = (toy[0][0] - t,toy[0][1])
        else:
            toy.remove(toy[0])
        before = total
        x=()
        if len(box)>0: x+= (box[0][0],box[0][1])
        if len(toy)>0: x+=(toy[0][0],toy[0][1])
        v = store.get( (len(box),len(toy)) + x )
        if  v !=None:
            #print "y",before,str(box)+str(toy),store[str(box)+str(toy)]
            t1 = v
        else: 
            store,s_p = do(box,toy,total,store) 
            t1 =  s_p
        stage_product = t+t1
        #print str(box_t)+str(toy_t) , stage_product
        store[len(box_t),len(toy_t),box_t[0][0],box_t[0][1],toy_t[0][0],toy_t[0][1]] = stage_product
        total =before
    else:
        before = total
        #print "1"
        box1 = box[1:]
        toy1 = toy[:]
        x=()
        if len(box1)>0: x+= (box1[0][0],box1[0][1])
        if len(toy1)>0: x+=(toy1[0][0],toy1[0][1])
        v= store.get( (len(box1),len(toy1)) + x )
        if v !=None:
            #print "y",before,str(box1)+str(toy1),store[str(box1)+str(toy1)]
            t1 = v
        else: 
            store,s_p = do(box1,toy1,total,store)
            t1 = s_p
        total = before
        #print "2"
        box1 = box[:]
        toy1 = toy[1:]
        x=()
        if len(box1)>0: x+= (box1[0][0],box1[0][1])
        if len(toy1)>0: x+=(toy1[0][0],toy1[0][1])
        v = store.get((len(box1),len(toy1)) + x )
        if v !=None:
            #print "y",before,store[str(box1)+str(toy1)]
            t2 =v
        else: 
            store,s_p = do(box1,toy1,total,store)
            t2 = s_p
        total =before
        #print "3"
        box1 =box[1:]
        toy1 = toy[1:]
        x=()
        if len(box1)>0: x+= (box1[0][0],box1[0][1])
        if len(toy1)>0: x+=(toy1[0][0],toy1[0][1])
        v=store.get( (len(box1),len(toy1)) + x )
        if v !=None:
            #print "y",before,store[str(box1)+str(toy1)]
            t3 = v
        else: 
            store,s_p = do(box1,toy1,total,store)
            t3 = s_p
        stage_product = max(t1,t2,t3)
        #print str(box)+str(toy) , stage_product
        store[len(box),len(toy),box[0][0],box[0][1],toy[0][0],toy[0][1]]  = stage_product
        
    #collect.append(total + stage_product)
    return (store,stage_product)

def solve():
    testcase = int(sys.stdin.readline())
    case =1
    for _ in range(testcase):
        box=[]
        toy=[]
        N,M = map(int,sys.stdin.readline().split())
        l1 = map(int,sys.stdin.readline().split())
        l2 = map(int,sys.stdin.readline().split())
        for i in range(0,len(l1),2):
            box.append((l1[i],l1[i+1]))
        for i in range(0,len(l2),2):
            toy.append((l2[i],l2[i+1]))
        rs = (len(box),len(toy),box[0][0],box[0][1],toy[0][0],toy[0][1])
        store = {}
        total =0
        store,total = do(box,toy,total,store)
        #print store
        print "Case #%d: %d" %(case,store[rs])
        case+=1
        
solve()
