# Enter your code here. Read input from STDIN. Print output to STDOUT
N, Q = map(int, raw_input().split())
A = map(int, raw_input().split())
scanned = []

for i in xrange(N):
	scanned.append([(A[i]&1)])
	#print "i = ", i, len(scanned)
	for j in xrange(i+1,N):
		#print "\t j = ", j, len(scanned[i])
		scanned[i].append(scanned[i][j-i-1] ^ ( A[j] & 1 ))

print scanned
for q in xrange(Q):
    L, R = map(int, raw_input().split())
    #print L-1, R-L-1
    odd = scanned[L-1][R-L]
    print (1-odd)*"Even" + odd*"Odd"
