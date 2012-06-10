fiblist = [1,2]
while 1:
	fiblist.append(fiblist[-1] + fiblist[-2])
	if fiblist[-1] > 4000000:
		fiblist.pop(-1)
		break
print sum([a for a in fiblist if a%2==0])
