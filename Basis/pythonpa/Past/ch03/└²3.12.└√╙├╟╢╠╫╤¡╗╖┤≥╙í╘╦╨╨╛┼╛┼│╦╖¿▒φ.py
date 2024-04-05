for i in range(1, 10):#阶梯向上
    s = ""
    for j in range(i+1,10):
        s += str.format("{0:1}*{1:1}={2:>2}   ",  i,  j,  i * j)
    print(s)
    
for i in range(1, 10):#下三角
    s = ""
    for j in range(1,i+1):
        s += str.format("{0:1}*{1:1}={2:>2}   ",  i,  j,  i * j)
    print(s)
    
for i in range(1, 10):  #九九乘法表
    s = ""
    for j in range(1,10):
        s += str.format("{0:1}*{1:1}={2:>2}   ",  i,  j,  i * j)
    print(s)

