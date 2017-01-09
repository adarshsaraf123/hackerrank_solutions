# Enter your code here. Read input from STDIN. Print output to STDOUT
tens = {0:'',10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18: 'Eighteen', 19:'Nineteen', 2:'Twenty', 3:'Thirty', 4: 'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
ones = {0:'', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
commas = ['',' Thousand ', ' Million ', ' Billion ', ' Trillion ']

def convert_three(num):
    h = num / 100
    num %= 100
    s = ''
    if h > 0:
        s = ones[h] + ' Hundred '
    if num > 9 and num < 20:
        s += tens[num]
    else:
        t = num / 10
        if t > 0:
			s += tens[t] + ' ' 
        o = num % 10
        if o > 0:
			s += ones[o]
    return s

T = input()
for _ in xrange(T):
	N = input()
	if N == 0:
		print 'Zero'
		continue
	s = ''
	threes = []
	while N != 0:
		threes.append(N % 1000)
		N /= 1000
	n = len(threes)
	for i in xrange(n-1,-1,-1):
		s += convert_three(threes[i])
		if threes[i] > 0:
			s += commas[i]
	print s
    