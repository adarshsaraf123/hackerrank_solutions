# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
T = input()
for t in xrange(T):
	N, M = map(int, raw_input().split())
	adjacency_list = [[] for _ in xrange(N)]
	for _ in xrange(M):
		x, y = map(int, raw_input().split())
		adjacency_list[x-1].append(y-1)
		adjacency_list[y-1].append(x-1)
	S = input() - 1
	shortest_dist = [-1]*N
	color = [0]*N
	
	Q = deque([])
	Q.append(S)
	shortest_dist[S] = 0
	color[S] = 1
	while len(Q)!=0:
		current = Q.popleft()
		for i in adjacency_list[current]:
			if not color[i]:
				shortest_dist[i] = shortest_dist[current] + 1
				color[i] = 1
				Q.append(i)
	
	for i in xrange(N):
		if i == S:
			continue
		if shortest_dist[i] == -1:
			print -1,
		else:
			print 6*shortest_dist[i],
	print