import math
a = float(input("请输入三角形的边长a:"))
b = float(input("请输入三角形的边长b:"))
c = float(input("请输入三角形的边长c:"))
h = (a + b + c)/2
area = math.sqrt( h * (h-a) * (h-b) * (h-c))
print(a, b, c)
print(area)
