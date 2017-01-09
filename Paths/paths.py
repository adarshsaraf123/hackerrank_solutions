T = input()
for t in xrange(T):
	possible = False
	N = input()
	Maze = []
	for i in xrange(N):
		Maze.append(map(int,raw_input().split()))
		
	A = [[False for x in range(N)] for x in range(N)] 
	print A
	#A[0][0] = True
	#print Maze
	#print A

	for x in xrange(N):
		for y in xrange(N):
			#print x, y, Maze[x][y],
			#raw_input()
			if Maze[x][y] == 1:
				if x - 1 >= 0:
					A[x][y] = A[x][y] or A[x-1][y]
				if y - 1 >= 0:
					A[x][y] = A[x][y] or A[x][y-1]
			#print A[x][y]
			
	print A
	possible = A[N-1][N-1]
	if possible:
		print "POSSIBLE"
	else:
		print "NOT POSSIBLE"
