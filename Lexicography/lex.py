# Enter your code here. Read input from STDIN. Print output to STDOUT
from operator import mul
fact = {0:1, 1:1}
def factorial(n):
	if n in fact:
		return fact[n]
	else:
		fact[n] = n*factorial(n-1)
		return fact[n]

from collections import Counter
word, K = raw_input().split()
K = int(K)
while K != 0:
	letters_count = Counter(word)
	
	word_len = len(word)
	letters = sorted(set(word))
	
	k_word = []
	cur_rank = 0
	
	numerator = factorial(word_len - 1)
	denominator = reduce(mul, (factorial(letters_count[c]) for c in letters))
	found = False
	#update letters_count, numerator and denominator for each iteration 
	for i in range(word_len): #iterate over the positions of the new word of rank K to be found
		#print k_word, letters_count, numerator, denominator, cur_rank
		if found:
			break
		last_c = letters[0]
		for c in letters:
			if letters_count[c] == 0:
				continue
			temp = (numerator * letters_count[c]) / denominator
			if cur_rank + temp > K:
				#found the i'th letter
				if i < word_len-1:
					numerator /= word_len - 1 - i
					denominator /= letters_count[c]
					letters_count[c] -= 1
				k_word.append(c)
				break
			elif cur_rank + temp == K:
				#using this letter will result in the required word of rank K
				found = True
				k_word.append(c)
				letters_count[c] -= 1
				for l in letters[::-1]:
					while letters_count[l] > 0:
						k_word.append(l)
						letters_count[l] -= 1
				break
			else:
				cur_rank += temp
			#print cur_rank
	
	print ''.join(k_word)
	#print letters
	#print l_c
	
	#new input
	word, K = raw_input().split()
	K = int(K)