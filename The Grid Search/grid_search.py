# Enter your code here. Read input from STDIN. Print output to STDOUT
T = input()
for t in xrange(T):
	R, C = map(int,raw_input().split())
	grid = []
	for _ in xrange(R):
		grid.append(raw_input())
	r, c = map(int,raw_input().split())
	pattern = []
	for _ in xrange(r):
		pattern.append(raw_input())
	#print grid
	#print pattern
	found = False
	for n in xrange(C-c+1):
		for m in xrange(R-r+1):
			k = 0
			match = True
			while(k < r):
				for j in xrange(c):
					if pattern[k][j] != grid[m+k][n+j]:
						match = False
						break
				if not match:
					break
				k += 1
			if match:
				found = True
				#print m, n
				break
		if found:
			break
	if found:
		print "YES"
	else:
		print "NO"