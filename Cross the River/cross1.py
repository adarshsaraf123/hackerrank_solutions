N, H, dH, dW = map(int, raw_input().split())
rocks = [map(int, raw_input().split()) for _ in xrange(N)]
Y = 0
X = 1
S = 2
neginf = -1 * float('inf')
rocks.sort(key = lambda l: (l[Y],l[X]))
#print rocks
scores = [rocks[i][S] if H - rocks[i][Y] <= dH else neginf for i in xrange(N) ]

i = N - 2
while i > -1:
	#now all the rocks concerned are not directly connected to the opposite shore and thus we try to find the max score for these based on the points accesible from this rock
	j = len(scores)
	while j > i:
		
	print scores
	scores[i] = max(scores[i], max( scores[j] + rocks[i][S] for j in xrange(i+1, N) if ( (rocks[j][Y] > rocks[i][Y]) and (rocks[j][Y] - rocks[i][Y] <= dH) and (abs(rocks[i][X] - rocks[j][X]) <= dW) ) ) )
	i -= 1

max_score = max(scores[i] for i in xrange(N) if rocks[i][Y] <= dH)

print max_score