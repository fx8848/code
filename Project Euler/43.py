import itertools
#here is a better and faster way: http://blog.dreamshire.com/2009/04/28/project-euler-problem-43-solution/
iter_list = itertools.permutations(range(10))
result_sum = 0
divs = [2,3,5,7,11,13,17]
for number in iter_list:
	if number[0] == 0: continue
	number_str = ''.join([str(n) for n in number])
	isok = True
	for i in range(len(divs)):
		if int(number_str[i+1: i+4]) % divs[i] != 0:
			isok = False
			break
	if isok:
		result_sum += int(number_str)
print result_sum 
