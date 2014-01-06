import sys
def cal(anchor,num,m,i,k):
	if m==0:
		cost =abs(anchor-num)
		return (cost,anchor)
	else:
		if (abs(anchor-num)-k) % m !=0:
			cost = 	((abs(anchor-num)-k)/m)*i + k
		else:
			cost =  (((abs(anchor-num)-k)/m)-1)*i + k	

	if anchor > num:
		next = num+k
	elif anchor < num:
		next = num - k
	return (cost,next)	
def find_next_step(anchor,cur_num,totalcost,ind,d,m,i,n,arr):
	anchor+=" "+str(cur_num)
	if ind==n-1:
		print anchor
		print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" 
		return totalcost
	if abs(cur_num-arr[ind+1]) <=m:
		t=find_next_step(anchor,arr[ind+1],totalcost,ind+1,d,m,i,n,arr)
		anchor = str(cur_num)
		min_v=t
	else:
		t=find_next_step(anchor,cur_num,totalcost+d,ind+1,d,m,i,n,arr)
		anchor = str(cur_num)	
		min_v=t
		k=0
		while (abs(cur_num-arr[ind+1])-k) >= m:
			cost,next = cal(cur_num,arr[ind+1],m,i,k)
			t=find_next_step(anchor,next,totalcost+cost,ind+1,d,m,i,n,arr)
			anchor = str(cur_num)
			if min_v > t: 
				min_v=t
			k+=1
	return min_v
def find_prev_step(anchor,cur_num,totalcost,ind,d,m,i,n,arr):
	anchor+=" "+str(cur_num)
	if ind==0:
		print anchor
		print "************************************************************************" 
		return totalcost
	if abs(cur_num-arr[ind-1]) <=m:
		t=find_prev_step(anchor,arr[ind-1],totalcost,ind-1,d,m,i,n,arr)
		anchor = str(cur_num)
		min_v=t
	else:
		t=find_prev_step(anchor,cur_num,totalcost+d,ind-1,d,m,i,n,arr)
		anchor = str(cur_num)
		min_v=t
		k=0
		while (abs(cur_num-arr[ind-1])-k) >= m:
			cost,next = cal(cur_num,arr[ind-1],m,i,k)
			t=find_prev_step(anchor,next,totalcost+cost,ind-1,d,m,i,n,arr)
			anchor = str(cur_num)
			if min_v > t: 
				min_v=t
			k+=1
	return min_v
def find(d,i,m,n,arr):
	rs=[]
	for ind in range(n):
		min_1=find_next_step("",arr[ind],0,ind,d,m,i,n,arr)
		#print min_1		
		min_2=find_prev_step("",arr[ind],0,ind,d,m,i,n,arr)
		#print min_2
		rs.append(min_1+min_2)
		print "Total cost",min_1+min_2
		print "-------------------------------------------------------------------"
	return min(rs)	
		
def solution():
	case =1
	test_case  = int(sys.stdin.readline())
	for i in range(test_case):
		d,i,m,n = map(int,sys.stdin.readline().split())
		arr = map(int,sys.stdin.readline().split())
		rs = find(d,i,m,n,arr)
		print "Case #%d: %d" %(case,rs)
		case+=1
solution()
		
		
