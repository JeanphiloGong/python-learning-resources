#coding=utf-8
dimensions =(200,50)#元组中的元素是不可以修改的，调用规则和列表是类似的
print(dimensions[0])
print(dimensions[1])


dimensions[0] = 250#元组元素不可以被修改，会导致PYthon进行报错
print(dimensions)
