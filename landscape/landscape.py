import turtle

turtle.shape("turtle")

hank = turtle.Turtle()
scn = turtle.Screen()
bill = turtle.Turtle()
dale = turtle.Turtle()
boomhauer = turtle.Turtle()

hank.shape("turtle")
bill.shape("square")
dale.shape("circle")

hank.pencolor("black")
hank.pensize(3)
hank.fillcolor("lime green")
hank.begin_fill()
hank.forward(600)
hank.backward(1200)
hank.right(90)
hank.forward(400)
hank.left(90)
hank.forward(1200)
hank.left(90)
hank.forward(400)
hank.end_fill()

bill.penup()
bill.forward(600)
bill.pendown()
bill.fillcolor("dodger blue")
bill.begin_fill()
bill.left(90)
bill.forward(400)
bill.left(90)
bill.forward(1200)
bill.left(90)
bill.forward(400)
bill.left(90)
bill.forward(1200)
bill.end_fill()

dale.penup()
dale.goto(-200, 0)



turtle.exitonclick()
