# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(3500)
mod_value = 10**9 + 7
count_memoized = {}
def count_possibilities(current_soldier, current_skills, level = 0):
	#print level*"\t",current_soldier, current_skills, R 
	if current_skills == R:
		temp = count_memoized[(current_soldier, current_skills)] = pow(2,N-current_soldier, mod_value)
		return temp
	if current_soldier == N or current_skills > R:
		return 0
	if (current_soldier, current_skills) in count_memoized:
		return count_memoized[(current_soldier,current_skills)]
	count = 0
	#generate breadth with iteration and depth with recursion to make use of backtracking
	for i in xrange(current_soldier,N):
		count = (count + count_possibilities(i + 1, current_skills | S[i], level + 1)) % mod_value
	#count = ( count + count_possibilities(current_soldier + 1, current_skills) ) % mod_value
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
if N == 0:
	print 0
else:
	print count_possibilities(0,0)