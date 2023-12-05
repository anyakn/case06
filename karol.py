import turtle

turtle.speed(100)
depth = int(input('Глубина рекурсии:'))
size = int(input('Длина стороны:'))


def dandelion(size, depth):
    if depth == 0:
        turtle.forward(size)
    else:
        turtle.forward(size)
        for i in range(6):
            dandelion(size / 3, depth - 1)
            turtle.right(60)
        turtle.backward(size)


def dandelion_snowflake(size, depth):
    for i in range(6):
        dandelion(size, depth - 1)
        turtle.right(60)

dandelion_snowflake(size, depth)


def koch(size, depth):
    if depth == 0:
        turtle.forward(size)
    else:
        koch(size / 3, depth - 1)
        turtle.left(60)
        koch(size / 3, depth - 1)
        turtle.right(120)
        koch(size / 3, depth - 1)
        turtle.left(60)
        koch(size / 3, depth - 1)


def koch_snowflake(size, depth):
    for i in range(3):
        koch(size, depth)
        turtle.right(120)


koch_snowflake(size, depth)


def ice_1(size, depth):
    if depth == 0:
        turtle.forward(size)
    else:
        ice_1(size, depth - 1)
        turtle.left(90)
        ice_1(size / 2, depth - 1)
        turtle.right(180)
        ice_1(size / 2, depth - 1)
        turtle.left(90)
        ice_1(size, depth - 1)


ice_1(size, depth)


def color_tree(depth, size):
    turtle.colormode(255)
    cg = 255 - int(depth * (250 / 6)) % 255
    turtle.color(0, cg, 0)
    if depth == 0:
        return
    else:
        turtle.forward(size)
        turtle.left(45)
        color_tree(depth - 1, size / 2)
        turtle.right(90)
        color_tree(depth - 1, (size / 2))
        turtle.left(45)
        turtle.backward(size)


turtle.left(90)
color_tree(depth, size)
turtle.done()
