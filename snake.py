import turtle
import time
import random

delay=0.07
score=0
highscore=0

#set up the screen

wn = turtle.Screen()
wn.title("snake game by shah")
wn.bgcolor("crimson")
wn.setup(width=600, height=600)
wn.tracer(0)


#snake head

head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("lime")
head.penup()
head.goto(0,0)
head.direction="stop"


#snakefood
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)
food.direction="stop"


segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0  highscore: 0", align="center", font=("Courier",24,"normal"))

#function
def goup():
 if head.direction != "down":
  head.direction="up"


def godown():
 if head.direction != "up":
  head.direction="down"


def goleft():
 if head.direction != "right":
  head.direction="left"
 
 
def goright():
 if head.direction != "left":
   head.direction="right"
 
 
def move():
 if head.direction=="up":
  y=head.ycor()
  head.sety(y + 20)
 
 
 if head.direction=="down":
  y=head.ycor()
  head.sety(y - 20)
 
 
 if head.direction=="left":
  x=head.xcor()
  head.setx(x - 20)
 
 
 if head.direction=="right":
  x=head.xcor()
  head.setx(x + 20)

#keyboard bindings

wn.listen()
wn.onkeypress(goup,"w")
wn.onkeypress(godown,"s")
wn.onkeypress(goleft,"a")
wn.onkeypress(goright,"d")



#main game loop

while True:
 wn.update()
 
 #check for head collision with the body segments
 for segment in segments:
  if segment.distance(head)<20:
   time.sleep(1)
   head.direction= "stop"
   head.goto(0,0)
   #hide the segments
   for segment in segments:
    segment.goto(10000,10000)
  
   #clear the segments
   segments.clear()
 
 #check for collision with the borders
 if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
  time.sleep(1)
  head.goto(0,0)
  head.direction= "stop"
  
  #hide the segments
  for segment in segments:
   segment.goto(10000,10000)
  
  #clear the segments
  segments.clear()
  
  #reset score
  score=0
  pen.clear()
  pen.write("score: {}  highscore: {}".format(score,highscore), align="center", font= ("Courier",24,"normal"))
    
  
 #check for collision with the food
 if head.distance(food)<20:
  #move food to the random spot
  x=random.randint(-290,290)
  y=random.randint(-290,290)
  food.goto(x,y)
 
  #add a new segments
  newsegment=turtle.Turtle()
  newsegment.speed(0)
  newsegment.shape("circle")
  newsegment.color("lime")
  newsegment.penup()
  segments.append(newsegment)
  
  #increase in score
  score+= 10
  pen.clear()
  pen.write("score: {}  highscore: {}".format(score,highscore), align="center", font= ("Courier",24,"normal"))
 
  if score > highscore:
   highscore=score
   pen.clear()
   pen.write("score: {}  highscore: {}".format(score,highscore), align="center", font= ("Courier",24,"normal"))
  
  
 #move the end segments in reverse order
 for index in range(len(segments)-1 ,0 ,-1):
   x= segments[index-1].xcor()
   y= segments[index-1].ycor()
   segments[index].goto(x,y)
   
  #move segment 0 to where the head is
 if len(segments) > 0:
    x= head.xcor()
    y= head.ycor()
    segments[0].goto(x,y)
 

  
 move()
 
 time.sleep(delay)



wn.mainloop()