import math
m = int(input("请输入一个整数(>1): "))
k= int(math.sqrt(m))
flag = True
i = 2
while (i <= k and flag == True):
    if (m % i == 0): flag = False
    else: i += 1
if (flag == True): print(m, "是素数")
else: print(m, "是合数！")
