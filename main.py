import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("deepskyblue")

t = turtle.Turtle()

t.speed(0.5)


# GRASS

t.penup()
t.goto(-5000,-50)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.goto(5000,0)
t.goto(5000,-50)
t.goto(-5000,-1000)
t.goto(-5000,0)
t.end_fill()

# CLOUD
t.penup()
t.goto(50,150)
t.pencolor("white")

t.pendown()
t.pensize(10)
t.goto(50,150)

t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()

t.goto(95,150)

t.pendown()

t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()

t.goto(5,150)

t.pendown()

t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.circle(20)
t.end_fill()

# SUN
t.penup()
t.goto(275,250)
t.pencolor("yellow")

t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# FLOWER
t.goto(50,-250)

t.pencolor("blue")
t.fillcolor("blue")
t.begin_fill()
t.circle(10)
t.end_fill()

t.goto(40,-260)

t.pencolor("blue")
t.fillcolor("blue")
t.begin_fill()
t.circle(10)
t.end_fill()

t.goto(30,-250)

t.pencolor("blue")
t.fillcolor("blue")
t.begin_fill()
t.circle(10)
t.end_fill()

t.goto(40,-240)

t.pencolor("blue")
t.fillcolor("blue")
t.begin_fill()
t.circle(10)
t.end_fill()

t.goto(40,-250)

t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
t.circle(7)
t.end_fill()

# TREE
t.penup()
t.goto(200,-150)
t.pencolor("brown")

t.pendown()
t.pensize(20)
t.goto(200,-50)

t.pencolor("darkgreen")
t.fillcolor("darkgreen")
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()

# FENCE
t.goto(-50,-170)
t.pencolor("brown")

t.pendown()
t.pensize(10)
t.forward(100)
t.penup()

t.goto(-50,-155)
t.pencolor("brown")
t.pendown()
t.pensize(10)
t.forward(100)
t.penup()

t.goto(-50,-140)
t.pencolor("brown")
t.pendown()
t.pensize(10)
t.forward(100)
t.penup()

t.goto(-35,-130)
t.pencolor("brown")
t.pendown()
t.pensize(10)
t.right(90)
t.forward(55)
t.penup()

t.goto(35,-130)
t.pencolor("brown")
t.pendown()
t.pensize(10)
t.forward(55)
t.penup()

# POND

t.goto(-370,-260)

t.pencolor("deepskyblue")
t.fillcolor("deepskyblue")
t.begin_fill()
t.circle(150)
t.end_fill()

# TEXT
t.color("black")

t.goto(-175,250)

t.write("spring", font=("Arial", 24, "bold"))

#BIRDS

t.penup()

t.goto(-175,150)
t.pendown()

t.pensize(4)
t.left(25)
t.forward(20)

t.left(125)
t.forward(20)

t.penup()

t.goto(-155,130)
t.pendown()

t.right(150)

t.pensize(4)
t.left(25)
t.forward(10)

t.left(125)
t.forward(10)

t.penup()

t.goto(-185,120)
t.pendown()

t.right(150)

t.pensize(4)
t.left(25)
t.forward(10)

t.left(125)
t.forward(10)

# BUSH

t.penup()
t.goto(50,150)
t.pencolor("darkgreen")

t.pensize(10)
t.goto(220,-250)

t.pendown()
t.pencolor("darkgreen")
t.fillcolor("darkgreen")
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()

t.goto(165,-260)

t.pendown()
t.pencolor("darkgreen")
t.fillcolor("darkgreen")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()

t.goto(250,-260)

t.pendown()
t.pencolor("darkgreen")
t.fillcolor("darkgreen")
t.begin_fill()
t.circle(20)
t.end_fill()

#LAST LINE OF CODE
turtle.done()