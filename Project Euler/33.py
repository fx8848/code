d = 1
for i in range(1, 10):
  for j in range(1, i):
    for k in range(1, j):
      ki = k*10 + i
      ij = float(i)*10 + j
      if (k*ij == ki*j):
        d *= ij/ki
print d 
