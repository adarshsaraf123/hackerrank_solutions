import sys
def min_cost_position(roses_low, P, e, N, M, S):
	#print "\t", "roses_low =", roses_low, "positions =", P
	if roses_low > N: # implies all the roses have been watered
		return (0, [])
	if P == []: # no more sprinklers available to water the roses
		return None
	if (P[0] - roses_low) > e: #some of the roses will remain dry if this condition holds
		return None
	included = min_cost_position(P[0] + e + 1, P[1:], e, N, M, S)
	excluded = min_cost_position(roses_low, P[1:], e, N, M, S)
	if excluded != None:
		if included != None:
			if (S+included[0]) < excluded[0]:
				return (S+included[0], [P[0]] + included[1])
			else:
				return excluded
		else:
			return excluded
	elif included != None:
		return (S+included[0], [P[0]] + included[1])
	else:
		return None

T = input()
for t in xrange(T):
	N, M, S, Q = map(int, raw_input().split())
	P = map(int, raw_input().split())
	E_min = max([ (P[i+1] - P[i]) / 2 for i in xrange(M-1) ] + [P[0] - 1, N - P[M-1]])
	E_max = max(P[0] -1, N - P[0], P[M-1] - 1, N - P[M-1])
	optimal_cost = sys.maxint
	optimal_positions = []
	optimal_E = -1
	for e in xrange(E_min, E_max + 1):
		#print e
		local_sol = min_cost_position(1,P,e, N, M, S)
		if local_sol!= None:
			local_cost = local_sol[0] + e*Q
			if local_cost < optimal_cost:
				optimal_cost = local_cost
				optimal_positions = local_sol[1]
				optimal_E = e
	print len(optimal_positions), optimal_E
	for p in optimal_positions:
		print p,
	print 