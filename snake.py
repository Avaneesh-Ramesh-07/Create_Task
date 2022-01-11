import turtle as t
import time

#initialize window
window=t.Screen()
window.title("Snake Game - Avaneesh R. and Anvay T.")
window.bgcolor("lightgreen")
t.shape("square")

#defining movement functions
def up():
  #faces turtle up
  if t.heading()!="down":
      t.seth(90)

def down():
  #faces turtle down
  if t.heading() != "up":
      t.seth(270)

def left():
  #faces turtle left
  if t.heading() != "right":
      t.seth(180)

def right():
  #faces turtle right
  if t.heading()!="left":
      t.seth(0)
#defining other functions
def go_to(x,y):
  #function to move turtle based on parameters x and y coordinates
  t.penup()
  t.goto(x,y)
  t.pendown()

def check_loss(x, y):
  #function to check if the user lost
  if x > (221) or x <-221 or  y > (221) or  y < -221:
      return -1
def move():
  #moves the turtle based on its current heading
  t.speed(0.5)
  t.penup()
  if t.heading()==90:
    if check_loss(t.xcor(), t.ycor()+26)==-1:
        t.setpos(0,0)
    else:
        t.sety(t.ycor()+26)
        time.sleep(0.1)
  if t.heading()==270:
    if check_loss(t.xcor(), t.ycor()-26)==-1:
        t.setpos(0,0)
    else:
        t.sety(t.ycor()-26)
        time.sleep(0.1)
  if t.heading()==0:
    if check_loss(t.xcor()+26, t.ycor())==-1:
        t.setpos(0,0)
    else:
        t.setx(t.xcor()+26)
        time.sleep(0.1)
  if t.heading()==180:
    if check_loss(t.xcor()-26, t.ycor())==-1:
        t.setpos(0,0)
    else:
        t.setx(t.xcor()-26)
        time.sleep(0.1)


#makes a grid for the board

t.speed(1000)
t.turtlesize(1.3)
go_to(-(442/2), -(441/2))
t.lt(90)
for i in range(4):
  for i in range(17):
      t.forward(26)
      t.right(90)
      t.fd(442)
      t.bk(442)
      t.left(90)
  t.right(90)
go_to(0,0)

#creating food
food = t.Turtle()
colors = 'red'
shapes = 'circle'
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 78)



#event listeners
t.listen()
t.onkey(up, "Up")  #call "up" function if up arrow key is pressed
t.onkey(down, "Down") #call "down" function if down arrow key is pressed
t.onkey(left, "Left") #call "left" function if left arrow key is pressed
t.onkey(right, "Right") #call "right" function if right arrow key is pressed


while True:
  #while loop that will run facilitating the main snake game
  t.update()
  move()
t.mainloop() #keeps window open


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


