#encoding=utf8
'''
动态规划，P200，矩阵链乘法问题
'''
import copy

def matrix_chain_order(p):
	n = len(p) - 1
	m = [[0]*n for row in range(n)] 
	s = copy.deepcopy(m) 
	for l in range(2, n+1):  #l为链的长度
		for i in range(1, n-l+2):  #i为链开始的位置，从1开始
			j = i+l-1   #j为链结束的位置，从1开始
			m[i-1][j-1] = 100000000000
			for k in range(i, j):
				q = m[i-1][k-1] + m[k][j-1] + p[i-1]*p[k]*p[j]
				if q < m[i-1][j-1]:
					m[i-1][j-1] = q
					s[i-1][j-1] = k
	return m, s

def print_optimal_parens(s, i, j):
	global resultstr
	if i==j:
		resultstr += 'A'+str(i+1)
	else:
		resultstr += '('
		print_optimal_parens(s, i, s[i][j]-1)
		print_optimal_parens(s, s[i][j], j)
		resultstr += ')'

if __name__ == '__main__':
	p = [30,35,15,5,10,20,25]
	m, s = matrix_chain_order(p)
	print s
	print m
	resultstr = ''
	print_optimal_parens(s, 0, 5)
	print resultstr
