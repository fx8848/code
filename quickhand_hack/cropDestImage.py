#encoding=utf-8
#! /usr/bin/python

import Image
import sys
import os

if len(sys.argv) == 1:
	print "参数不能为空"
	exit()
filename = sys.argv[1]
if not os.path.exists(filename):
	print "文件不存在"
	exit()
box = (10,10,80,70)  #要跟其它要比较的图片一样大小
destimg = Image.open(filename)
destimg = destimg.convert('RGB')
outimg = destimg.crop(box)
outimg.save(filename+'2.jpg', 'jpeg');
#destimg.save(filename+".jpg", 'jpeg')

