mod_value = 10**9 + 7
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
	A = [0] * (2**N - 1)
	for i in xrange(N-1,-1,-1):
		A[C|]
