#encoding=utf-8
import re
import os
import zipfile

fileid = '90052'
values = []
while 1:
	f = open('/home/chenming/Desktop/channel/%s.txt' % fileid)
	content = f.read()
	ids = re.findall('Next nothing is (\d+)', content)
	#nextid = ids and ids[0] or '90052'
	nextid = ids[0] if ids else '90052' #两种写法
	fileid = nextid
	if nextid == '90052':
		break
	values.append(int(fileid))
	#print nextid
#print values
print ''.join(map(lambda i: zipfile.ZipFile('/home/chenming/Desktop/channel.zip').getinfo(str(i)+'.txt').comment, [i for i in values]))

