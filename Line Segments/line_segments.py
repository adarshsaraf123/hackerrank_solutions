from operator import itemgetter

covers = lambda l1,l2: True if (l2[0] >= l1[0] and l2[1] <= l1[1]) else False

N = input()
lines = []
for i in xrange(N):
    A,B = map(int,raw_input().split())
    lines.append((A,B))
count = N
lines.sort(key = lambda l: (l[0], -l[1]))
print lines
unseen_lines = lines[1:]
accepted_lines = [lines[0]]
count_covering = 0
count_covered_by = 0

for line in lines[1:]:
	count_covering = 0
	count_covered_by = 0
	unseen_lines.remove(line)
	
	for l in accepted_lines[::-1]:
		if covers(l,line):
			count_covered_by += 1
		else:
			break
	for l in unseen_lines[]:
		if covers(line, l):
			count_covering += 1
		else:
			break
	
	accepted_lines.append(line)
	print line, count_covered_by, count_covering
	#if count_covering > count_covered_by:
		#unseen_lines.remove(line)
	#elif count_covered_by > count_covering:
		
		