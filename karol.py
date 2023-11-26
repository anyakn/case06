import turtle

turtle.speed(100)

def dandelion(size, depth):
    if depth == 0:
        turtle.forward(size)
    else:
        turtle.forward(size)
        for i in range(6):
            dandelion(size/3, depth-1)
            turtle.right(60)
        turtle.backward(size)


def dandelion_snowflake(size, depth):
    for i in range(6):
        dandelion(size, depth - 1)
        turtle.right(60)

depth = int(input('Глубина рекурсии:'))
size = int(input('Длина стороны:'))

dandelion_snowflake(size, depth)
turtle.done()


import turtle
turtle.speed(1)

def koch(size, depth):
    if depth == 0:
        turtle.forward(size)
    else:
        koch(size/3, depth-1)
        turtle.left(60)
        koch(size/3, depth-1)
        turtle.right(120)
        koch(size/3, depth-1)
        turtle.left(60)
        koch(size/3, depth-1)


def koch_snowflake(size, depth):
    for i in range(3):
        koch(size, depth)
        turtle.right(120)


def ice_1(size, depth):
    if depth == 0:
        turtle.forward(size)
    else:
        ice_1(size, depth-1)
        turtle.left(90)
        ice_1(size / 2, depth - 1)
        turtle.right(180)
        ice_1(size / 2, depth - 1)
        turtle.left(90)
        ice_1(size, depth-1)


depth = int(input('Глубина рекурсии:'))
size = int(input('Длина стороны:'))
ice_1(size, depth)


depth = int(input('Глубина рекурсии:'))
size = int(input('Длина стороны:'))
koch_snowflake(size, depth)
