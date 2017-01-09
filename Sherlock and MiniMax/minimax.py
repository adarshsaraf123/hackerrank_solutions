import bisect

N = input()
A = map(int, raw_input().split())
P, Q = map(int, raw_input().split())
A.sort()
#print A
A = A[max(0, bisect.bisect_left(A, P) - 1) : min(N, bisect.bisect(A, Q)+1)]
#print A
N = len(A)
diffs = { (A[i+1]+A[i]) / 2 : (A[i+1] - A[i])/2 for i in xrange(N-1)}
if P < A[0]:
    diffs[P] = A[0] - P
if Q > A[-1]:
    diffs[Q] = Q - A[-1]
elif Q > A[-2]:
	diffs[Q] = Q - A[-2]
diffs[A[N-1] + 1] = 1
diffs = sorted(diffs.iteritems(), key = lambda x: (-x[1],x[0]))
#print diffs
for x,y in diffs:
    if x >= P and x <= Q:
        print x
        break

