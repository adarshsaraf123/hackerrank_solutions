# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, raw_input().split())
topics = [raw_input() for _ in xrange(N)]
team_topics = []
for i in xrange(N):
	i_zeroes = [index for index in xrange(M) if topics[i][index] == '0']
	i_count = M - len(i_zeroes)
	#print i, i_zeroes, i_count
	#print i*'\t',
	for j in xrange(i+1, N):
		j_xones = [index for index in i_zeroes if topics[j][index] == '1']
		#print j_xones
		team_topics.append(i_count + len(j_xones))
max_topics_known = max(team_topics)
print max_topics_known
print len(filter(lambda x: x == max_topics_known, team_topics))