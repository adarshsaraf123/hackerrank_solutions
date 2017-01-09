# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
string = raw_input()
L = len(string)
root = math.sqrt(L)
lower = int(math.floor(root))
upper = int(math.ceil(root))
if lower*lower >= L:
    rows = columns = lower
elif lower*upper >= L:
    rows = lower
    columns = upper
else:
    rows = columns = upper
for i in xrange(columns):
    if i >= L:
        break
    temp = string[i]
    k = i+columns
    while k < L:
        temp += string[k]
        k += columns
    print temp,