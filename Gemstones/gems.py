# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()
strings = []
for _ in xrange(N):
    strings.append(set(raw_input()))
gemstones = 0
for x in strings[0]:
    gem = 1
    i = 1
    while(i<N):
        if x not in strings[i]:
            gem = 0
            break
        i += 1
    gemstones += gem
print gemstones