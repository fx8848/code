# encoding=utf-8

import os
import sys

f = file('words.txt')
txt = f.readline().strip()
f.close()
words = txt.split(',')

f = file('words2.txt')
for eachline in f.readlines():
	words.append(eachline.split('=')[0])
f.close()

desf = file(sys.argv[1])
for eachline in desf:
	for word in words:
		index = eachline.find(word)
		if index != -1:	
			s1 = eachline[0:index]
			s2 = eachline[index:index+len(word)] #敏感词部分
			s3 = eachline[index+len(word):len(eachline)]
			print s1+"\033[0;31m"+s2+"\033[0m"+s3   #在终端上以自定义颜色打印出，后面那段将颜色复原
			break
desf.close()
