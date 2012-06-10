def numbers(n):
	count = 1
	if n == 1:
		return count
	while n != 1:
		if n % 2:
			n = n * 3 + 1
		else:
			n = n / 2
		count += 1
	return count

m = 0
for i in range(1000000,1,-1):
	temp = numbers(i)
	if m < temp:
		m = temp
		record = i
print record
