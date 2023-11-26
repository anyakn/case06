import turtle


turtle.speed(-1)


def square(n):
    for i in range(4):
        turtle.fd(n)
        turtle.rt(90)

    turtle.fd(0.1*n)
    turtle.rt(10)


def rec_square(n):
    if n <= 0:
        return None
    square(n)
    turtle.rt(5)
    return rec_square(0.9 * n)


def levy(n_l, size_l):
    if n_l == 0:
        turtle.fd(size_l)
    else:
        turtle.lt(45)
        levy(n_l - 1, size_l)
        turtle.rt(90)
        levy(n_l - 1, size_l)
        turtle.lt(45)


def dragon(n_d, size_d, sign):
    if n_d == 0:
        turtle.fd(size_d)
    else:
        turtle.lt(45*sign)
        dragon(n_d - 1, size_d / (2**0.5), 1)
        turtle.rt(90*sign)
        dragon(n_d - 1, size_d / (2 ** 0.5), -1)
        turtle.lt(45*sign)


def rhombus(x, y, r, n_r):
    if n_r == 0:
        turtle.pu()
        turtle.goto(x, y)
        turtle.fd(-r)
        turtle.lt(45)
        turtle.pd()
        for i in range(4):
            turtle.fd(r * 2**0.5)
            turtle.rt(90)
        turtle.rt(45)
    else:
        rhombus(x, y, r, 0)
        rhombus(x-r, y, r/2, n_r - 1)
        rhombus(x+r, y, r/2, n_r - 1)
        rhombus(x, y-r, r/2, n_r - 1)
        rhombus(x, y+r, r/2, n_r - 1)


turtle.done()
