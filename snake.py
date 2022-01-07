
import turtle as t
import keyboard
import time
def up():
    if check_loss() == -1:
        print("you lost")
    else:
        if t.heading()!="down":
            t.seth(90)

def down():
    if check_loss() == -1:
        print("you lost")
    else:
        if t.heading() != "up":
            t.seth(270)

def left():
    if check_loss() == -1:
        print("you lost")
    else:
        if t.heading() != "right":
            t.seth(180)

def right():
    if check_loss() == -1:
        print("you lost")
    else:
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

def check_loss():
    if x == (208) or x == -208 or  y == (208) or  y == -208:
        return -1

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
x=0
y=0
go_to(x,y)
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
    move_turtle()
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


