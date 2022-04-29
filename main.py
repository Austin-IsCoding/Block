#Libraries
import turtle
from random import*
from math import*
import os
import time

#Defenitions And Variables
xpos = 0
ypos = 0
rp = randint(-180,180)
hp = 5

def rs(input):
  turtle.register_shape(input)
def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
def a_up():
  global ypos
  ypos += 15
def a_down():
  global ypos
  ypos -= 15
def a_left():
  global xpos
  xpos -= 15
def a_right():
  global xpos
  xpos += 15


#Sprite Setup
rs("wolfox.gif")
rs("wolfoxopen.gif")
rs("wolfoxbite.gif")
rs("reddy.gif")
rs("hp0.gif")
rs("hp1.gif")
rs("hp2.gif")
rs("hp3.gif")
rs("hp4.gif")
rs("hp5.gif")

#Character Setup
enemy = turtle.Turtle()
a = turtle.Turtle()
h = turtle.Turtle()
h.shape("hp5.gif")
h.penup()
h.goto(-185,170)
a.shape("square")
scr = turtle.Turtle()
enemy.shape("wolfox.gif")
enemy.penup()
scr.hideturtle()
a.speed(1)
a.fillcolor("white")

#Screen Setup
S = turtle.Screen()
S.bgcolor('lightgreen')

#Final Setup
clearconsole()
a.penup()
turtle.listen()
clearconsole()

#Game Loop
running = True
while running:
  #HP
  if hp == 5:
    h.shape("hp5.gif")
  elif hp == 4:
    h.shape("hp4.gif")
  elif hp == 3:
    h.shape("hp3.gif")
  elif hp == 2:
    h.shape("hp2.gif")
  elif hp == 1:
    h.shape("hp1.gif")
  elif hp <= 0:
    running = False
  
  #Positions
  """a.goto(xpos,ypos)"""

  #Player A Keyboard Events
  S.onclick(a.goto)
  """turtle.onkey(a_up, "w")
  turtle.onkey(a_left, "a")
  turtle.onkey(a_down, "s")
  turtle.onkey(a_right, "d")"""

  #Enemy AI
  if rp > 140:
    rp = randint(-180,180)
    enemy.seth(rp)
    enemy.forward(20)

  #Boundaries
  if rp > 140:
    enemy.shape("wolfoxopen.gif")
    enemy.left(50)
    enemy.shape("wolfoxbite.gif")
    enemy.left(randint(1,1000))
    enemy.shape("wolfoxopen.gif")
    enemy.left(50)
    enemy.shape("wolfox.gif")
    if enemy.pos() == a.pos():
      hp -= 1
  if randint(1,100) == 1:
    enemy.goto(a.pos())

  #Random Percentage
  rp = randint(-180,180)