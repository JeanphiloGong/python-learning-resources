j = 0
print('100-200之间不能被3整除的数为: ')
for i in range (100, 200 + 1):
    if (i % 3 == 0): continue
    print(str.format("{0:<5}",i), end="")
    j += 1
    if (j % 10 ==0): print()
