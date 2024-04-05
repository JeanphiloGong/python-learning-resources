[ i**2 for i in range(10)]  #平方值
[(i, i**2) for i in range(10)]#序号，平方根
[i for i in range(10) if 1%2==0]#取偶数
[(x, y, x*y) for x in range(1, 4) for y in range(1, 4) if x >=y]
