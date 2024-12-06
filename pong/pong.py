import turtle
import random
import math

turtle.shape("turtle")

def drawRectangle(ul, w, h):
    # move to ul
    turtle.up()
    turtle.goto(ul[0], ul[1])
    turtle.down()
    # face right
    turtle.setheading(0)
    # go forward by width
    turtle.forward(w)
    # turn right 90
    turtle.right(90)
    # go forward by height
    turtle.forward(h)
    # ...
    turtle.right(90)
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(h)
    
# draw the bounding square (i.e., the walls)
drawRectangle((-200, 200), 400, 400)
turtle.hideturtle()

### PADDLE STUFF ###

# make the turtle the paddle!
paddle = turtle.Turtle()
paddle.shape('square')
paddle.fillcolor('red')
paddle.left(90)
paddle.turtlesize(1.5, 6)

paddle_x = -170
paddle_y = 0

# put the turtle in the correct starting location
paddle.up()
paddle.goto(paddle_x, paddle_y)

def go_up():
    global paddle_y
    paddle_y = paddle_y + 10
    # make sure we don't go past the top
    if paddle_y > 140:
        paddle_y = 140
    paddle.goto(paddle_x, paddle_y)

def go_down():
    global paddle_y
    paddle_y = paddle_y - 10
    # make sure we don't go past the bottom
    if paddle_y < -140:
        paddle_y = -140
    paddle.goto(paddle_x, paddle_y)

# set up functions to run every time the up/down keys are pressed
turtle.onkeypress(go_up, "k")
turtle.onkeypress(go_down, "j")
turtle.listen()

### BALL STUFF ###

# make the turtle the square!
ball = turtle.Turtle()
ball.shape('square')
ball.fillcolor('green')
ball.turtlesize(2, 2)
turtle_width = 40

# we'll use these variables to keep track of
# where the square should be/where it should move
turtle_x = random.randint(0, 150)
turtle_y = random.randint(-150, 150)
# these two variables together will form our direction
turtle_xoffset = random.uniform(-1.0, 1.0)
turtle_yoffset = random.uniform(-1.0, 1.0)
#print(turtle_xoffset, turtle_yoffset)
# let's *normalize* our direction so that
# it has a length 1 hypotenuse
direction_hyp_length = math.sqrt(turtle_xoffset**2 + turtle_yoffset**2)
turtle_xoffset = turtle_xoffset / direction_hyp_length * 2
turtle_yoffset = turtle_yoffset / direction_hyp_length * 2
# now the length of the hypotenuse is 2

is_game_over = False

# put the turtle in the correct starting location
ball.up()
ball.goto(turtle_x, turtle_y)

def bounce_if_hit_paddle():
    global turtle_x
    global turtle_xoffset

    A = turtle_x <= paddle_x + 15 + 20
    B = turtle_y <= paddle_y + 60 + 20
    C = turtle_y >= paddle_y - 60 - 20
    
    if A and B and C:
        turtle_x = paddle_x + 15 + 20


        turtle_xoffset = turtle_xoffset * -1

def bounce_if_hit_wall():
    global turtle_x
    global turtle_y
    global turtle_xoffset
    global turtle_yoffset
    global is_game_over
    
    if turtle_y <= -200 + turtle_width/2:
        # we either hit the bottom wall, or we're trying to go below it
        # move the turtle back inside
        turtle_y = -200 + turtle_width/2
        # change the turtle_yoffset so we move upwards now
        turtle_yoffset = turtle_yoffset * -1

    if turtle_y >= 200 - turtle_width/2:
        # we either hit the top wall, or we're trying to go above it
        # move the turtle back inside
        turtle_y = 200 - turtle_width/2
        # change the turtle_yoffset so we move upwards now
        turtle_yoffset = turtle_yoffset * -1

    if turtle_x <= -200 + turtle_width/2:
        # we either hit the left wall, or we're trying to go past it
        # move the turtle back inside
        turtle_x = -200 + turtle_width/2
        # change the turtle_xoffset so we move to the right now
        turtle_xoffset = turtle_xoffset * -1
        # Game over!
        is_game_over = True

    if turtle_x >= 200 - turtle_width/2:
        # we either hit the right wall, or we're trying to go past it
        # move the turtle back inside
        turtle_x = 200 - turtle_width/2
        # change the turtle_xoffset so we move to the left now
        turtle_xoffset = turtle_xoffset * -1

def drawFrame():
    global turtle_x
    global turtle_y
    global turtle_xoffset
    global turtle_yoffset

    # change the turtle's x coordinate by the x offset
    turtle_x = turtle_x + turtle_xoffset
    # change the turtle's y coordinate by the y offset
    turtle_y = turtle_y + turtle_yoffset

    # if we hit a wall, bounce off
    bounce_if_hit_wall()

    # if we hit the paddle, bounce off
    bounce_if_hit_paddle()

    # redraw the turtle
    ball.goto(turtle_x, turtle_y)

while not is_game_over:
    # repeatedly, draw a new frame
    drawFrame()
