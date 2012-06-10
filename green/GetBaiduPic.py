# coding=utf-8
import urllib
import os

def GetPicURLS(url):
	urllist = []
	content = urllib.urlopen(url).read().decode('gb2312')
	s1 = 'psrc:"http://hiphotos.baidu.com'
	while True:
		i = content.find(s1)
		if(i==-1): 
			break
		content = content[i+31:len(content)]
		i = content.find('"')
		str0 = content[0:i]
		str0 = 'http://hiphotos.baidu.com'+str0
		str0 = str0.replace('abpic','pic')
		urllist.append(str0)
		print str0
		content = content[i:len(content)]
	return urllist

#用户名
hiname = 'hacklzt'
#图片下载地址列表
piclist = []
i = 0
num = 0
tempPic = ''
baseurl = 'http://hi.baidu.com/'+hiname+'/album/%C4%AC%C8%CF%CF%E0%B2%E1/index/'

while True:
	piclist = GetPicURLS(baseurl + str(i))
	if(piclist[0] == tempPic):
		break
	for j in range(1, len(piclist)):
		os.system('wget '+piclist[j])
		num = num+1
	tempPic = piclist[0]
	i = i+1

