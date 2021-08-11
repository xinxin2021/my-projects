# coding=utf-8
import turtle as t
import time

t.fillcolor("#FFFFCC")
t.begin_fill()
t.penup()
t.goto(-200,100)  #初始位置在-150,100,
t.right(90)
t.pendown()
t.fd(150)
t.circle(50,90)
t.fd(300)
t.circle(50,90)
t.fd(150)
t.left(66)
t.circle(493,48)
t.left(66)
t.end_fill()
#=============================蛋糕的外框

t.penup()
t.goto(-200,50)
t.pendown()

t.left(60)
t.fd(20)
t.circle(10,70)
t.fd(50)
t.circle(-10,70)
t.fd(60)
t.circle(10,70)
t.fd(50)
t.circle(-10,70)
t.fd(60)
t.circle(10,70)
t.fd(50)
t.circle(-10,70)
t.fd(60)
t.circle(10,70)
t.fd(42)
#=============================绘制奶酪

t.penup()
t.goto(-200,100)
t.pendown()

#=============================移到最初的起点

t.fillcolor("#5cb85c")
t.begin_fill()          #第一个圈
t.left(90)
t.circle(-20,220)
t.end_fill()

t.fillcolor("#cca4e3")
t.begin_fill()         #第二个圈
t.left(200)
t.circle(-23,185)
t.end_fill()

t.fillcolor("#5cb85c")
t.begin_fill()          #第三个圈
t.left(180)
t.circle(-22,185)
t.end_fill()

t.fillcolor("#5AA9F3")
t.begin_fill()          #第四个圈
t.left(180)
t.circle(-20,186)
t.end_fill()

t.fillcolor("blue")
t.begin_fill()          #第五个圈
t.left(180)
t.circle(-20,183)
t.end_fill()

t.fillcolor("yellow")
t.begin_fill()          #第六个圈
t.left(180)
t.circle(-20,190)
t.end_fill()

t.fillcolor("orange")
t.begin_fill()
t.left(180)
t.circle(-21,177)
t.end_fill()

t.fillcolor("brown")
t.begin_fill()
t.left(180)
t.circle(-20,190)
t.end_fill()

t.fillcolor("purple")
t.begin_fill()
t.left(190)
t.circle(-20,200)
t.end_fill()

t.fillcolor("pink")
t.begin_fill()
t.left(195)
t.circle(-22,204)
t.end_fill()

#===================================绘制蛋糕上的花瓣

t.penup()
t.goto(-130,140)
t.left(215)
t.pendown()
t.fd(90)
t.right(90)
t.fd(10)
t.left(185)
t.fillcolor("#ff2d51")
t.begin_fill()
t.circle(-10,180)
t.circle(10,180)
t.left(180)
t.circle(-20,180)
t.end_fill()
t.fillcolor("yellow")
t.begin_fill()
t.left(175)
t.fd(10)
t.right(90)
t.fd(79)
t.end_fill()

#========================第一个蜡烛,接下来是第二个蜡烛

t.penup()
t.goto(120,140)
t.left(180)
t.pendown()
t.fd(90)
t.right(90)
t.fd(10)
t.left(185)
t.fillcolor("#ff2d51")
t.begin_fill()
t.circle(-10,180)
t.circle(10,180)
t.left(180)
t.circle(-20,180)
t.end_fill()
t.fillcolor("yellow")
t.begin_fill()
t.left(175)
t.fd(10)
t.right(90)
t.fd(85)
t.end_fill()

#=========================第二支蜡烛

t.penup()
t.goto(0,-30)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.right(90)
t.fd(15)
t.goto(0,-50)
t.goto(15,-30)
t.goto(0,-30)
t.end_fill()

t.penup()
t.goto(-70,30)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10,360)
t.end_fill()

t.penup()
t.goto(70,30)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10,360)
t.end_fill()

#============两只眼睛一张嘴

time.sleep(3)
# t.right(90)
# t.fd(100)    #向前方画100像素
# t.left(90)  #向右旋转90度
# t.fd(150)
# t.left(90)
# t.pendown()
# t.fd(150)
# t.left(90)
# t.circle(100,45)
#==============================设置初始位置


# t.circle(200, 45)
# t.left(90)
# t.circle(200, 90)
# t.left(90)
# t.circle(200, 45)
# #===============================绘制顶部半圆
#
#
# t.penup()
# t.goto(-140,160)
# t.right(90)
# t.pendown()
# t.goto(-140,20)
