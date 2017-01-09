# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int,raw_input().split())
coins = sorted(map(int, raw_input().split()))
count_table = [1]
for i in xrange(1,N+1):
    count_table.append(sum(count_table[i-c] for c in coins if i - c >= 0))
print count_table