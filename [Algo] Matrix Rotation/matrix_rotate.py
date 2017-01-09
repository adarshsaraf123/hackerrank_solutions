def get_loop_indices(m):
	i = m
	loop_indices = [(m,m)]
	j = m+1
	while( j < (N-m)):	# top line
		loop_indices.append((i,j))
		j += 1
	j -= 1
	i += 1
	while(i<(M-m)): 		# right line
		loop_indices.append((i,j))
		i+=1
	i -= 1
	j -= 1
	while(j>=m):			# bottom line
		loop_indices.append((i,j))
		j -= 1
	j += 1
	i -= 1
	while(i>m):			# left line
		loop_indices.append((i,j))
		i -= 1
	i +=1 
	return loop_indices

M, N, R = map(int, raw_input().split())
A = []
for m in xrange(M):
	A.append(map(int, raw_input().split()))
upper_m = min(M,N) / 2
for m in xrange(upper_m):
	loop_indices = get_loop_indices(m)
	# loop_indices now has the mth loop in the given matrix
	n = len(loop_indices)
	r = R % n
	if r == 0: # to avoid the cases when no rotation is required
		continue
	
	temp = [A[index[0]][index[1]] for index in loop_indices[:r]]
	i = 0
	while i < n - r:
		A[loop_indices[i][0]][loop_indices[i][1]] = A[loop_indices[i+r][0]][loop_indices[i+r][1]]
		i += 1
	k = 0
	while k < r:
		A[loop_indices[i+k][0]][loop_indices[i+k][1]] = temp[k]
		k += 1 

#print the rotated matrix
for i in xrange(M):
	for j in xrange(N):
		print A[i][j],
	print 