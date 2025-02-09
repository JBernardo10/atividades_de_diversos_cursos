import turtle

#turtle.speed(1)
turtle.color("red")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.width(4)
turtle.left(130)
turtle.forward(155)
for i in range(200):
    turtle.right(1)
    turtle.forward(1)
turtle.left(140)
for i in range(200):
    turtle.right(1)
    turtle.forward(1)
turtle.home()
turtle.end_fill()
turtle.done()
