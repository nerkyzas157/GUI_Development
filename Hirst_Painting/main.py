import turtle
import random
import colorgram

# Define objects and setup the Turtle
hirst_turtle = turtle.Turtle()
turtle.colormode(255)
turtle.speed = 0
hirst_turtle.pensize(20)
hirst_turtle.hideturtle()

# Set a temporary position of the image and extracted the colours
colors = colorgram.extract("image.jpg", 100)


def color(colors):
    """Function that chooses random color from the extracted colors list."""
    num = random.randint(0, len(colors) - 1)
    f_color = colors[num]
    rgb = f_color.rgb
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    return (r, g, b)


def back():
    """Moves Turtle to it's initial pozition and goes up by a row."""
    hirst_turtle.penup()
    hirst_turtle.backward(310)
    hirst_turtle.left(90)
    hirst_turtle.forward(30)
    hirst_turtle.pendown()
    hirst_turtle.right(90)


def get_position():
    """Adjusts the starting coordinates so painting could be centered."""
    hirst_turtle.penup()
    hirst_turtle.setheading(225)
    hirst_turtle.forward(200)
    hirst_turtle.setheading(0)
    hirst_turtle.pendown()


# Drawing the Hirst Painting
get_position()
for xy in range(10):
    for x in range(10):
        hirst_turtle.pencolor(color(colors))
        hirst_turtle.forward(1)
        hirst_turtle.penup()
        hirst_turtle.forward(30)
        hirst_turtle.pendown()
    back()

# Created an object and used it's function, to hold the painting in place
screen = turtle.Screen()
screen.exitonclick()
