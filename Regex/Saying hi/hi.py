import re
N = input()
for _ in range(N):
    s = raw_input()
    if re.search("^((?i)hi)\s[^dD]",s):
        print s