import turtle
from time import sleep
import math
from letterFuncs import *

# Constants
WORLD_SIZE = 1000
LETTER_SIZE = 200
SPACE_BETWEEN_LETTERS = 30
SPACE_BETWEEN_WORDS = 100
SPACE_BETWEEN_LINES = 100

# Letter class
class Letter:
    # default size
    SIZE = LETTER_SIZE

    # constructor
    def __init__(self, starting_x, starting_y, letter, function_to_draw):
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.letter = letter
        self.size = self.SIZE
        self.function_to_draw = function_to_draw

    # draw the letter
    def draw(self):
        # get set up to draw the letter
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(self.starting_x, self.starting_y)
        turtle.pendown()
        self.function_to_draw(self.size)
        turtle.setheading(0)
        turtle.penup()

    # set starting position
    def set_starting_position(self, x, y):
        self.starting_x = x
        self.starting_y = y

    # set size
    def set_size(self, size):
        self.size = size

# Dictionary of Letters
letters = {
        "A": Letter(0, 0, "A", draw_a),
        "B": Letter(0, 0, "B", draw_b),
        "C": Letter(0, 0, "C", draw_c),
        "D": Letter(0, 0, "D", draw_d),
        "E": Letter(0, 0, "E", draw_e),
        "F": Letter(0, 0, "F", draw_f),
        "G": Letter(0, 0, "G", draw_g),
        "H": Letter(0, 0, "H", draw_h),
        "I": Letter(0, 0, "I", draw_i),
        "J": Letter(0, 0, "J", draw_j),
        "K": Letter(0, 0, "K", draw_k),
        "L": Letter(0, 0, "L", draw_l),
        "M": Letter(0, 0, "M", draw_m),
        "N": Letter(0, 0, "N", draw_n),
        "O": Letter(0, 0, "O", draw_o),
        "P": Letter(0, 0, "P", draw_p),
        "Q": Letter(0, 0, "Q", draw_q),
        "R": Letter(0, 0, "R", draw_r),
        "S": Letter(0, 0, "S", draw_s),
        "T": Letter(0, 0, "T", draw_t),
        "U": Letter(0, 0, "U", draw_u),
        "V": Letter(0, 0, "V", draw_v),
        "W": Letter(0, 0, "W", draw_w),
        "X": Letter(0, 0, "X", draw_x),
        "Y": Letter(0, 0, "Y", draw_y),
        "Z": Letter(0, 0, "Z", draw_z)
}


# Functions
def turtle_reset(): # resets turtle to default position
    turtle.clear()
    turtle.penup()
    turtle.setposition(-WORLD_SIZE, WORLD_SIZE - LETTER_SIZE)
    turtle.setheading(0)

def carriage_return(current_position): # moves turtle to next line
    turtle.penup()
    turtle.setposition(-WORLD_SIZE, current_position[1] - SPACE_BETWEEN_LINES - LETTER_SIZE)
    current_position = turtle.position()

    return current_position

# main function that gets input line from user
def main():
    turtle.getscreen().setworldcoordinates(-WORLD_SIZE, -WORLD_SIZE, WORLD_SIZE, WORLD_SIZE)
    turtle.speed('fast')

    line = input("Enter the line (or QUIT to quit): ").upper()
    while line != "QUIT":
        turtle_reset()
        # get starting position and save it in a variable to be used later
        current_position = turtle.position()

        for letter in line:
            if current_position[0] > WORLD_SIZE - LETTER_SIZE:
                current_position = carriage_return(current_position)


            if letter == " ": # skip spaces and look appropriately
                turtle.penup()
                turtle.forward(SPACE_BETWEEN_WORDS)
                current_position = turtle.position()

            elif letter == "\n": # move to next line (carriage return)
                current_position = carriage_return(current_position)

            elif letter not in letters: # check if letter is valid
                print("Letter not found: " + letter)

            else:
                letters[letter].set_starting_position(current_position[0], current_position[1])
                letters[letter].draw()
                current_position = turtle.position()
                turtle.setposition(letters[letter].starting_x + LETTER_SIZE + SPACE_BETWEEN_LETTERS, letters[letter].starting_y)
                current_position = turtle.position()

        garbage = input("Press Enter to continue...") # wait for user
        # get input from user
        line = input("Enter the line (or QUIT to quit): ").upper()

if __name__ == "__main__":
    main()
