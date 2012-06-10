# coding=utf-8
import urllib
import os
import codecs
import thread

def GetURLS(url):
	list0 = []
	s1 = '<div class="tit"><a href'
	content = urllib.urlopen(url).read().decode('gbk')
	i = content.find(s1)
	if(i <> -1):
		content = content[i+26:len(content)]
	while True:
		i = content.find(s1)
		if(i == -1):
			break
		content = content[i+26:len(content)]
		i = content.find('"')
		str0 = content[0:i]
		str0 = 'http://hi.baidu.com'+str0
		list0.append(str0)
		content = content[i:len(content)]
	return list0

def GetContent(url):
	s1 = '<div id="m_blog" class="modbox"'
	s2 = '<div class="opt">'
	content = urllib.urlopen(url).read().decode('gbk')
	i = content.find('<title>')+7
	content = content[i:len(content)]
	j = content.find('_')
	title = content[0:j]
	i = content.find(s1)
	j = content.find(s2)
	content = content[i:j]
	return content, title

def ToHTML(content, name):
	s1 = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<title>\n'+name+'</title>\n</head>\n<body>\n'
	s2 = '\n</body></html>'
	name = name.replace('*', '')
	name = name.replace('/', '')
	name = name.replace('\\', '')
	name = name.replace(':', '')
	name = name.replace('?', '')
	name = name.replace('"', '')
	name = name.replace('<', '')
	name = name.replace('>', '')
	name = name.replace('|', '')
	name = name.replace('#', 'Sharp')
	name = name + '.html'
	content = s1+content+s2
	filea = codecs.open(name, 'w', 'utf-8')
	filea.write(content)
	filea.close()

def downOne(url, sum0):
	content, title = GetContent(url)
	mylock.acquire()   #获取同步锁
	title = str(sum0)+','+title
	mylock.release()  #释放同步锁
	ToHTML(content, title)
	print title											


HiName = 'hacklzt'
baseurl = 'http://hi.baidu.com/'+HiName+'/blog/index/'
i = 0 #博客分页 
sum0 = 0 #文章总数

#多线程同步锁
mylock = thread.allocate_lock()
while True:
	list0 = GetURLS(baseurl+str(i))
	if(len(list0) == 0):
		break
	for j in list0:
		sum0 = sum0+1
		thread.start_new_thread(downOne,(j, sum0))		
	i = i+1
