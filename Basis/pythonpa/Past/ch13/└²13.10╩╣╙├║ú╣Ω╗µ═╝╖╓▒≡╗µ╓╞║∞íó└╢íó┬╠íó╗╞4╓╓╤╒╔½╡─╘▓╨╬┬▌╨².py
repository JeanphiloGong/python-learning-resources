import turtle
p = turtle.Turtle()#创建海龟对象
p.speed(0)#定义绘图的速度“fasest"或者0均表示最快”
colors = ["red", "blue", "green", "yellow"]
for i in range(100):
    p.pencolor(colors[i%4])
    p.circle(i)
    p.left(91)
