import sys
cost_memory = {}
P = []
def min_cost_position(roses_low, sprinkler_low, e, N, M, S, first = False, level = 1):
	if roses_low > N: # implies all the roses have been watered
		return []
	
	if sprinkler_low == M: # no more sprinklers available to water the roses
		return None
	
	#print level*"\t", "roses_low =", roses_low, "position =", P[sprinkler_low]
	
	if (P[sprinkler_low] - roses_low) > e: #some of the roses will remain dry if this condition holds; so solution not possible
		return None
	
	global cost_memory
	if first:
		cost_memory = {}

	if (roses_low, sprinkler_low) in cost_memory:
		return cost_memory[(roses_low, sprinkler_low)]
	
	#print level*"\t", "included"
	included = min_cost_position(P[sprinkler_low] + e + 1, sprinkler_low + 1, e, N, M, S, level = level + 1)
	
	#print level*"\t", "excluded"
	excluded = min_cost_position(roses_low, sprinkler_low + 1, e, N, M, S, level = level + 1)
	
	if included != None:
		included = [P[sprinkler_low]] + included
		
		if excluded != None:
			if len(included) > len(excluded):
				cost_memory[(roses_low, sprinkler_low)] = excluded
				#print cost_memory
				return excluded
	
		cost_memory[(roses_low, sprinkler_low)] = included
		#print cost_memory
		return included
	
	cost_memory[(roses_low, sprinkler_low)] = excluded
	#print cost_memory
	return excluded

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
		local_sol = min_cost_position(1,0,e, N, M, S, first = True, level = 1)
		#print cost_memory
		if local_sol!= None:
			local_cost = (len(local_sol) * S) + (e*Q)
			if local_cost < optimal_cost:
				optimal_cost = local_cost
				optimal_positions = local_sol
				optimal_E = e
	print len(optimal_positions), optimal_E
	for p in optimal_positions:
		print p,
	print 