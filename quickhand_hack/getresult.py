#encoding=utf-8
#!/usr/bin/python 
import os
import operator
import math

ids = []
result = {}
for i in range(0,60):
	imgname = str(i) + '.jpg'
	shell = os.popen("convert "+imgname+" dest.jpg -compose Difference -composite  -colorspace gray -verbose  info: |  sed -n '/statistics:/,/^  [^ ]/ p' | grep mean | cut -d ':' -f 2 | cut -d '(' -f 1").read()
	try:
		result[imgname] = float( shell.strip() )
	except:
		print shell.strip()
#sorted_x = sorted(result.iteritems(), key=operator.itemgetter(1))
#print sorted_x
min_key = min(result, key = result.get)
min_value = result[min_key]
for k in result.keys():
	if( result[k]<3 or abs(result[k] - min_value)<4):
		ids.append(k.split('.')[0])

print ','.join(ids)
