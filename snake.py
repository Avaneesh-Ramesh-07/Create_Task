import turtle
import keyboard
import time
"""
window=turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")"""
t=turtle.Turtle('square')


def create_board():
    t.speed(1000)
    t.turtlesize(1.3)
    go_to(-(442/2), -(441/2))
    t.lt(90)
    #makes a grid for the board
    for i in range(4):
        for i in range(17):
            t.forward(26)
            t.right(90)
            t.fd(442)
            t.bk(442)
            t.left(90)
        t.right(90)
    t.speed(100)
def go_to(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#setting up board
create_board()
x=0
y=0
go_to(x,y)
def check_loss():
    if x == (208) or x == -208 or  y == (208) or  y == -208:
        return -1
while True:

    if keyboard.read_key()=='w' and t.heading() != 180:
        if check_loss()==-1:
            break
        y+=26

        go_to(x,y)
        time.sleep(0.25)
    elif keyboard.read_key()=='a' and t.heading() != 270:
        if check_loss()==-1:
            break
        x-=26

        go_to(x,y)
        time.sleep(0.25)
    elif keyboard.read_key()=='s' and t.heading() != 0:
        if check_loss()==-1:
            break
        y-=26

        go_to(x,y)
        time.sleep(0.25)
    elif keyboard.read_key()=='d' and t.heading() != 90:
        if check_loss()==-1:
            break
        x+=26

        go_to(x,y)
        time.sleep(0.25)
    print(t.heading())


