import turtle

'''
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


rec_square(100)
turtle.done()


def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)


def main():
    tracer(0)
    up()
    goto(-300, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(n, a)
    update()
    done()

main()


def squares(k, size):
    if k == 0:
        for i in range(4):
            turtle.forward(size)
            turtle.rt(90)

    else:
        turtle.pu()
        turtle.forward(0.05*size)
        turtle.rt(10)
        turtle.pd()
        return squares(k-1, size*0.9)


squares(3, 200)
'''

turtle.speed(-1)


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


dragon(10, 100, 1)





turtle.done()
