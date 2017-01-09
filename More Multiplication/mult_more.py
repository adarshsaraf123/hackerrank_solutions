A, B = raw_input().split()
while A != '0' and B != '0':
	result = int(A) * int(B)
	result = str(result)
	#print result
	d_a = [int(c) for c in A]
	d_b = [int(c) for c in B]
	#print d_a, d_b
	cols = len(d_a)
	rows = len(d_b)
	c = (cols + 1)*3 + 2 + cols
	r = (rows - 1)*4 + 5 + 4
	output = [[' ' for _ in range(c)] for _ in range(r)]
	
	# ////////////// initialize the outer box /////////////////////
	output[0][0] = output[0][c-1] = output[r-1][0] = output[r-1][c-1] = '+'
	for i in range(1,r-1):
		output[i][0] = output[i][c-1] = '|'
	for j in range(1,c-1):
		output[0][j] = output[r-1][j] = '-'
	
	# ////////////// add the operands /////////////////////////////
	# first
	i = 4
	for x in range(cols):
		output[1][i] = str(d_a[x])
		i += 4
	#second
	j = 4
	for y in range(rows):
		output[j][c-2] = str(d_b[y])
		j += 4
	
	# ////////////// create the inner matrix //////////////////////
	# >> top row
	for j in range(2,c-2):
		output[2][j] = ('+' if (j % 4 == 2) else '-')
	
	j = 2
	for y in range(cols+1):
		for i in range(3,r-2):
			output[i][j] = ('+' if (i % 4 == 2) else '|')
		j += 4
		
	i = 6
	for x in range(rows):
		for j in range(3,c-3):
			if j % 4 != 2:
				output[i][j] = '-'
		i += 4
	
	for x in range(rows):
		for y in range(cols):
			i = x*4 + 3
			j = y*4 + 3
			output[i][j+2] = '/'
			output[i+1][j+1] = '/'
			output[i+2][j] = '/'
			d = d_b[x]*d_a[y]
			d = str(d).zfill(2)
			output[i][j] = d[0]
			output[i+2][j+2] = d[1]
	
	# ////////////// add the result elements ////////////////////// 
	n = len(result)
	j = c - 6
	i = r - 2
	for y in range(cols):
		output[r-2][j] = result[n-y-1]
		output[r-2][j-2] = '/'
		j -= 4
	if n > cols:
		i = r - 4
		for x in range(n - cols):
			output[i][1] = result[n-1 - cols - x]
			output[i-2][1] = '/'
			i -= 4
		output[i+2][1] = ' '
	else:
		output[r-2][1] = ' '
	# ////////////// printing the output //////////////////////////
	for row in output:
		print "".join(row)
    # ////////////// new data /////////////////////////////////////
	A, B = raw_input().split()