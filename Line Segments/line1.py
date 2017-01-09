# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
t = sorted({tuple(map(int, raw_input().split())) for _ in xrange(n)}, key=lambda x: (x[0], -x[1]))
dp = [0]
for _, y in t:
    if y > dp[-1]:
        dp.append(y)
        continue
    #b, e = 0, len(dp)-1
    #while b < e:
        #c = (b+e+1)/2
        #if dp[c]<y: b=c
        #else: e=c-1
    #dp[b+1]=y
#print len(dp)-1