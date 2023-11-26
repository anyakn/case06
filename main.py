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


print('Доступные фракталы на рисования:', 'Бесконечные квадраты', 'Кривая Леви', 'Дракон', 'Ромб', sep='\n')

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

    else:
        print('Такого фрактала нет. Повторите попытку!')

turtle.done()
