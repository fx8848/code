#http://www.pythonchallenge.com/pc/return/evil.html
f = open('evil2.gfx', 'rb')
data = f.read()
for i in range(5):
	f2 = open('evil_%d.jpg' % i, 'wb')
	f2.write(data[i::5])
	f2.close()
f.close()
