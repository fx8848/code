#encoding=utf8
from math import sqrt
'''
Note that Hexagonal numbers are a subset of Triangle numbers so we only determine the first occurrence of Hi = Pj to find our answer. We can safely start our search from 144 as alluded from the problem’s description.
'''
def is_pentagonal(n):
	   p = (sqrt(1 + 24*n) + 1) / 6
	   return p==int(p)
h = lambda n: n*(2*n - 1) #calculate the nth hexagonal number
n = 144 
while not(is_pentagonal(h(n))): n += 1 
print h(n)
