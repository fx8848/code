#encoding=utf-8
#!/usr/bin/python

import Image
import os
import sys

per_w = 70
per_h = 60
space = 1
if len(sys.argv) == 1:
	print "参数不能为空"
	exit()
filename = sys.argv[1]
if not os.path.exists(filename):
	print "目标文件不存在"
	exit()
destimg = Image.open(filename)
for i in range(0,6):
	for j in range(0,10):
		topx = j*per_w + j*space
		topy = i*per_h + i*space
		bottomx = topx+per_w
		bottomy = topy+per_h
		box = (topx, topy, bottomx, bottomy)
		smallimg = destimg.crop(box)
		smallimg.save(str(i*10+j)+'.jpg')
