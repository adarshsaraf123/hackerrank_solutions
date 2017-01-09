import sys
sys.setrecursionlimit(3500)
mod_value = 10**9 + 7
mod_add = lambda x,y : (x + y) % mod_value
N, M = map(int, raw_input().split())
S = []
for n in xrange(N):
	S.append( int(raw_input(), 2) )
R = int(raw_input(), 2)
S = filter(lambda x: x & (~R) == 0, S)
N = len(S)
if N == 0: #if there are no soldiers left then there can be no possible solutions at all
	print 0
else:
	count_memoized = {}
	stack = []
	stack.append((0,0))
	count = 0 
	while(len(stack)!=0):
		#print stack
		current_soldier, current_skills = stack.pop()
		if current_skills == R:
			temp = count_memoized[(current_soldier, current_skills)] = pow(2,N-current_soldier, mod_value)
			count = mod_add(count, temp)
		elif current_soldier == N:
			continue
		elif (current_soldier, current_skills) in count_memoized:
			count = mod_add(count,count_memoized[(current_soldier,current_skills)])
		else:
			stack.append((current_soldier + 1, current_skills | S[current_soldier]))
			stack.append((current_soldier + 1, current_skills))
			#print current_soldier, current_skills, count
	print count