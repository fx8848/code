#encoding=utf8
'''
算法导论，P19，分治法，合并排序
'''

def merger_sort(A, p, r):
	if p < r:
		q = (p + r) // 2
		merger_sort(A, p, q)
		merger_sort(A, q+1, r)
		merge(A, p, q, r)

#对数组A的，p到q，q+1到r进行合并
def merge(A, p, q, r):
	L = A[p:q+1]
	R = A[q+1:r+1]
	L.append(float('Infinity')) 
	R.append(float('Infinity')) 
	i, j = 0, 0
	for k in range(p, r+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1



if __name__ == '__main__':
	m = [11,21,31,44,15,56,67,88]
	merge(m, 0, 3, 7)
	#print m
	A = [5,2,4,7,1,3,2,6]
	merger_sort(A, 0, len(A)-1) 
	print A

