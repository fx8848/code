s = 1
for i in range(1,101,1):
	s *= i
add = 0
for si in str(s):
	add += int(si)
print add
