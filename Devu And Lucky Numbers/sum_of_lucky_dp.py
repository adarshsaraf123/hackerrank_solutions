mod_value = 1000000007

table_of_10s = {0: 0, 1: 1, 2: 11, 3: 111, 4: 1111, 5: 11111, 6: 111111, 7: 1111111, 8: 11111111, 9: 111111111, 10: 111111104, 11: 111111034, 12: 111110334, 13: 111103334, 14: 111033334, 15: 110333334, 16: 103333334, 17: 33333334, 18: 333333341, 19: 333333390, 20: 333333880, 21: 333338780, 22: 333387780, 23: 333877780, 24: 338777780, 25: 387777780, 26: 877777780, 27: 777777745, 28: 777777402, 29: 777773972, 30: 777739672, 31: 777396672, 32: 773966672, 33: 739666672, 34: 396666672, 35: 966666700, 36: 666666938, 37: 666669339, 38: 666693349, 39: 666933449, 40: 669334449, 41: 693344449, 42: 933444449, 43: 334444428, 44: 344444260, 45: 444442580, 46: 444425773, 47: 444257703, 48: 442577003, 49: 425770003, 50: 257700003, 51: 577000017, 52: 770000136, 53: 700001312, 54: 13072, 55: 130721, 56: 1307211, 57: 13072111, 58: 130721111, 59: 307211104, 60: 72111020, 61: 721110201, 62: 211101962, 63: 111019607, 64: 110196064, 65: 101960634, 66: 19606334, 67: 196063341, 68: 960633404, 69: 606333978, 70: 63339739, 71: 633397391, 72: 333973869, 73: 339738670, 74: 397386680, 75: 973866780, 76: 738667738, 77: 386677332, 78: 866773300, 79: 667732945, 80: 677329409, 81: 773294049, 82: 732940442, 83: 329404372, 84: 294043700, 85: 940436987, 86: 404369808, 87: 43698053, 88: 436980531, 89: 369805283, 90: 698052810, 91: 980528059, 92: 805280528, 93: 52805225, 94: 528052251, 95: 280522476, 96: 805224747, 97: 52247415, 98: 522474151, 99: 224741476}

table_count_choices = {}

def create_table_count_choices(digits,x,y,z):
	x = min(x,digits)
	y = min(y,digits)
	z = min(z,digits)
	
	#set the boundary for d = 0
	upper_i = min(x, digits)
	for i in xrange(upper_i + 1):
		upper_j = min(y, digits - i)
		for j in xrange(upper_j + 1):
			upper_k = min(z, digits- i - j)
			for k in xrange(upper_k + 1):
				table_count_choices[(0,i,j,k)] = 1
				#print 0, i, j, k
	
	#set the boundary for i = 0
	for d in xrange(1,digits+1):
		#set for j = 0 when i = 0
		for k in xrange()
		upper_j = min(y, d)
		for j in xrange(1, upper_j + 1):
			upper_k = min(z,d - j)
			for k in xrange(1, upper_k+1):
				print d, 0, j, k
				table_count_choices[(d,0,j,k)] = table_count_choices[(d-1,0,j-1,k)] + table_count_choices[(d-1,0,j,k-1)]
	
	#for d in xrange(1,digits+1):
		#upper_k = min(z, digits)
		#for k in xrange(digits) 
		#upper_i = min(x, digits)
		#for i in xrange(1,upper_i + 1):
			#upper_k = min(z, digits- i)
			#for k in xrange(1, upper_k + 1):
				#table_count_choices[(d,i,0,k)] = table_count_choices[(d-1,i-1,0,k)] + table_count_choices[(d-1,i,0,k-1)]
	
	#for d in xrange(1,digits+1):
		#upper_i = min(x, digits)
		#for i in xrange(upper_i + 1):
			#upper_j = min(y, digits - i)
			#for j in xrange(upper_j + 1):
				#table_count_choices[(d,i,j,0)] = table_count_choices[(d-1,i-1,j,0)] + table_count_choices[(d-1,i,j-1,0)]
	
	#for d in xrange(1,digits+1):
		#upper_i = min(x, digits)
		#for i in xrange(1, upper_i + 1):
			#upper_j = min(y, digits - i)
			#for j in xrange(1, upper_j + 1):
				#upper_k = min(z, digits- i - j)
				#for k in xrange(1, upper_k + 1):
					#table_count_choices[(d,i,j,k)] = table_count_choices[(d-1,i-1,j,k)] + table_count_choices[(d-1,i,j-1,k)] + table_count_choices[(d-1,i,j,k-1)]
	
	#count = 0
	#if x > 0:
		#count += count_choices(x-1,y,z,k-1)
	#if y > 0:
		#count += count_choices(x,y-1,z,k-1)
	#if z > 0:
		#count += count_choices(x,y,z-1,k-1)
	#return count

def sum_lucky(x, y, z):
	max_digits = x + y + z
	sum_value = 0
	for num_digits in xrange(1,max_digits+1):
		if num_digits not in table_of_10s:
			table_of_10s[num_digits] = (table_of_10s[num_digits-1]*10 + 1) % mod_value
		sum_value = (sum_value + 4*(table_of_10s[num_digits])*table_count_choices[(num_digits - 1, x-1, y, z)]) % mod_value
		sum_value = (sum_value + 5*(table_of_10s[num_digits])*table_count_choices[(num_digits - 1, x, y-1, z)]) % mod_value
		sum_value = (sum_value + 6*(table_of_10s[num_digits])*table_count_choices[(num_digits - 1, x, y, z-1)]) % mod_value
		#print num_digits, sum_value
	return sum_value

test_choice = True
if test_choice:
	values = (10,5,3,9)
	create_table_count_choices(*values)
	#print table_count_choices[(10,5,3,9)]
else:
	x, y, z = 1, 2, 3#map(int,raw_input().split())
	print sum_lucky(x,y,z)
	