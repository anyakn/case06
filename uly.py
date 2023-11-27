import turtle

def minkowski(t, order, size):
    if order == 0:
        t.fd(size)
    else:
        minkowski(t, order-1, size/4)
        t.lt(90)
        minkowski(t, order-1, size/4)
        t.rt(90)
        minkowski(t, order-1, size/4)
        t.rt(90)
        minkowski(t, order-1, size/4)
        minkowski(t, order-1, size/4)
        t.lt(90)
        minkowski(t, order-1, size/4)
        t.lt(90)
        minkowski(t, order-1, size/4)
        t.rt(90)
        minkowski(t, order-1, size/4)

# Установка начальных параметров
t = turtle.Turtle()
t.speed(0)
t.pu()
t.goto(-200, 0)
t.pd()

# Вызов функции для построения кривой Минковского различной глубины рекурсии
depth = 3
size = 400
minkowski(t, depth, size)

turtle.done()



def snowflake(t, order, size):
    if order == 0:
        t.fd(size)
    else:
        snowflake(t, order-1, size/3)
        t.lt(60)
        snowflake(t, order-1, size/3)
        t.rt(120)
        snowflake(t, order-1, size/3)
        t.lt(60)
        snowflake(t, order-1, size/3)

# Установка начальных параметров
t = turtle.Turtle()
t.speed(0)
t.pu()
t.goto(-200, 0)
t.pd()

# Вызов функции для построения ледяного фрактала различной глубины рекурсии
depth = 4
size = 300
for _ in range(3):
    snowflake(t, depth, size)
    t.rt(120)

turtle.done()
