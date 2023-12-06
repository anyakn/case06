import turtle

turtle.speed(-1)


def square(n_s):
    for i in range(4):
        turtle.fd(n_s)
        turtle.rt(90)

    turtle.fd(0.1*n_s)
    turtle.rt(10)


def rec_square(n_s):
    if n_s <= 0:
        return None
    square(n_s)
    turtle.rt(5)
    return rec_square(0.9 * n_s)


def levy(n_l, size_l):
    if n_l == 0:
        turtle.fd(size_l)
    else:
        turtle.lt(45)
        levy(n_l - 1, size_l)
        turtle.rt(90)
        levy(n_l - 1, size_l)
        turtle.lt(45)


def dragon(n_d, size_d, sign_d):
    if n_d == 0:
        turtle.fd(size_d)
    else:
        turtle.lt(45*sign_d)
        dragon(n_d - 1, size_d / (2**0.5), 1)
        turtle.rt(90*sign_d)
        dragon(n_d - 1, size_d / (2 ** 0.5), -1)
        turtle.lt(45*sign_d)


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


def color_tree(depth, size):
  turtle.colormode(255)
  cg = 255 - int(depth * (250/6)) % 255
  turtle.color(0, cg, 0)
  if depth == 0:
    return
  else:
    turtle.forward(size)
    turtle.left(45)
    color_tree(depth-1, size / 2)
    turtle.right(90)
    color_tree(depth-1, (size/2))
    turtle.left(45)
    turtle.backward(size)

def minkowski(order, size):
    if order == 0:
        turtle.fd(size)
    else:
        minkowski(order-1, size/2)
        turtle.lt(90)
        minkowski(order-1, size/2)
        turtle.rt(90)
        minkowski(order-1, size/2)
        turtle.rt(90)
        minkowski(order-1, size)
        turtle.lt(90)
        minkowski(order-1, size/2)
        turtle.lt(90)
        minkowski(order-1, size/2)
        turtle.rt(90)
        minkowski(order-1, size/2)

def ice_fractal2(order, size):
    if order == 0:
        turtle.fd(size)
    else:
        ice_fractal2(order-1, size/2)
        turtle.lt(120)
        ice_fractal2(order-1, size/4)
        turtle.rt(180)
        ice_fractal2(order-1, size/4)
        turtle.lt(120)
        ice_fractal2(order-1, size/4)
        turtle.rt(180)
        ice_fractal2(order - 1, size / 4)
        turtle.lt(120)
        ice_fractal2(order - 1, size / 2)


print('Доступные фракталы на рисования:', 'Бесконечные квадраты', 'Двоичное дерево',
      'Кривая Леви', 'Дракон', 'Ромб', 'Снежинка Коха',
      'Снежинка-одуванчик', 'Кривая Минковского', 'Ледяной фрактал 1', 'Ледяной фрактал 2', sep='\n')

k = 0
while k < 1:
    choice = input('Выберите фрактал: ').lower()
    if choice == 'бесконечные квадраты':
        k += 1
        size = int(input('Введите длину: '))
        rec_square(size)

    elif choice == 'кривая леви':
        k += 1
        n = int(input('Введите глубину рекурсии: '))
        size = int(input('Введите длину: '))
        levy(n, size)

    elif choice == 'дракон':
        k += 1
        n = int(input('Введите глубину рекурсии: '))
        size = int(input('Введите длину: '))
        sign = int(input('Введите знак(-1 или 1): '))
        dragon(n, size, sign)

    elif choice == 'ромб':
        k += 1
        xr = int(input('Введите координату x: '))
        yr = int(input('Введите координату y: '))
        rr = int(input('Введите радиус: '))
        n = int(input('Введите глубину рекурсии: '))
        rhombus(xr, yr, rr, n)

    elif choice == 'снежинка коха':
        k += 1
        depth = int(input('Глубина рекурсии:'))
        size = int(input('Длина стороны:'))
        koch_snowflake(size, depth)

    elif choice == 'снежинка-одуванчик':
        k += 1
        depth = int(input('Глубина рекурсии:'))
        size = int(input('Длина стороны:'))
        dandelion_snowflake(size, depth)

    elif choice == 'ледяной фрактал 1':
        k += 1
        depth = int(input('Глубина рекурсии:'))
        size = int(input('Длина стороны:'))
        ice_1(size, depth)

    elif choice == 'двоичное дерево':
        k += 1
        depth = int(input('Глубина рекурсии:'))
        size = int(input('Длина стороны:'))
        turtle.left(90)
        color_tree(depth, size)

    elif choice == 'кривая минковского':
        k += 1
        depth = int(input('Глубина рекурсии:'))
        size = int(input('Длина стороны:'))
        minkowski(depth, size)

    elif choice == 'ледяной фрактал 2':
        k += 1
        depth = int(input('Глубина рекурсии:'))
        size = int(input('Длина стороны:'))
        ice_fractal2(depth, size)

    else:
        print('Такого фрактала нет. Повторите попытку!')

turtle.done()
