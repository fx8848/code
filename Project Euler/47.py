from euler import factor
# the euler module can find here : http://blog.dreamshire.com/2009/03/26/94/ 
ci = 1
nf = 4		#number of distinct factors
ns = 4		#number of consecutive integers
n = 2*3*5*7	#starting candidate for search
while ci != ns:
  n += 1
  if len(factor(n)) == nf: ci += 1
  else: ci = 0
 
print "Answer to PE47 = ", n-nf+1
