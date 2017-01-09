# Enter your code here. Read input from STDIN. Print output to STDOUT
def djikstra(source):
    global neighbours
    dist = {vertex: inf for vertex in xrange(1, N+1)}
    dist[source] = 0 
    q = range(1,N + 1)
    #print q
    found = {vertex:0 for vertex in xrange(1,N+1)}
    iter = 0
    while iter < N:
        u = min(q, key = lambda vertex: dist[vertex]+M*found[vertex])
        #q.remove(u)
        #print iter, u
        found[u] = 1
        for v, c in neighbours[u]:
            if not found[v]:
                dist[v] = min(dist[v], dist[u] + c)
        iter += 1
        #print dist
    return dist

from collections import deque

inf = float('inf')
N, M = map(int, raw_input().split())
edges = [map(int, raw_input().split()) for _ in xrange(M)]
#print edges
neighbours = {vertex: [] for vertex in xrange(1, N+1) }
max_cost = 0
for u, v, c in edges:
    neighbours[u].append( (v, c) )
    neighbours[v].append( (u, c) )
    if c > max_cost:
        max_cost = c
#print neighbours
M = max_cost*2
roads = 0 
dist1 = djikstra(1)
distN = djikstra(N)
print dist1, distN
max_dist = dist1[N] - 1
roads += max_dist
for i in xrange(2, N):
	left_cost = dist1[i]
	right_cost = distN[i]
	#costi = min(left_cost, right_cost)
	#print "left", left_cost
	if left_cost < max_dist:
		roads += max_dist - left_cost
	if right_cost < max_dist:
		roads += max_dist - right_cost
	if left_cost < max_dist:
		for j in xrange(2,N):
			if j == i:
				continue
			right_cost = distN[j]
			#print "right", right_cost
			total_cost = left_cost + right_cost
			if total_cost < max_dist:
				roads += max_dist - total_cost
print roads