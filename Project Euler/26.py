#encoding=utf-8
'''
而怎么计算一个数的循环长度呢
只需要知道它能被多少长度的9整除就行了
3能被9整除，所以它的循环长度是1
7能被999999整除，商正好是循环体142857，所以它的循环长度是6
'''
from euler import is_prime

n = 997
for p in range(n, 1, -2):
	if not is_prime(p):
		continue
	c = 1
	while (pow(10, c) - 1) % p != 0:
		c += 1
	if p-c == 1:
		break
print p
