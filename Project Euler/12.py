#encoding=utf-8

def get_divisors_count(number):
	if number<1: return 1
	count = 1
	factor = 2
	n = number
	while n>1:
		if n%factor == 0:
			t = 1
			while n%factor == 0:
				t += 1
				n /= factor
			count *= t
		factor += 1
	return count
tt = 1000
while 1:
	s = tt * (tt+1) / 2
	if get_divisors_count(s)>500:
		print s
		break
	tt += 1 

