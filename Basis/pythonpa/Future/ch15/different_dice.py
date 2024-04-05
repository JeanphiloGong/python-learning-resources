from die import Die
import pygal

#创建一个D6
die_1 = Die()
die_2 = Die(10)

#掷几次骰子，并将结果存储在一个列表之中
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
	
#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results if rolling one D6 1000 times"
hist.x_labels = []
for i in range(1,17):
	hist.x_labels.append(i)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice.svg')

