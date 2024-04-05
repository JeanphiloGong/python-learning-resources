from die import Die
import pygal

#创建一个D6
die_1 = Die()
die_2 = Die()
die_3 = Die()
die_4 = Die()

#掷几次骰子，并将结果存储在一个列表之中
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll() + die_3.roll() +die_4.roll()
	results.append(result)
	
#分析结果
frequencies = []

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides + die_4.num_sides
for value in range(1,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results if rolling two D6 1000 times"
hist.x_labels = ['1', '2', '3' , '4', '5', '6',]
for i in range(7,25):
	hist.x_labels.append(i)
hist.x_title = "Result"
hist.y_title = "Frequency if Result"

hist.add('Four D6', frequencies)
hist.render_to_file('die_visual.svg')

