
import turtle as t
import keyboard
import time
def up():
    if t.heading()!="down":
        t.seth(90)

def down():
    if t.heading() != "up":
        t.seth(270)

def left():
    if t.heading() != "right":
        t.seth(180)

def right():
    if t.heading()!="left":
        t.seth(0)
def move_turtle():
    t.forward(26)

window=t.Screen()
window.title("Snake Game")
window.bgcolor("green")

def go_to(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
t.speed(1000)
t.turtlesize(1.3)
go_to(-(442/2), -(441/2))
t.lt(90)

def check_loss(x, y):
    if x == (208) or x == -208 or  y == (208) or  y == -208:
        return -1
def move():
    if t.heading()==90:
        if check_loss(t.xcor(), t.ycor()+26)==-1:
            t.setpos(0,0)
        else:
            t.sety(t.ycor()+0.1)
    if t.heading()==270:
        if check_loss(t.xcor(), t.ycor()-26)==-1:
            t.setpos(0,0)
        else:
            t.sety(t.ycor()-26)
    if t.heading()==0:
        if check_loss(t.xcor()+26, t.ycor())==-1:
            t.setpos(0,0)
        else:
            t.setx(t.xcor()+26)
    if t.heading()==180:
        if check_loss(t.xcor()-26, t.ycor())==-1:
            t.setpos(0,0)
        else:
            t.setx(t.xcor()-26)


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
go_to(0,0)
"""
def go_up():
    if check_loss() == -1:
        print("you lost")
    y += 26

    go_to(x, y)
    time.sleep(0.25)
def go_down():
    if check_loss() == -1:
        print("you lost")
    y -= 26

    go_to(x, y)
    time.sleep(0.25)
def go_right():
    if check_loss() == -1:
        print("you lost")
    x += 26

    go_to(x, y)
    time.sleep(0.25)
def go_left():
    if check_loss() == -1:
        print("you lost")
    x-= 26

    go_to(x, y)
    time.sleep(0.25)"""



t.listen()

t.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
t.onkey(down, "Down")
t.onkey(left, "Left")
t.onkey(right, "Right")


while True:
    t.update()

    move()
t.mainloop()

"""


#setting up board

while True:
    if keyboard.read_key()=='w' and t.heading() != 180:
        if check_loss()==-1:
            print("you lost")
        y+=26

        go_to(x,y)
        time.sleep(0.25)
    elif keyboard.read_key()=='a' and t.heading() != 270:
        if check_loss()==-1:
            print("you lost")
        x-=26

        go_to(x,y)
        time.sleep(0.25)
    elif keyboard.read_key()=='s' and t.heading() != 0:
        if check_loss()==-1:
            print("you lost")
        y-=26

        go_to(x,y)
        time.sleep(0.25)
    elif keyboard.read_key()=='d' and t.heading() != 90:
        if check_loss()==-1:
            print("you lost")
        x+=26

        go_to(x,y)
        time.sleep(0.25)
    print(t.heading())"""


