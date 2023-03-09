import turtle as t
from turtle import *
import random as r
import time

n = 100.0
t.delay(0)
speed("fastest")
screensize(bg='black')


def bgpic(self, picname=None):
    if picname is None:
        return self._bgpicname
    if picname not in self._bgpics:
        self._bgpics[picname] = self._image(picname)
    self._setbgpic(self._bgpic, self._bgpics[picname])
    self._bgpicname = picname


if __name__ == '__main__':
    myWin = t.Screen()
    t.setup(width=600, height=750, startx=0, starty=0)
    t.bgpic('1.gif')  # 这里设置本地图片地址，建议是gif图片

left(90)
forward(3 * n)
color("orange", "yellow")
begin_fill()
left(126)
for i in range(5):
    forward(n / 5)
    right(144)
    forward(n / 5)
    left(72)
end_fill()
right(126)


def drawlight():
    if r.randint(0, 50) == 0:  # 如果觉得彩灯太多，可以把取值范围加大一些，对应的灯就会少一些
        color('tomato')
        begin_fill()
        circle(6)
        end_fill()
    elif r.randint(0, 50) == 1:
        color('orange')
        begin_fill()
        circle(3)
        end_fill()
    elif r.randint(0, 50) == 2:
        color('pink')
        begin_fill()
        circle(2)
        end_fill()
    else:
        pensize(5)
        color('green')


pensize(5)
color("dark green")
backward(n * 5)


def tree(d, s):
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    drawlight()  # 同时画小彩灯
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)


tree(15, n)
backward(n / 2)

for i in range(200):
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:
        pensize(1)
        color('tomato')
    else:
        pensize(1)
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)

t.color("dark red", "red")
t.write("Merry Christmas", align="center", font=("Comic Sans MS", 30, "bold"))  # 写字
penup()
left(180)
backward(50)
pendown()
t.write("To Mr.Shi", align="center", font=("Comic Sans MS", 30, "bold"))  # 写字


def drawsnow():
    t.ht()  # 隐藏笔头，ht=hideturtle
    t.pensize(2)  # 定义笔头大小
    for i in range(200):  # 画多少雪花
        t.pencolor("white")  # 定义画笔颜色为白色，其实就是雪花为白色
        t.pu()  # 提笔，pu=penup
        t.setx(r.randint(-350, 350))  # 定义x坐标，随机从-350到350之间选择
        t.sety(r.randint(-100, 350))  # 定义y坐标，注意雪花一般在地上不会落下，所以定义是从1开始
        t.pd()  # 落笔，pd=pendown
        dens = 6  # 雪花瓣数设为6
        snowsize = r.randint(1, 10)  # 定义雪花大小
        for j in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
            # t.forward(int(snowsize))  #int（）取整数
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            # t.bd(int(snowsize))  #注意没有bd=backward，但有fd=forward，小bug
            t.right(int(360 / dens))  # 转动角度


drawsnow()  # 画雪花
t.done()  # 完成,否则会直接关闭
# time.sleep(60)
