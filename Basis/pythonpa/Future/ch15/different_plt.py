from die import Die
import matplotlib.pyplot as plt

#创建一个D6
die_1 = Die()
die_2 = Die(10)

#掷几次骰子，并将结果存储在一个列表之中
results = []
for roll_num in range(10000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
	
#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
#对结果进行可视化
x_values = [x for x in range(1,17)]
y_values = frequencies
plt.scatter(x_values,y_values,c = y_values,cmap=plt.cm.Blues,
     edgecolor = 'none',s =10)
     
#设置标题
plt.title ('RESULRS of TWO DIE',fontsize =14)
plt.xlabel("Result",fontsize =14)
plt.ylabel("Frencies of Result",fontsize = 14)

#设置刻度的大小
plt.tick_params(axis = 'both',which = 'major',labelsize =14)


plt.show()


