#encoding=utf-8

numbers_sum = 1
corder_sum = 1
circle_num = (1001 + 1) / 2   #2n-1等于边长，n为圈数
for circle in range(2, circle_num+1):
	numbers_sum = (2 * (circle-1) - 1)**2 
	first_num = numbers_sum + 1 #这一圈的第一个数
	step = 2*circle - 2  #边长-1 
	first_corder = first_num + step - 1
	corder_sum += first_corder*4 + step*6

print corder_sum
