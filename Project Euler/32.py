pandigitals = set()
for multiplicard in range(1, 5001):
	for multiplier in range(1, 101):
		product = multiplicard * multiplier
		ss = str(product)+str(multiplicard)+str(multiplier)
		ss = ''.join(sorted(ss))
		if ss == '123456789':
			print product
			pandigitals.add(product)
	
print sum(pandigitals)
