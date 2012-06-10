#encoding=utf8
'''
动态规划，P208页，最长公共子序列问题
'''
def lcs_length(X, Y):
	m, n = len(X), len(Y)
	c = [ [0]*(n+1) for row in range(m+1)]
	b = [ [0]*n for row in range(m)]
	for i in range(1, m+1):
		for j in range(1, n+1):
			if X[i-1] == Y[j-1]:
				c[i][j] = c[i-1][j-1] + 1
				b[i-1][j-1] = 0
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				b[i-1][j-1] = 1 
			else:
				c[i][j] = c[i][j-1]
				b[i-1][j-1] = -1 
	return c, b
def print_lcs(b, X, i, j):
	if i==0 or j==0:
		return
	if b[i-1][j-1] == 0:
		print_lcs(b,X,i-1,j-1)
		print X[i-1]
	elif b[i-1][j-1] == 1:
		print_lcs(b,X,i-1,j)
	else:
		print_lcs(b,X,i,j-1)


if __name__ == "__main__":
	X = list('ABCBDAB')
	Y = list('BDCABA')
	c, b = lcs_length(X, Y)
	print_lcs(b, X, len(X), len(Y))
	
