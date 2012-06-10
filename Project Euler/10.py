import math

def is_prime(dest):
	divisor = 3
	sqrt_dest = math.sqrt(dest)
	while divisor <= sqrt_dest:
		if dest % divisor == 0:
			return 0
		divisor += 2
	return 1

print sum([2] + [a for a in xrange(3,2000001,2) if is_prime(a)])
