import turtle

turtle.speed(1)
turtle.left(90)
turtle.bgcolor("black")

def draw_tree(branch_len, pen_size):
    if branch_len < 3:
        turtle.color("green")
    else:
        turtle.color("brown")
    if branch_len < 10:
            turtle.pensize(1)
    else:
        turtle.pensize(pen_size)

        
    if branch_len > 5:
        turtle.forward(branch_len)
        turtle.left(38)
        draw_tree(branch_len - 15, pen_size - 1)
        turtle.right(60)
        draw_tree(branch_len - 15, pen_size - 1)
        turtle.left(30)
        turtle.backward(branch_len)

draw_tree(100,7)
turtle.done()