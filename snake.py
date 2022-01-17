#importing packages
import turtle as t
import time
import random

#initialize window
window=t.Screen()
window.title("Snake Game - Avaneesh R. and Anvay T.")
window.bgcolor("lightgreen")
t.shape("square")
window.colormode(255)


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
  delay=0.06
  #moves the turtle based on its current heading
  t.speed(0.5)
  t.penup()
  if t.heading()==90:
    if check_loss(t.xcor(), t.ycor()+26)==-1:
        t.setpos(0,0)
    else:
        t.sety(t.ycor()+26)
        time.sleep(delay)
  if t.heading()==270:
    if check_loss(t.xcor(), t.ycor()-26)==-1:
        t.setpos(0,0)
    else:
        t.sety(t.ycor()-26)
        time.sleep(delay)
  if t.heading()==0:
    if check_loss(t.xcor()+26, t.ycor())==-1:
        t.setpos(0,0)
    else:
        t.setx(t.xcor()+26)
        time.sleep(delay)
  if t.heading()==180:
    if check_loss(t.xcor()-26, t.ycor())==-1:
        t.setpos(0,0)
    else:
        t.setx(t.xcor()-26)
        time.sleep(delay)
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
    pos=((26*random.randint(-8,8)), 26*random.randint(-8,8))
    
    possible_pos.append(pos)
  possible_pos=list(set(possible_pos)) #removes duplicates
  print(possible_pos)
  status_dict={}
  for i in range(3):
      food = t.Turtle()
      food.ht()
      colors = 'red'
      shapes = 'circle'
      food.shape(shapes)
      food.color(colors)
      food.speed(1000)
      food.penup()
      random_pos=possible_pos[random.randint(0, len(possible_pos)-1)]
      food.goto(random_pos[0], random_pos[1])
      food.st()
      possible_pos.remove(random_pos)
      status_dict[food]=True
  return status_dict

#creates multiple turtles from the apples
def add_new_turtle(turtle_dict, r, g, b):
  print(r)
  print(g)
  print(b)
  created_turtle=t.Turtle()
  created_turtle.color(r, g, b)
  created_turtle.speed(10000)
  created_turtle.penup()
  created_turtle.shape('square')
  created_turtle.turtlesize(1.3)
  keys=list(turtle_dict.keys())
  #print(turtle_dict)
  created_turtle.goto(turtle_dict[t])
  turtle_dict[created_turtle]=created_turtle.pos()
  return turtle_dict

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
      
      """r+=2*(random.randint(1,3))
      g+=2*(random.randint(1,3))
      b+=2*(random.randint(1,3))
      if r > 255:
        r=2
      if g > 255:
        g=2
      if b > 255:
        b=2"""
      r=random.randint(20,255)
      g=random.randint(20,255)
      b=random.randint(20,255)
      turtle_dict=add_new_turtle(turtle_dict, r, g, b)
  for turtle in turtle_dict:
    turtle_dict[turtle]=turtle.pos()
  keys=list(turtle_dict.keys())
  for i in range(1, len(keys)):
    if i != len(keys):
      keys[i].goto(turtle_dict[keys[i-1]])
  
  move()
t.mainloop() #keeps window open