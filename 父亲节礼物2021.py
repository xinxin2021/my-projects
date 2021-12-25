# coding=utf-8
import turtle

pen = turtle.Pen()

pen.penup()
pen.goto(0, -250)  # 初始化位置
pen.pendown()

pen.setheading(90)  # 向上
pen.fillcolor('#ff0000')  # 填充颜色：红色
# 绘制过程
pen.begin_fill()
pen.forward(500)
pen.left(90)
pen.forward(300)
pen.left(90)
pen.forward(500)
pen.left(90)
pen.forward(600)
pen.left(90)
pen.forward(500)
pen.left(90)
pen.forward(300)
pen.end_fill()

pen.penup()
pen.goto(-205, 70)
pen.pendown()
pen.write('父',font=('Arial',90,'bold'))  # 打印文字：父，字体：Arial，字号：90，类型：加粗
pen.penup()
pen.goto(-205, -60)
pen.pendown()
pen.write('亲',font=('Arial',90,'bold'))
pen.penup()
pen.goto(-205,-200)
pen.write('节',font=('Arial',90,'bold'))
pen.penup()
pen.goto(90, 70)
pen.pendown()
pen.write('快',font=('Arial',90,'bold'))
pen.penup()
pen.goto(90,-200)
pen.write('乐',font=('Arial',90,'bold'))

turtle.done()  # 结束，不会一下子关掉