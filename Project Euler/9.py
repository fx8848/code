find = 0
for c in range(1,1000,1):
	for b in range(1,c,1):
		a = 1000-b-c
		if a**2 + b**2 == c**2:
			find = 1
			break
	if find:
		break
print a*b*c 
#print( [a*b*(1000 - b -a) for b in xrange(1,500+1) for a in xrange(b,500+1) if a * a + b * b == ((1000 -b -a) * (1000 - b - a))][0])
