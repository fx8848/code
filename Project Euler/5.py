num = 40
while 1:
	f = 1
	for i in range(1,20,1):
		if not num % i == 0:
			f = 0
			break
	if f:
		break
	num = num + 20
print num
