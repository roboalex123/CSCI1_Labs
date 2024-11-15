import turtle
from time import sleep
import math
import random

# Constants
WORLD_SIZE = 4000

class ShapeDrawer:
    SHAPE_SIZE_RANGE = (40, 400)
    NUM_SHAPES_RANGE = (5, 20)
    SHAPE_ORIENTATION_RANGE = (0, 360)

    def draw_circle(self, radius):
        self.turtle.circle(radius)

    def draw_square(self, size):
        for _ in range(4):
            self.turtle.forward(size)
            self.turtle.left(90)

    def draw_triangle(self, size):
        for _ in range(3):
            self.turtle.forward(size)
            self.turtle.left(120)

    def draw_star(self, size):
        for _ in range(5):
            self.turtle.forward(size)
            self.turtle.left(144)

    def draw_pentagon(self, size):
        for _ in range(5):
            self.turtle.forward(size)
            self.turtle.left(72)

    def draw_hexagon(self, size):
        for _ in range(6):
            self.turtle.forward(size)
            self.turtle.left(60)


    COLORS = [
        "red",
        "blue",
        "green",
        "purple",
        "orange",
        "yellow",
        "black",
        "brown",
        "cyan",
        "magenta",
    ]

    def __init__(self):
        self.num_shapes = random.randint(*self.NUM_SHAPES_RANGE)
        self.turtle = turtle.Turtle()
        self.turtle.getscreen().setworldcoordinates(
            -WORLD_SIZE, -WORLD_SIZE,
            WORLD_SIZE, WORLD_SIZE
        )
        self.turtle.speed('fast')
        self.COLOR = random.choice(self.COLORS)
        self.turtle.color(self.COLOR)
        self.turtle.fillcolor(self.COLOR)
        self.SHAPE_FUNCS = [
            self.draw_circle,
            self.draw_square,
            self.draw_triangle,
            self.draw_star,
            self.draw_pentagon,
            self.draw_hexagon,
        ]

    def draw(self):
        for _ in range(self.num_shapes):
            shape_func = random.choice(self.SHAPE_FUNCS)
            self.draw_shape(shape_func)

    def draw_shape(self, shape_name):
        SIZE = random.randint(*self.SHAPE_SIZE_RANGE)
        SHAPE_LOCATION = (
                random.randint(-WORLD_SIZE + SIZE, WORLD_SIZE - SIZE),
                random.randint(-WORLD_SIZE + SIZE, WORLD_SIZE - SIZE)
                )

        self.turtle.penup()
        self.turtle.goto(SHAPE_LOCATION)
        self.turtle.setheading(random.randint(*self.SHAPE_ORIENTATION_RANGE))
        self.turtle.pendown()

        self.turtle.begin_fill()
        shape_name(SIZE)
        self.turtle.end_fill()

    def clear(self):
        self.turtle.clear()

def main():
    NUMBER_OF_TURTLES = input("How many turtles? ")
    try:
        NUMBER_OF_TURTLES = int(NUMBER_OF_TURTLES)
    except ValueError:
        NUMBER_OF_TURTLES = 1

    turtles = []
    for _ in range(NUMBER_OF_TURTLES):
        turtles.append(ShapeDrawer())

    while True:
        for t in turtles:
            t.draw()
        sleep(10)

        for t in turtles:
            t.clear()

if __name__ == "__main__":
    main()
