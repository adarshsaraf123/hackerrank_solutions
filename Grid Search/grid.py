# Enter your code here. Read input from STDIN. Print output to STDOUT
from heapq import heapify, heappop, heappush
T = input()
for _ in xrange(T):
    N = input()
    grid = [sorted(raw_input()) for _ in xrange(N)]
    #for g in grid:
	#	print g
    orderable = 1
    for j in xrange(N):
        i = 0 
        while i < N-1 and grid[i][j] <= grid[i+1][j]:
            i += 1
        if i < N - 1:
			#print i, j
			orderable = 0 
			break
    print orderable*'YES' + (1-orderable)*'NO'