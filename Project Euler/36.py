result = 0
for i in range(1, 1000001):
	if str(i) == str(i)[::-1]:
		b = str(bin(i))[2:]
		if b == b[::-1]:
			#print i, b
			result += i 
print result
