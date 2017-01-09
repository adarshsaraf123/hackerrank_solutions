# Enter your code here. Read input from STDIN. Print output to STDOUT
from heapq import heappush, heappop

N, M = map(int, raw_input().split())
edges = [map(int, raw_input().split()) for _ in xrange(M)]
neighbours = {vertex: [] for vertex in xrange(1, N+1) }
for u, v, c in edges:
    neighbours[u].append( (v, c) )
    neighbours[v].append( (u, c) ) 

dist1 = {vertex:None for vertex in xrange(1,N+1)}
q = [(0, 1)]
while True:
	min_cost, u = heappop(q)
	if dist1[u] is None:
		dist1[u] = min_cost
		if u == N:
			break
		#vertices_found += 1
		for v, right_cost in neighbours[u]:
			if dist1[v] is None:
				heappush(q, (min_cost + right_cost, v))
del dist1[1]
max_dist = dist1[N] - 1
dist1 = {vertex: dist for (vertex, dist) in dist1.iteritems() if dist is not None and dist < max_dist}

distN = {vertex:None for vertex in xrange(1,N+1)}
q = [(0, N)]
while True:
	min_cost, u = heappop(q)
	if distN[u] is None:
		if min_cost >= max_dist:
			break
		distN[u] = min_cost
		for v, right_cost in neighbours[u]:
			if distN[v] is None:
				heappush(q, (min_cost + right_cost, v))
del distN[N]
distN = {vertex: dist for (vertex, dist) in distN.iteritems() if dist is not None}

print dist1, distN
roads = max_dist
#print roads
roads += sum(max_dist - d for d in dist1.itervalues())
#print roads
roads += sum(max_dist - d for d in distN.itervalues())
#print roads
roads += sum(max_dist - lcost - rcost for (u, lcost) in dist1.iteritems() for (v, rcost) in distN.iteritems() if u != v and lcost + rcost < max_dist)
#print [max_dist - lcost - rcost for (u, lcost) in dist1.iteritems() for (v, rcost) in distN.iteritems() if u != v and lcost + rcost < max_dist]

print roads