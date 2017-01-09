N, H, dH, dW = map(int, raw_input().split())
rocks = [map(int, raw_input().split()) for _ in xrange(N)]
Y = 0
X = 1
S = 2
inf = float('inf')
rocks.sort(key = lambda l: (l[Y],l[X]))
#print rocks
scores = [-1*inf for _ in xrange(N)]
scores[N-1] = rocks[N-1][S]
for i in xrange(N-1, -1, -1):
	if H - rocks[i][Y] > dH:
		break
	scores[i] = rocks[i][S]
#print scores 
for i in xrange(N-1, -1, -1):
	for j in xrange(i-1, -1, -1):
		#print i, j, scores[j], scores[i], rocks[j][S]
		if rocks[i][Y] - rocks[j][Y] <= dH and rocks[i][Y] > rocks[j][Y]:
			if abs(rocks[i][X] - rocks[j][X]) > dH:
				continue
			scores[j] = max(scores[j], scores[i] + rocks[j][S])
	#print scores, rocks
max_score = scores[0]
for i in xrange(1,N):
	if rocks[i][Y] > dH:
		break
	if scores[i] > max_score:
		max_score = scores[i]
print max_score