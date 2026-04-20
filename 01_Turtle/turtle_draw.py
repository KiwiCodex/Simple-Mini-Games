import turtle

screen = turtle.Screen()
tortuga = turtle.Turtle()

tortuga.shapesize(2, 2, 2) #tamaño de la tortuga
tortuga.fillcolor("green") #color de la tortuga
tortuga.pensize(2)
tortuga.shape("turtle")

tortuga.begin_fill()
tortuga.goto(100, 100)
tortuga.goto(-100, 100)
tortuga.home()
tortuga.color("red")
tortuga.end_fill()

tortuga.begin_fill()
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.color("green")
tortuga.end_fill()


tortuga.circle(25)
tortuga.circle(50)
tortuga.pencolor("blue")
tortuga.dot(25)

tortuga.setx(100)
tortuga.sety(50)

tortuga.begin_fill()
tortuga.circle(60)
tortuga.color("black")
tortuga.end_fill()

tortuga.begin_fill()
tortuga.circle(30)
tortuga.color("white")
tortuga.end_fill()

tortuga.pencolor("blue")
tortuga.dot(25)

tortuga.setx(-200)

for i in range(4):
    tortuga.forward(100)
    tortuga.right(90)

while i <= 100:
    tortuga.circle(i)
    i+=10

turtle.done()