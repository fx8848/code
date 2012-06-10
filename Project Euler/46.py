n = 5
f = 1
primes = set()
 
while (1):
  if all( n % p for p in primes ):
    primes.add(n)
  else:
    if not any( (n-2*i*i) in primes for i in range(1, n) ):
      break
  n += 3-f
  f = -f
print n
