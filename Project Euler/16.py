s = 2**1000
t = 0
for si in str(s):
	t += int(si)
print t
print sum([int(si) for si in str(2**1000)])
