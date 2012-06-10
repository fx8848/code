#encoding=utf8
'''
算法导论，P230，贪心算法，0-1背包问题，动态规划解
'''

'''
v:价值数组，  w:重量数组   n:物品个数   W:背包的最大重量
'''
def dynamic_01_knapsack(v, w, n, W):
	c = [ [0] * (W+1) for row in range(n+1) ]
	for i in range(1, n+1):
		for weight in range(1, W+1):
			if w[i-1] <= weight:   #能装下
				if v[i-1] + c[i-1][weight-w[i-1]] > c[i-1][weight]:
					c[i][weight] = v[i-1] + c[i-1][weight-w[i-1]]
				else:
					c[i][weight] = c[i-1][weight]
			else: #装不下
				c[i][weight] = c[i-1][weight]
	return c[n][W]

if __name__ == '__main__':
	v = [60,100,120]
	w = [10,20,30]
	W = 50
	print dynamic_01_knapsack(v, w, 3, W)
