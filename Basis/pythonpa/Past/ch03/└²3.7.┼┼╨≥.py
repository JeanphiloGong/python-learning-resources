a = float(input("请输入a:"))
b = float(input("请输入b:"))
c = float(input("请输入c:"))
if (a < b): t = a; a = b; b = t
if (a < c): t = a; a = c; c = t
if (b < c): t = b; b = c; c = t
print("排序结果(降序): ", a, b, c)

