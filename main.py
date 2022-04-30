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
e_hp = 2

def rs(input):
  turtle.register_shape(input)
def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
def attack(__innit__,__call__):
  global e_hp
  e_hp -= 1
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
enemy.penup()
enemy.goto(185,-170)
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
  clearconsole()
  print("ENEMY:")
  print(enemy.pos())
  print("hp:")
  print(e_hp)
  print("")
  print("PLAYER:")
  print(a.pos())
  print("hp:")
  print(hp)
  print("-----------------")
  h.shape("hp{0}.gif".format(hp))
  if hp == 0:
    print("hp == 0")
    time.sleep(0.75)
    running = False
  
  #Attack
  if enemy.pos() == a.pos():
    enemy.onclick(attack)

  #Player A Keyboard Events
  S.onclick(a.goto)
  """turtle.onkey(a_up, "w")
  turtle.onkey(a_left, "a")
  turtle.onkey(a_down, "s")
  turtle.onkey(a_right, "d")"""

  #Damage
  if rp > 140:
    enemy.shape("wolfoxopen.gif")
    enemy.left(50)
    enemy.shape("wolfoxbite.gif")
    enemy.left(randint(1,500))
    if enemy.pos() == a.pos():
      hp -= 1
    enemy.left(randint(1,500))
    enemy.shape("wolfoxopen.gif")
    enemy.left(50)
    enemy.shape("wolfox.gif")
    time.sleep(0.5)
  if randint(1,100) <= 20:
    enemy.goto(a.pos())

  #Random Percentage
  rp = randint(-180,180)