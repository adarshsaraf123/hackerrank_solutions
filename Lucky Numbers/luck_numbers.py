def lucky_numbers(n):
	marked = [0]*n
	sieve = 3
	unmarked = n
	while sieve < unmarked:
		#print sieve
		#raw_input()
		k = 0
		first_mark = True
		for i in xrange(n):
			if not marked[i]:
				k += 1
			if k == sieve:
				marked[i] = 1
				unmarked -= 1
				k = 0
		for i in xrange((sieve - 1)/2 + 1, n):
			if not marked[i]:
				sieve = i*2 + 1
				break
		#print marked, unmarked
		#raw_input()
	return marked

N = 300000
marked = lucky_numbers(N)
#for i in xrange(N):
	#if not marked[i]:
		#print i*2 + 1,