import turtle
### Functions to draw letters ###

# A
def draw_a(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward(size)
    # right vertical line
    turtle.right(90)
    turtle.forward(size)
    # middle horizontal line
    turtle.backward((size/5) * 3)
    turtle.right(90)
    turtle.forward(size)

# B
def draw_b(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward((size/5) * 4)
    # top right vertical line
    turtle.right(90)
    turtle.forward((size/5) * 2)
    # middle horizontal line
    turtle.right(90)
    turtle.forward((size/5) * 2)
    turtle.right(180)
    turtle.forward((size/5) * 3)
    # bottom right vertical line
    turtle.right(90)
    turtle.forward((size/5) * 3)
    # bottom horizontal line
    turtle.right(90)
    turtle.forward(size)

# C
def draw_c(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward(size)
    turtle.right(180)
    turtle.forward(size)
    # get to bottom horizontal line
    turtle.left(90)
    turtle.forward(size)
    # bottom horizontal line
    turtle.left(90)
    turtle.forward(size)

# D
def draw_d(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward((size/5) * 3)
    # right vertical line
    turtle.right(90)
    turtle.forward(size)
    # bottom horizontal line
    turtle.right(90)
    turtle.forward((size/5) * 3)

# E
def draw_e(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward(size)
    turtle.right(180)
    turtle.forward(size)
    # get to middle horizontal line
    turtle.left(90)
    turtle.forward((size/2) * 1)
    # middle horizontal line
    turtle.left(90)
    turtle.forward((size/5) * 3)
    # get to bottom horizontal line
    turtle.left(180)
    turtle.forward((size/5) * 3)
    turtle.left(90)
    turtle.forward((size/2) * 1)
    # bottom horizontal line
    turtle.left(90)
    turtle.forward(size)

# F
def draw_f(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward(size)
    turtle.right(180)
    turtle.forward(size)
    # get to middle horizontal line
    turtle.left(90)
    turtle.forward((size/2) * 1)
    # middle horizontal line
    turtle.left(90)
    turtle.forward((size/5) * 3)

# G
def draw_g(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward(size)
    turtle.right(180)
    turtle.forward(size)
    # get to bottom horizontal line
    turtle.left(90)
    turtle.forward(size)
    # bottom horizontal line
    turtle.left(90)
    turtle.forward(size)
    # get to middle horizontal line
    turtle.left(90)
    turtle.forward((size/5) * 3)
    # middle horizontal line
    turtle.left(90)
    turtle.forward((size/5) * 3)

# H
def draw_h(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # get to middle horizontal line
    turtle.right(180)
    turtle.forward((size/5) * 2)
    # middle horizontal line
    turtle.left(90)
    turtle.forward(size)
    # right vertical line
    turtle.left(90)
    turtle.forward((size/5) * 2)
    turtle.right(180)
    turtle.forward(size)

# I
def draw_i(size):
    # bottom horizontal line
    turtle.forward(size)
    # get to middle vertical line
    turtle.left(180)
    turtle.forward((size/2) * 1)
    # middle vertical line
    turtle.right(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward((size/2) * 1)
    turtle.left(180)
    turtle.forward(size)

# J
def draw_j(size):
    # left vertical line
    turtle.left(90)
    turtle.forward((size/5) * 1)
    # get to bottom horizontal line
    turtle.right(180)
    turtle.forward((size/5) * 1)
    # bottom horizontal line
    turtle.left(90)
    turtle.forward(size / 2)
    # middle vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward((size/2) * 1)
    turtle.left(180)
    turtle.forward(size)

# K
def draw_k(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # get to middle diag
    turtle.right(180)
    turtle.forward((size/5) * 2)
    # middle diag
    turtle.left(130)
    turtle.forward((size/5) * 3)
    # get to lower diag
    turtle.right(180)
    turtle.forward((size/5) * 3)
    # lower diag
    turtle.left(50 + 45)
    turtle.forward((size/5) * 4)

# L
def draw_l(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # get to bottom horizontal line
    turtle.right(180)
    turtle.forward(size)
    # bottom horizontal line
    turtle.left(90)
    turtle.forward(size)

# M
def draw_m(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # get to middle vertical
    turtle.right(90)
    turtle.forward((size/2) * 1)
    # middle vertical
    turtle.right(90)
    turtle.forward(size)
    # get to right vertical
    turtle.left(180)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward((size/2) * 1)
    # right vertical line
    turtle.right(90)
    turtle.forward(size)

# N
def draw_n(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # get to middle vertical
    turtle.right(90)
    turtle.forward(size)
    # right vertical line
    turtle.right(90)
    turtle.forward(size)

# O
def draw_o(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward(size)
    # right vertical line
    turtle.right(90)
    turtle.forward(size)
    # bottom horizontal line
    turtle.right(90)
    turtle.forward(size)

# P
def draw_p(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward(size)
    # right vertical line
    turtle.right(90)
    turtle.forward((size/5) * 2)
    # bottom horizontal line
    turtle.right(90)
    turtle.forward(size)

# Q
def draw_q(size):
    # get to right vertical line
    turtle.penup()
    turtle.forward(size)
    turtle.pendown()
    # right vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.left(90)
    turtle.forward(size)
    # left vertical line
    turtle.left(90)
    turtle.forward((size/5) * 2)
    # bottom horizontal line
    turtle.left(90)
    turtle.forward(size)

# R
def draw_r(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward(size)
    # right vertical line
    turtle.right(90)
    turtle.forward((size/5) * 2)
    # bottom horizontal line
    turtle.right(90)
    turtle.forward(size)
    # lower diag
    turtle.right(180 + 45)
    turtle.forward((size/5) * 4)

# S
def draw_s(size):
    # bottom horizontal line
    turtle.forward(size)
    # right vertical line
    turtle.left(90)
    turtle.forward((size/2) * 1)
    # middle horizontal line
    turtle.left(90)
    turtle.forward(size)
    # left vertical line
    turtle.right(90)
    turtle.forward((size/2) * 1)
    # top horizontal line
    turtle.right(90)
    turtle.forward(size)

# T
def draw_t(size):
    # get to middle vertical line
    turtle.penup()
    turtle.forward(size / 2)
    turtle.pendown()
    # middle vertical line
    turtle.left(90)
    turtle.forward(size)
    # top horizontal line
    turtle.right(90)
    turtle.forward((size/2) * 1)
    turtle.left(180)
    turtle.forward(size)

# U
def draw_u(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    # get to bottom horizontal line
    turtle.right(180)
    turtle.forward(size)
    # bottom horizontal line
    turtle.left(90)
    turtle.forward(size)
    # right vertical line
    turtle.left(90)
    turtle.forward(size)

# V
def draw_v(size):
    # get to left diag line
    turtle.penup()
    turtle.forward(size/2)
    turtle.pendown()
    # left diag
    turtle.left(120)
    turtle.forward((size/5) * 4)
    # get back for right diag
    turtle.left(180)
    turtle.forward((size/5) * 4)
    # right diag
    turtle.left(120)
    turtle.forward((size/5) * 4)

# W
def draw_w(size):
    # left vertical line
    turtle.left(90)
    turtle.forward(size)
    turtle.right(180)
    turtle.forward(size)
    # 1/2 bottom horizontal line
    turtle.left(90)
    turtle.forward(size/2)
    # middle vertical line
    turtle.left(90)
    turtle.forward((size/5) * 4)
    turtle.right(180)
    turtle.forward((size/5) * 4)
    # 1/2 bottom horizontal line
    turtle.left(90)
    turtle.forward(size/2)
    # right vertical line
    turtle.left(90)
    turtle.forward(size)

# X
def draw_x(size):
    # left diag
    turtle.left(45)
    turtle.forward((size/5) * 4)
    for j in range(2):
        for i in range(2):
            turtle.left(180)
            turtle.forward((size/5) * 4)
            turtle.backward((size/5) * 4)
        turtle.left(90)

# Y
def draw_y(size):
    # get to middle vertical line
    turtle.penup()
    turtle.forward(size / 2)
    turtle.pendown()
    # middle vertical line
    turtle.left(90)
    turtle.forward((size/5) * 2)
    # left diag
    turtle.left(45)
    turtle.forward((size/5) * 2)
    turtle.backward((size/5) * 2)
    # right diag
    turtle.right(90)
    turtle.forward((size/5) * 2)

# Z
def draw_z(size):
    # bottom horizontal line
    turtle.forward(size)
    turtle.backward(size)
    # right vertical line
    turtle.left(90)
    turtle.forward((size/2) * 1)
    # middle horizontal line
    turtle.right(90)
    turtle.forward(size)
    # left vertical line
    turtle.left(90)
    turtle.forward((size/2) * 1)
    # top horizontal line
    turtle.left(90)
    turtle.forward(size)
