a = int(input("请输入第一个整数: "))
b = int(input("请输入第二个整数: "))
print(str.format("输入值: {0}, {1}", a, b))
if (a < b):
    t = a
    a = b
    b = t
print(str.format("降序值: {0}, {1}, {2}, {2}, {0}", a, b, 12))    
