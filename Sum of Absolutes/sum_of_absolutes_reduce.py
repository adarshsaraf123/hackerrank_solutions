# Enter your code here. Read input from STDIN. Print output to STDOUT
func = lambda x,y: x ^ (y&1)
N, Q = map(int, raw_input().split())
A = map(int, raw_input().split())
for q in xrange(Q):
	L, R = map(int, raw_input().split())
	odd = reduce(func, [0]+A[L-1:R])
	print (1-odd)*"Even" + odd*"Odd"


