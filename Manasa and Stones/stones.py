# Enter your code here. Read input from STDIN. Print output to STDOUT
T = input()
for t in xrange(T):
    N = input() - 1
    a = input()
    b = input()
    if a == b:
        print N*a
    else:
        if a > b:
            a, b = b, a
        for i in xrange(N+1):
            print i*b + (N-i)*a,
		print