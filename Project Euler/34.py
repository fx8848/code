fact = (1,1,2,6,24,120,720,5040,40320,362880)
s = 0

for n in range(10, 50000):
	x = sum( fact[int(d)] for d in str(n) )
	if n == x:
		s += n 
print s
