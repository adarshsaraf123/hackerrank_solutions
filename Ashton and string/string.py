# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
T = input()
for t in xrange(T):
    s=raw_input()
    N = len(s)
    K = input()
    substrings = []
    for m in xrange(N):
		for n in xrange(m, N):
			temp = s[m:n+1]
			if temp not in substrings:
				substrings.append(temp)
    concatenated = substrings[0]
    i= 0
    print substrings
    while(len(concatenated) < K):
        concatenated += substrings[i]
        i += 1
    print concatenated
    print concatenated[K]