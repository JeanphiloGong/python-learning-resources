#coding=utf-8
domain=[value for value in range(1,21)]#输出1~20的数字
print(domain)

domain1 = [value for value in range(1,1000001)]
print(domain1)#输出1~1000000的数字
print(min(domain1))#输出该列表中最小的数
print(max(domain1))#输出该列表中最大的数字
print(sum(domain1))#计算该列表中所有数字的和

domain2=[]
for value1 in range(1,20,2):#创建一个包含从1~20的奇数的元素
  domain2.append(value1)
  print(domain2)
 
domain3=[]
for value2 in range(3,31,3):
	domain3.append(value2)
	print(domain3)#输出3~30内可以被3整除的数字
	
domain4=[]
for value3 in range(1,11):
	domain4.append(value3**3)
	print(domain4)#前十个整数的3次方
	
domain5=list(value4**3 for value4 in range(1,11))
print(domain5)
	
