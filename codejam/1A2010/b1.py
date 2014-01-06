import sys
def solve():
	case =1
	test_case  = int(sys.stdin.readline())
	for _ in range(test_case):
		d,insert,m,n = map(int,sys.stdin.readline().split())
		arr = map(int,sys.stdin.readline().split())
		dp=[]
		for i in range(n+1):
			dp.append([])
			dp[i] = [0]*256
		#for i in range(256):
		#	if i in dic:
		#		dp[1][i] = min(abs(arr[0] - i),dp[0][i]+d)
		#		print "for i,j:",1,i,"value:",dp[1][i]
		#	else:
		#		dp[1][i] = abs(arr[0] - i)
		#		print "for i,j:",1,i,"having min at:",arr[0],"value:",dp[1][i]
		for i in range(1,n+1):
			for j in range(256):
				min_v =-1
				anchor =-1
				original =-1
				jj=-1
				for k in range(256):
					if m >0:
						if abs(k-j) > m:
							if abs(k-j) % m !=0:
								cost = dp[i-1][k] + (abs(k-j)/m) * insert + abs(arr[i-1] - j)
							else:
								cost = dp[i-1][k] + ((abs(k-j)/m)-1) * insert + abs(arr[i-1] - j)				
						else:
							cost = dp[i-1][k]+abs(arr[i-1] - j) 
					else:
						#cost = dp[i-1][k] + abs(k-j) + abs(arr[i-1]-j) #wrong because when k moves to j we break the smooth between  
						cost = dp[i-1][j] +abs(arr[i-1]-j) 
					if min_v == -1 or min_v >cost:
						anchor =k
						original = arr[i-1]
						jj = dp[i-1][k]
						min_v = cost
				if min_v == -1 : min_v =0
				#print "for i,j:",i,j,"having min at:",anchor,"original:",original,"previous",jj,"value:",min(min_v,dp[i-1][j]+d) 
				dp[i][j] = min(min_v,dp[i-1][j]+d) 
		#compare = []
		#for i in range(n+1):
		#	print "I:",i,dp[i], n, d,i
		#	compare.append(min(dp[i]))
		#print dp[n]
		print "Case #%d: %d" %(case,min(dp[n]))
		case+=1



solve()
