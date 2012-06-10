import urllib

words = urllib.urlopen('http://projecteuler.net/project/words.txt').read()
wordslist = [ w[1:-1] for w in words.split(',') ]
tri_numbers = []
n = 1
while n*(n+1) / 2 <= 260:
	tri_numbers.append(n*(n+1)/2)
	n += 1
result = 0
for word in wordslist:
	v = 0
	for w in word:
		v += ord(w)-ord('A')+1
	if v in tri_numbers:
		result += 1

print result 

