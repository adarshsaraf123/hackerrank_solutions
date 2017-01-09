import sys


K,N = raw_input().strip().split(' ')
K,N = [int(K),int(N)]
R = map(lambda x: int(x)*int(x),raw_input().strip().split(' '))
dist = [sum(map(lambda x: int(x)*int(x), raw_input().split())) for _ in range(N)]
dist.sort()
#print R, dist
i = K-1
s = 0
for d in dist:
	print d
	while d > R[i] and i > -1:
		i -= 1
	if i == -1:
		break
	s += (i+1)
print s
