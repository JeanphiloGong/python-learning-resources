#coding=utf-8
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  #对列表进行输出
motorcycles.append('ducati')
print(motorcycles)#在列表末尾添加元素
motorcycles.insert(0,'ducati')
print(motorcycles)#在列表特定位置添加元素
del motorcycles[0]
print(motorcycles)#利用del语句删除元素
poped_motorcycles = motorcycles.pop()#可以利用pop（）方法将列表中最后一个元素删除而且将其提出
print(motorcycles)
print(poped_motorcycles)
last_owned = motorcycles.pop()
print("The last motorcycles I owned was a " + last_owned.title() + ".\n")
#可以利用pop（）语句得到最后列表中最后一个元素的值并机械能输出
first_owned = motorcycles.pop(0)#可以利用元素的序号将元素从列表中提出
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles.remove('yamaha')#可以利用元素的值通过remove（）直接将元素从列表中删除
print(motorcycles)

motorcycles.append('yamaha')
too_expensive = 'yamaha'#设置一个新的变量进行运行程序
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive +" is too expensive for me")
