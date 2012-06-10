#encoding=utf8
'''
算法导论，P78，堆排序算法
'''

def heapsort(A):
	build_max_heap(A)
	A_sorted = []
	for i in range(len(A), 1, -1):
		A_sorted.insert(0, A.pop(0))
		max_heapify(A, 1)
	A_sorted.insert(0, A.pop(0))
	return A_sorted

def build_max_heap(A):
	for i in range(len(A)/2, 0, -1):
		max_heapify(A, i)

#使以i为根的子树成为最大堆，i从1开始
def max_heapify(A, i):
	l = 2 * i   #左儿子
	r = 2 * i +1
	heap_size = len(A)
	largest = i
	if l <= heap_size and A[l-1] > A[i-1]:
		largest = l
	if r <= heap_size and A[r-1] > A[largest-1]:
		largest = r
	if largest != i:
		tmp = A[i-1]
		A[i-1] = A[largest-1]
		A[largest-1] = tmp
		max_heapify(A, largest)


if __name__ == '__main__':
	test = [16,14,10,8,7,9,3,2,4,1]
	max_heapify(test, 2)
	#print test
	test = [4,1,3,2,16,9,10,14,8,7]
	build_max_heap(test)
	#print test
	test_sorted = heapsort(test)
	print test_sorted
