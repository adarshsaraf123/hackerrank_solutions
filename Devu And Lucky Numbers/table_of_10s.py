mod_value = 10**9 + 7
table_of_10s_modular = [0,1]

for i in xrange(2, 301):
	table_of_10s_modular.append((table_of_10s_modular[i-1]*10 + 1) % mod_value)

print table_of_10s_modular