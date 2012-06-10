from euler import is_prime, is_perm
 
n = 1489 	# must be odd
while True:
  b, c = n+3330, n+6660
  if is_prime(n) and is_prime(b) and is_prime(c) \
    and is_perm(n,b) and is_perm(b,c): break
  n += 2
 
print "Answer to PE49 = ", str(n)+str(b)+str(c)
