pent = set( n * (3*n - 1) / 2 for n in range(2,2400) ) 
 
def pe44():
  for pj in pent: 
    for pk in pent: 
      if pj - pk in pent and pj + pk in pent: 
        return pj - pk
 
print pe44()
