mod_value = 10**9 + 7
count_memoized = {}
def count_possibilities(current_soldier, current_skills):
	if current_skills == R:
		temp = count_memoized[(current_soldier, current_skills)] = pow(2,N-current_soldier, mod_value)
		return temp
	if current_soldier == N:
		return 0
	if (current_soldier, current_skills) in count_memoized:
		return count_memoized[(current_soldier,current_skills)]
	count = 0
	if S[current_soldier] & (~R) == 0:
		count += count_possibilities(current_soldier + 1, current_skills | S[current_soldier])
	count = ( count + count_possibilities(current_soldier + 1, current_skills) ) % mod_value
	#print current_soldier, current_skills, count
	count_memoized[(current_soldier, current_skills)] = count
	return count

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
	print count_possibilities(0,0)
