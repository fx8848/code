import math

def get_divisors_sum(n):
	s = 1
	for i in range(2, int(math.sqrt(n) + 1)): 
		if n % i == 0:
			s += i
			s += n / i
	return s

#print get_divisors_sum(220)
pairs = []
for i in range(1,10001,1):
	div_sum = get_divisors_sum(i)
	if div_sum != i:
		if get_divisors_sum(div_sum) == i:
			pairs.append(i)
print sum(set(pairs))
