import urllib

def name_sum(name):
	s = 0
	for si in name:
		s += ord(si) - ord('A') + 1
	return s
namedata = urllib.urlopen('http://projecteuler.net/project/names.txt').read()
#namedata = open('names.txt').read()
namelist = [l[1:-1] for l in namedata.split(',')]
namelist.sort()

score_sum = 0
for i, name in enumerate(namelist):
	score_sum += (i+1) * name_sum(name)
print score_sum
