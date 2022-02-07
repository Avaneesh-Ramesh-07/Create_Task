"""This is the code for the Create Task. We have created the Snake Game"""


#importing packages
import turtle as t
import time
import random

#initialize window and creates the turtle 
window=t.Screen()
window.title("Snake Game")

#creating a list so that the gifs for the apple, banana, mango, pepper, cherry, orange, and lemon load
shape_list=['apple.gif', 'banana.gif', 'mango.gif', 'pepper.gif', 'cherry.gif', 'orange.gif', 'lemon.gif']
for i in shape_list:
  window.addshape(i)
window.colormode(255)
t.colormode(255)
window.bgcolor(144,238,144)

delay=0.15

t.shape("circle")

#defining functions 
def up():
  #faces turtle up
  if t.heading()!=270:
    t.seth(90)

def down():
  #faces turtle down
  if t.heading() != 90:
      t.seth(270)

def left():
  #faces turtle left
  if t.heading() != 0:
      t.seth(180)

def right():
  #faces turtle right
  if t.heading()!=180:
      t.seth(0)

def go_to(x,y):
  #function to move turtle based on parameters x and y coordinates
  t.penup()
  t.goto(x,y)
  t.pendown()

def check_loss(x, y, turtle_dict):
  #function to verify if the user lost or not (checks the x and y coordinates)
  if x > (221) or x <-221 or  y > (221) or  y < -221:
      return -1
  if (x,y) in turtle_dict.values():
    return -1

def game_finished(score):
  #function to execute when the player loses the game, clears the screen, outputs a thanks message. 
  t.clearscreen()
  window.bgcolor("lightgreen")
  t.ht()
  t.pu()
  #Game-Ending text
  t.write("Thanks for playing! :)\nYou had a final score of " + str(score) + "!\nThis means you ate "+ str(score) + " piece(s) of food!\nHope you had lots of fun playing our game!\nRerun the program to play again!", font=("Helvetica", 15, "normal") ,align="center")
  time.sleep(7)
  exit()
# Score function that adds plus one score when you eat a piece of food. 
def move(delay, turtle_dict):
  score=len(turtle_dict.keys())-1
  #moves the turtle based on its current heading
  t.speed(0.5)
  t.penup()
  if t.heading()==90:
    if check_loss(t.xcor(), t.ycor()+26, turtle_dict)==-1:
        game_finished(score)
    else:
        t.sety(t.ycor()+26)
        time.sleep(delay)
  if t.heading()==270:
    if check_loss(t.xcor(), t.ycor()-26, turtle_dict)==-1:
        game_finished(score)
    else:
        t.sety(t.ycor()-26)
        time.sleep(delay)
  if t.heading()==0:
    if check_loss(t.xcor()+26, t.ycor(), turtle_dict)==-1:
        game_finished(score)
    else:
        t.setx(t.xcor()+26)
        time.sleep(delay)
  if t.heading()==180:
    if check_loss(t.xcor()-26, t.ycor(), turtle_dict)==-1:
        game_finished(score)
    else:
        t.setx(t.xcor()-26)
        time.sleep(delay)

def update_food(status_dict, turtle_dict):
  #student defined function to update the food
  if True not in status_dict.values():
    possible_pos=[]
    for i in range(10):
      pos=((26*random.randint(-8,8)), 26*random.randint(-8,8))
      
      possible_pos.append(pos)
    possible_pos=list(set(possible_pos)) #removes duplicates
    for position in possible_pos:
      if position in turtle_dict.values():

        possible_pos.remove(position)
    status_dict={}
    for i in range(3):
        food = t.Turtle(visible=False)
        shape=shape_list[random.randint(0, len(shape_list)-1)]
        
        colors = 'red'
        food.turtlesize(stretch_wid=1.3,
                      stretch_len=1.3)
        food.shape(shape)
        food.color(colors)
        food.speed(1000)
        food.penup()
        random_pos=possible_pos[random.randint(0, len(possible_pos)-1)]
        food.goto(random_pos[0], random_pos[1])
        food.st()
        possible_pos.remove(random_pos)
        status_dict[food]=True
        updated_dict=status_dict
    return updated_dict #returns the updated version of the dictionary that has all the just generated food
  else:

    return status_dict #return the same version of the dictionary

def add_new_turtle(turtle_dict, r, g, b, delay):
  #creates additional turtles stemming from the apples
  if delay-0.01>0:
    delay-=0.01
  else:
    delay=0
  created_turtle=t.Turtle(visible=False)
  created_turtle.color(r, g, b)
  created_turtle.speed(7)
  created_turtle.penup()
  created_turtle.shape('circle')
  created_turtle.st()
  keys=list(turtle_dict.keys())
  created_turtle.goto(turtle_dict[t])
  turtle_dict[created_turtle]=created_turtle.pos()
  return turtle_dict, delay

#creates a 442x442 grid for the snake board
t.ht()
t.speed(0)
go_to(-(442/2), -(441/2))
t.lt(90)

for i in range(4):
  for i in range(17):
      t.color(42, 107, 7)
      t.forward(26)
      t.right(90)
      t.color(84, 212, 15)
      t.fd(442)
      t.bk(442)
      t.left(90)
  t.right(90)
t.color(42, 107, 7)
t.seth(90)
t.fd(442)
go_to(0,0)
t.color("black")
t.st()

#event listeners
t.listen()
t.onkey(up, "Up")  #call "up" function if up arrow key is pressed
t.onkey(down, "Down") #call "down" function if down arrow key is pressed
t.onkey(left, "Left") #call "left" function if left arrow key is pressed
t.onkey(right, "Right") #call "right" function if right arrow key is pressed

#status dictionary that keeps track of the turtle objects and their positions.
status_dict={}
turtle_dict={t:(0,0)}
#first call of the update_food to make sure food doesn't get placed on where turtle spawns.
status_dict=update_food(status_dict, turtle_dict)

#definition of r, g, b values that will be used to change color for every subsequent part of the snake; to give vibrancy. 
r=0
b=20
g=0

while True:
  #while loop that will run facilitating the main snake game and confirms that there are three apples on the board at all times
  t.update()
  status_dict=update_food(status_dict, turtle_dict)
  for i in status_dict:
    if t.pos() == i.pos():
      #checks if the head is on the same square as an apple
      status_dict[i]=False
      i.ht()
      #adjusts color for each new turtle being spawned in      
      r+=10
      g+=10
      b+=10
      if b > 255:
        b=0
        r=20
        g=0
      if r > 255:
        b=20
        r=0
        g=0
      
      output_list=add_new_turtle(turtle_dict, r, g, b, delay)
      turtle_dict=output_list[0] #updates the turtle dictionary
      delay=output_list[1]
  
  for turtle in turtle_dict:
    #updates turtle dictionary with new positions
    turtle_dict[turtle]=turtle.pos()
  turtle_objects=list(turtle_dict.keys())
  for i in range(1, len(turtle_objects)):
     #logic for moving snake, each turtle (apart from head) goes to the previous turtle's previous position.
    if i != len(turtle_objects):
      turtle_objects[i].goto(turtle_dict[turtle_objects[i-1]])
  
  move(delay, turtle_dict) #moves head
  time.sleep(0.12) #adds small delay to make everything smoother while moving the turtle
window.mainloop() #keeps turtle window open