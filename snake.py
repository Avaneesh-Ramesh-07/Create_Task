#importing packages
import turtle as t
import time
import random

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
def move(turtle_dict):
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
def update_food(status_dict):
  """needs_replenish=True
  if status_dict is not None:
    for key in status_dict:
      if status_dict[key]==True:
        print("here")
        needs_replenish=False
  if needs_replenish==True:"""
  possible_pos=[]
  for i in range(10):
    possible_pos.append(((26*random.randint(-8,8)), 26*random.randint(-8,8)))
  possible_pos=list(set(possible_pos)) #removes duplicates
  print(possible_pos)
  status_dict={}
  for i in range(3):
      food = t.Turtle()
      colors = 'red'
      shapes = 'circle'
      food.shape(shapes)
      food.color(colors)
      food.speed(1000)
      food.penup()
      random_pos=possible_pos[random.randint(0, len(possible_pos)-1)]
      food.goto(random_pos[0], random_pos[1])
      possible_pos.remove(random_pos)
      status_dict[food]=True
  return status_dict


#creates multiple turtles from the apples
def add_new_turtle(turtle_dict):
  created_turtle=t.Turtle()
  created_turtle.penup()
  created_turtle.shape('square')
  created_turtle.turtlesize(1.3)
  created_turtle.goto(turtle_dict[t])
  turtle_dict[created_turtle]=created_turtle.pos()


    






#makes a 442x442 grid for the board

t.speed(1000000000)
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






#event listeners
t.listen()
t.onkey(up, "Up")  #call "up" function if up arrow key is pressed
t.onkey(down, "Down") #call "down" function if down arrow key is pressed
t.onkey(left, "Left") #call "left" function if left arrow key is pressed
t.onkey(right, "Right") #call "right" function if right arrow key is pressed

status_dict={}
status_dict=update_food(status_dict)
turtle_dict={t:(0,0)}
while True:

  #while loop that will run facilitating the main snake game and confirms that there are three apples on the board at all times
  t.update()
  if True not in status_dict.values():
    status_dict=update_food(status_dict)
  for i in status_dict:
    if t.pos() == i.pos():
      status_dict[i]=False
      i.ht()
      add_new_turtle(turtle_dict)
   

  
  
  turtle_dict[t]=t.pos()
  move()
t.mainloop() #keeps window open

