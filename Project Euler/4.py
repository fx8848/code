pal = []
for i in range(999,101,-1):
	for j in range(999,101,-1):
		if str(i*j) == str(i*j)[::-1]:
			pal.append(i*j)
print max(pal)
