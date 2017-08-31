import turtle
import random

annalisa = turtle.Turtle()
annalisa.hideturtle()
annalisa.speed(0)
turtle.screensize(2000, 2000, 'black')
turtle.colormode(255)


def draw_poly(sides, angle, length):
    for i in range(sides):
        annalisa.forward(length)
        annalisa.right(angle)


def poly_loop(layers, sides, steps):
    angle = 360 // sides
    length = 2000 // sides
    for i in range(layers):
        if length < 0:
            break
        else:
            annalisa.pendown()
            annalisa.fillcolor(random.randrange(0, 255),
                               random.randrange(0, 255),
                               random.randrange(0, 255))
            annalisa.begin_fill()
            draw_poly(sides, angle, length)
            annalisa.end_fill()
            annalisa.penup()
            annalisa.right(90)
            annalisa.forward(steps)
            annalisa.left(90)
            annalisa.forward(steps)
            length = length - steps


def main():
    annalisa.up()
    poly_loop(500, 16, 1)
    """ Use a higher number for layers and a lower number for steps.
    Higher number for side will make it more circular"""


if __name__ == '__main__':
    main()

turtle.exitonclick()
