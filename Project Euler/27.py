#encoding=utf-8
from euler import is_prime

def get_primes_num(a, b):
	n = 0
	while 1:
		value = n*n + a*n +b
		if value <= 0:
			break
		if not is_prime(value):
			break
		n += 1
	return n

#print get_primes_num(-79, 1601)
'''
b一定是正素数
因为当n为0时，表达式的值为b
'''
primes_b = []
for i in range(3, 1000):
	if is_prime(i):
		primes_b.append(i)

solution = ()
snum = 0
for a in range(-999, 1000):
	for b in primes_b:
		gpnum = get_primes_num(a, b)
		if gpnum > snum:
			solution = (a, b)
			snum = gpnum
			print solution, gpnum, solution[0] * solution[1]			
