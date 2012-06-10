resultsum = [] 

for num in range(2, 9**5*7):
	tmpsum = 0
	for i in str(num):
		tmpsum += int(i)**5
	if tmpsum == num:
		resultsum.append(tmpsum)
print resultsum
print sum(resultsum)
