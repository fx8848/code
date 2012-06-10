#encodin=utf-8
target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [1]+[0]*target
'''
动态归划问题
'''
for coin in coins:
   for i in range(coin, target+1):
       ways[i] += ways[i-coin]
print ways[target]
