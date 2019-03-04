import turtle
import math
#定义多个坐标
x1,y1=100,100
x2,y2=100,-100
x3,y3=-100,-100
x4,y4=-100,100

#绘制折线
#turtle抬笔
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()

turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)
#计算起始点与终点的距离
#第一种计算距离的方法，引入了math
# distance =math.sqrt((x1-x4)**2+(y1-y4)**2)
# turtle.write(distance)

#第二种计算距离的方法，没有引入math,分步计算的，经过检验程序是没有错误的
# a=(x1-x4)**2
# b=(y1-y4)**2
# c=(a+b)**0.5
# turtle.write(c)

#第三种计算距离的方法，引入math,使用的**0.5计算开方，经过检验程序是没有错误的
distance =((x1-x4)**2+(y1-y4)**2)**0.5
turtle.write(distance)