routes = 1
n = 40
m = 1
while n > m:
	routes *= n
	routes /= m
	n -= 1
	m += 1
print routes
