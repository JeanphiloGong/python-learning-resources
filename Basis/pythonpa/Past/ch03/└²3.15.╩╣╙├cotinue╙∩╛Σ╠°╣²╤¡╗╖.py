num = 0; scores = 0;
while True:
    s = input('请输入学生成绩(按Q或q结束):')
    if s.upper() == 'Q':
        break
    if float(s) < 0:
        continue
    num += 1
    scores += float(s)
print('学生人数为:{0},平均成绩为:{1}'.format(num,scores / num))
