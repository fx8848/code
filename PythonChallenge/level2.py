import sys
import io
import urllib

#txt = open('/home/chenming/Desktop/level1.txt').read()
txt = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
txt = txt[txt.index('%%$'): -5]
l = {}
for t in txt:
	if t not in l.keys():
		l[t] = 1
	else:
		l[t] += 1
l2 = sorted(l.items(), key=lambda d:d[1])
#print l2
print ''.join([minkey[0] for minkey in l2 if minkey[1]<2])
