import mod_inv
mod_value = 10**9 + 7
fact_modular = {0:1}
fact_modular_inverse = {0:1}

for i in xrange(1, 301):
	fact_modular[i] = (i*fact_modular[i-1]) % mod_value
for i in xrange(1, 101):
	fact_modular_inverse[i] = mod_inv.modinv(fact_modular[i], mod_value)

print fact_modular.values()
print fact_modular_inverse.values(), len(fact_modular_inverse)