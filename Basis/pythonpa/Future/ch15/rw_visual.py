import matplotlib.pyplot as plt

from random_walk import RandomWalk

#只要程序处于活动状态，就不断地模拟随机漫步
while True:
#创建一个随件漫步示例，并将其包含的点都绘制出来
	rw = RandomWalk(5000)
	rw.fill_walk()
	plt.figure(dpi=1680,figsize=(10,6))
	point_numbers = list(range(rw.num_points))
	
	#隐藏坐标轴
	current_axes = plt.axes()
	current_axes.get_xaxis().set_visible(False)
	current_axes.get_yaxis().set_visible(False)
	plt.plot(rw.x_values,rw.y_values,linewidth=0.1)
		   
	#突出起点和终点
	plt.plot(0,0,c='green')
	plt.plot(rw.x_values[-1],rw.x_values[-1])
	    

		   

	plt.show()
	
	keep_running = input("Make another walk?(y/n): ")
	if keep_running == 'n':
		break

