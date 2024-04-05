y = float(input("请输入y:"))
if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
    print("是闰年")
else:print("不是闰年")
