# Enter your code here. Read input from STDIN. Print output to STDOUT
N, Q = map(int, raw_input().split())
A = map(int, raw_input().split())
known_results = {}
for q in xrange(Q):
	L, R = map(int, raw_input().split())
	L = L-1
	R = R-1
	#print known_results, L , R
	min_diff = R - L + 1
	L_min = -1
	R_min = -1
	for l, r in known_results:
		diff = abs(L - l) + abs(R - r)
		if diff < min_diff:
			min_diff = diff
			L_min = l
			R_min = r
	#now (L_min, R_min) represents the closest available known value
	if (R - L + 1) < min_diff:
		odd = 0
		for i in xrange(L, R+1):
			odd ^= (A[i] & 1)
	else:
		if L_min == -1:
			odd = 0
			L_min = R + 1
			R_min = R
		else:
			odd = known_results[(L_min, R_min)]
		if L < L_min:
			for i in xrange(L,L_min):
				odd^= (A[i]&1)
				#print A[i],odd
		else:
			for i in xrange(L_min+1, L+1):
				odd ^= (A[i]&1)
		if R < R_min:
			for i in xrange(R,R_min):
				odd^= (A[i]&1)
		else:
			for i in xrange(R_min+1, R+1):
				odd ^= (A[i]&1)
	known_results[(L,R)] = odd
	print (1-odd)*"Even" + odd*"Odd"


