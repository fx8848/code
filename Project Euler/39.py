t_max = 0
p_limit = 1000
 
for p in range(p_limit//2, p_limit+1, 2):
  t = 0;
  for a in range(2, p/4+1):
    if  p*(p - 2*a) % (2*(p-a)) == 0: t += 1
    if t > t_max: (t_max, p_max) = (t, p)
 
print p_max
