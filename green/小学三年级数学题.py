#encoding=utf8
'''
有2,3,4,5,6,7,8七个数字，要把他们放到下面的算式的X中，使之成立
  X X X
    * X
---------
X X X X
每个数字至少出现一次。
'''
import itertools

results = set()
solutions = itertools.permutations(range(2,9))
for solution in solutions:
	sotmp = list(solution)
	for i in range(2,9):
		for j in range(len(solution)):
			so = sotmp[:]
			so.insert(j, i)
			A = int(''.join([str(s) for s in so[0:3]]))
			B = so[3]
			C = so[4]*1000 + so[5]*100 +so[6]*10 + so[7]
			if A * B == C:
				results.add('%d * %d = %d' % (A,B,C))
print '\n'.join(results)
