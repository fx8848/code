numbers = [0] * 91
numbers[0] = 0
numbers[1] = 3
numbers[2] = 3
numbers[3] = 5
numbers[4] = 4
numbers[5] = 4
numbers[6] = 3
numbers[7] = 5
numbers[8] = 5
numbers[9] = 4
numbers[10] = 3
numbers[11] = 6
numbers[12] = 6
numbers[13] = 8
numbers[14] = 8
numbers[15] = 7
numbers[16] = 7
numbers[17] = 9
numbers[18] = 8
numbers[19] = 8
numbers[20] = 6
numbers[30] = 6
numbers[40] = 5
numbers[50] = 5
numbers[60] = 5
numbers[70] = 7
numbers[80] = 6
numbers[90] = 6

def get_length(n):
	length = 0
	a = n / 100
	n = n % 100
	b = n / 10
	c = n % 10
	if a != 0:
		length += numbers[a] + 7 #7 for "hundred"
		if b != 0 or c != 0:
			length += 3 #3 for "and"
	if b != 0:
		if b == 1:
			length += numbers[b*10+c]
			return length
		else:
			length += numbers[b*10]
	if c != 0:
		length += numbers[c]
	return length

length = 0
for i in range(1,1000,1):
	length += get_length(i)
length += 11 #11 for "one thousand"
print length
	
