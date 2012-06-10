from euler import is_prime, is_pandigital
'''
any integer is divisible by 3 or 9 whose sum of digits is divisible by 3 or 9; therefore composite and not prime.

9+8+7+6+5+4+3+2+1 = 45,
8+7+6+5+4+3+2+1 = 36,
6+5+4+3+2+1 = 21, and
5+4+3+2+1 = 15,
all of which are divisible by 3 and therefore could not yield a 1 to {5, 6, 8, 9} pandigital prime. So that leaves 4 and 7 digit prime numbers less than 4321 and 7654321 respectively. 

'''

n = 7654321
while not(is_prime(n) and is_pandigital(str(n), 7)):
	n -= 2
print n
