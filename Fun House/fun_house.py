# Enter your code here. Read input from STDIN. Print output to STDOUT
W, L = map(int, raw_input().split())
c = 0
while W != 0 and L != 0:
	c += 1
	room = [raw_input() for _ in range(L)]
	
	#locate the entry
	i = 0
	c_i = 0
	j = 0
	c_j = 1
	found = False
	while not found:
		if room[i][j] == '*':
			found = True
		if i == L-1:
			if j == W-1:
				c_i = 0
				c_j = -1
			elif j == 0:
				c_i = -1
				c_j = 0
		elif i == 0 and j == W-1:
			c_i = 1
			c_j =  0
		i += c_i
		j += c_j
	
	i = i - c_i
	j = j - c_j
	
	if j == 0:
		#towards right
		c_i = 0
		c_j = 1
	elif j == W-1:
		#towards right
		c_i = 0
		c_j = -1
	elif i == 0:
		#towards bottom
		c_i = 1
		c_j = 0
	elif j == L-1:
		#towards top
		c_i = -1
		c_j = 0
	
	i += c_i
	j += c_j
	while i != 0 and i != L-1 and j != 0 and j != W-1:
		if room[i][j] == '/':
			if c_i == 0:
				if c_j == 1:
					c_i = -1
					c_j = 0
				elif c_j == -1:
					c_i = 1
					c_j = 0
			else:
				if c_i == 1:
					c_i = 0
					c_j = -1
				elif c_i == -1:
					c_i = 0
					c_j = 1
		elif room[i][j] == '\\':
			if c_i == 0:
				if c_j == 1:
					c_i = 1
					c_j = 0
				elif c_j == -1:
					c_i = -1
					c_j = 0
			else:
				if c_i == 1:
					c_i = 0
					c_j = 1
				elif c_i == -1:
					c_i = 0
					c_j = -1
		i += c_i
		j += c_j
	
	room[i] = room[i][:j] + '&' + room[i][j+1:]
	# print the output
	print "HOUSE", c
	for r in room:
		print r
	W, L = map(int, raw_input().split())