#encoding=utf8

'''
算法导论，P85，快速排序
'''

def quicksort(A, p, r):
	if p < r:
		q = partition(A, p, r)
		quicksort(A, p, q-1)
		quicksort(A, q+1, r)


#对子数组A[p, r]进行就地重排
def partition(A, p, r):
	x = A[r]
	i = p-1
	for j in range(p, r):
		if A[j] <= x:
			i += 1
			tmp = A[i]
			A[i] = A[j]
			A[j] = tmp
	tmp = A[i+1]
	A[i+1] = A[r]
	A[r] = tmp
	return i+1


if __name__ == '__main__':
	test = [2,8,7,1,3,5,6,4]
	partition(test, 0, len(test)-1)
	#print test
	quicksort(test, 0, len(test)-1)
	print test
