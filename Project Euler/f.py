#encoding=utf-8
txt = ''
for i in range(26,51):
	txt += str(i) + '、\r\n' +  open('%d.py' % i).read() + '\r\n'
open('f.txt', 'w').write(txt)
print 'success'
