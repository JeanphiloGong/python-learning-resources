import turtle
def draw_polygon(sides, side_len):#绘制指定边长度的多边形
    for i in range(sides):
        turtle.forward(side_len)#绘制边长
        turtle.left(360.0/sides)#旋转角度
def main():
    for i in range(9,10):# 绘制三角形、正方形、正五边形、
        step = 50
        draw_polygon(i, step)
if __name__ == '__main__': main()
