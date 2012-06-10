num = 0
strs = ''
count = 0
while count < 1000001:
	l = len(str(num))
	count += l
	strs += str(num)
	num += 1

ss = 1
for i in range(7):
	ss *= int( strs[10**i] )
print ss
