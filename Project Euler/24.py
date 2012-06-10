#encoding=utf-8
import copy

numbers = [str(i) for i in range(10)]
allnum = []

def gennum(numbers, numstring):
	for num in numbers:
		tmpstr = numstring[:]
		tmpstr.append(num)
		if len(numbers) == 1:
			allnum.append(tmpstr)
		elif len(numbers) > 1:
			tmp = numbers[:]
			tmp.remove(num)
			gennum(tmp, tmpstr)

gennum(numbers, [])
print len(allnum)
print allnum[999999]
print ''.join([str(i) for i in allnum[999999]])

#更加简单的方法
import itertools
print [d for d in itertools.permutations(range(10))][999999]
