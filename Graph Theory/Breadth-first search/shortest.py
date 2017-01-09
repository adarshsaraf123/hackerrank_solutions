# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(1500)
def update_matrix(current_node):
	for i in xrange(N):
		if i != current_node and i!= S and adjacency_matrix[current_node][i] != -1: #node i is reachable from the current node and is different from the current node
				new_dist = adjacency_matrix[S][current_node] + adjacency_matrix[current_node][i] #if i reach node i through current_node
				if adjacency_matrix[S][i] == -1: #if so far node i was not reachable from S
					adjacency_matrix[S][i] = new_dist
				else:
					adjacency_matrix[S][i] = min(adjacency_matrix[S][i], new_dist)
				update_matrix(i)
				

T = input()
for t in xrange(T):
	N, M = map(int, raw_input().split())
	adjacency_matrix = [None]*N
	for i in xrange(N):
		adjacency_matrix[i] = [-1]*i + [0] + [-1]*(N-i-1)
	for _ in xrange(M):
		x, y = map(int, raw_input().split())
		adjacency_matrix[x-1][y-1] = 1
	S = input()
	S = S-1
	print adjacency_matrix
	update_matrix(S)
	for i in adjacency_matrix[S]:
		if i == 0:
			continue
		elif i == -1:
			print -1,
			continue
		print i*6,
	print