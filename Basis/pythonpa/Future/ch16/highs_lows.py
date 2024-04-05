import csv

import pygal

from matplotlib import pyplot as plt
filename = '返校相关数据.csv'
with open(filename) as f:
    reader = csv.reader(f)#分析文件中的数据
    header_row = next(reader)
    #从文件中获取大家的返校日期
    names = []
    for row in reader:
        name = int(row[8])
        names.append(name)

print(len(names))

#对得到的返校时期进行分析
numbers = []
for value in range(217,220):
    number = names.count(value)
    numbers.append(number)

#对结果进行可视化
hist = pygal.Bar()

hist.title = 'Back To School Date Statistics'
hist.x_labels =[]
for i in range(217,220):
    hist.x_labels.append(i)
hist.x_title = "Date"
hist.y_title = "Statistics of date"

hist.add('Person',numbers)
hist.render_to_file('Statistics of date.svg')