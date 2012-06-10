from euler import prime_sieve, is_prime

max = 1000000
primes = prime_sieve(max)
prime_sum = [0]

sum = 0
count = 0
while(sum < max):
	sum += primes[count]
	prime_sum.append(sum)
	count += 1

terms = 1
for i in range(count):
	for j in range(i+terms, count):
		n = prime_sum[j] - prime_sum[i]
		if j-i > terms and is_prime(n):
			terms, max_prime = j-i, n
print max_prime			
