#encoding=utf-8
#http://www2.stetson.edu/~efriedma/holiday/2011/index.html
table = ['+', '*', '/', '-']
hasmethod = 0
def calc(method, cursum, curmethods, leftright):
	global hasmethod

	desmethod = []
	if hasmethod:
		return
	if method == '+':
		cursum += 7
		curmethods += '+'
		if cursum % 2 == 0:
			desmethod.append('/')
		if leftright == 'r':
			desmethod.append('*')
			desmethod.append('-')
	elif method == '*':
		cursum *= 3
		curmethods += '*'
		if leftright == 'l':
			if cursum % 2 == 0: 
				desmethod.append('/')
			desmethod.append('+')
		desmethod.append('-')
	elif method == '-':
		cursum -= 5
		curmethods += '-'
		if leftright == 'l':
			if cursum % 2 == 0:
				desmethod.append('/')
			desmethod.append('+')
		desmethod.append('*')
	elif method == '/':
		cursum /= 2
		curmethods += '/'
		desmethod.append('+') 
		if leftright == 'r':
			desmethod.append('*')
			desmethod.append('-')
	if cursum == 2012:
		ensuremethod(curmethods)
		curmethods = curmethods.replace('+', '+7 ')
		curmethods = curmethods.replace('-', '-5 ')
		curmethods = curmethods.replace('*', '*3 ')
		curmethods = curmethods.replace('/', '/2 ')
		print curmethods
		hasmethod = 1
	elif len(curmethods) < 30:  #防止递归调用层次过深
		for m in desmethod:
			curleftright = leftright
			#控制方向，从左进还是从右进
			if (m in ['+', '/'] and method in ['+', '/']) or (m in ['*', '-'] and method in ['*', '-']):
				curleftright = 'r' if leftright == 'l' else 'l'
			calc(m, cursum, curmethods, curleftright)

def ensuremethod(methodstr):
	print methodstr
	print len(methodstr)
	s = 2011
	str0 = ''
	for i in methodstr:
		strs = str(s)
		if i == '+':
			s += 7
			str0 = '+7'
		elif i == '-':
			s -= 5
			str0 = '-5'
		elif i == '*':
			s *= 3
			str0 = '*3'
		elif i == '/':
			s /= 2
			str0 = '/2'
		print '%s%s=%d' % (strs, str0, s)
	print s


hasmethod = 0
calc('+', 2011, '', 'r')
