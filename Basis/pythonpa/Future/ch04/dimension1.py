#coding=utf-8
dimensions =(200,50)#元组中的元素是不可以修改的，调用规则和列表是类似的
print(dimensions[0])
print(dimensions[1])


for dimension in dimensions:#对元组中所有元素进行遍历
	print(dimension)

dimensions = (400,100)
print("\n Modiified dimensions:")
for dimension in dimensions:
	print(dimension)
