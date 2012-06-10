#encoding=utf-8
'''
动态规划，196页，装配线调试问题
'''
'''
a:装配站的装配时间，t:在装配站Sij移到别一条线花费的时间
e:进入i条线的时间， x:离开i条线的时间
n:装配站总数
'''
def fastest_way(a, t, e, x, n):
	a1, a2 = a[0], a[1]
	t1, t2 = t[0], t[1]
	e1, e2 = e[0], e[1]
	x1, x2 = x[0], x[1]
	f1 = [ e1 + a1[0] ]
	f2 = [ e2 + a2[0] ]
	f = 0
	l1, l2 = [], [] 
	l = 0
	for i in range(1, n):
		if f1[i-1] + a1[i] <= f2[i-1] + t2[i-1] + a1[i]:
			f1.append( f1[i-1] + a1[i] )
			l1.append(1)
		else:
			f1.append( f2[i-1] + t2[i-1] + a1[i])
			l1.append(2)
		if f2[i-1] + a2[i] <= f1[i-1] + t1[i-1] + a2[i]:
			f2.append(f2[i-1] + a2[i])
			l2.append(2)
		else:
			f2.append(f1[i-1] + t1[i-1] + a2[i])
			l2.append(1)
	if f1[n-1] + e1 <= f2[n-1] + e2:
		f = f1[n-1] + e1
		l = 1
	else:
		f = f2[n-1] + e2
		l = 2
	return (l1, l2), l

def print_stations(lxx, l, n):
	print lxx
	print 'line %d, station %d' % (l, n)
	i = l
	for j in range(n-1, 0, -1):
		i = lxx[i-1][j-1]
		print 'line %d, station %d' % (i, j)

if __name__ == '__main__':
	a1 = [7,9,3,4,8,4]
	a2 = [8,5,6,4,5,7]
	a = [a1, a2]
	t1 = [2,3,1,3,4]
	t2 = [2,1,2,2,1]
	t = [t1, t2]
	e = [2,4]
	x = [3,2]
	lxx, l = fastest_way(a, t, e, x, len(a1))
	print_stations(lxx, l, len(a1))
