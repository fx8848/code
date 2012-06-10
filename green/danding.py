# encoding=utf-8
import xml.etree.ElementTree as ET
import os

path = os.getcwd()+os.sep+'danding'
if not os.path.isdir(path):
	print '正在创建下载目录 /danding'
	os.mkdir(path)
	os.curdir=path
os.system('wget http://www.danding.com.cn/picList.xml -O '+path+os.sep+'picList.xml')
root = ET.parse('picList.xml').getroot()
allpics = root.findall('pic')
for pic in allpics:
	picurl = pic.find('src').text
	arr = picurl.split('/')
	picname = arr[len(arr)-1]
	#print picurl
	os.system('wget '+picurl+' -O '+path+os.sep+picname)


