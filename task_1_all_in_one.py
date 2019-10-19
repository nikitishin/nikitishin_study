import math
import sys
print("Программа состоит из пяти задач")
print("1 - 11(b)")
print("2 - 23(a)")
print("3 - 31(3)")
print("4 - 36")
print("5 - 52")
home_work = [1,2,3,4,5,]

def eleven_b(x, y, z):
    a = (3 + math.exp(y - 1))/ (1+ pow(x,2)* math.fabs(y - math.tan(z)))
    b = 1 + math.fabs(y - x) + pow(y - x,2)/ 2 + pow(math.fabs(y - x), 3)/ 3
    return (a, b)

def twenty_three_a(a, b, c):
    p = (a + b + c) / 2
    h_1 = 2 / a * math.sqrt(p * (p - a) * (p - b) * (p - c))
    h_2 = 2 / b * math.sqrt(p * (p - a) * (p - b) * (p - c))
    h_3 = 2 / c * math.sqrt(p * (p - a) * (p - b) * (p - c))
    return (h_1, h_2, h_3)

def thirty_one_3(a):
    a_1 = a * a
    a_2 = a_1 * a
    a_3 = a_2 * a_2
    a_4 = a_3 * a_2
    a_5 = a_4 * a_3
    a = 0
    return (a_5)

def thirty_six(a, b, c):
    L = []
    if a < b:
        if b < c:
            L[:] = ['Равенство верно']
        else:
            L[:] = ['Равенство ложно']
    else:
        L[:] = ['Равенство ложно']
    del a, b, c
    return (L)

def fifty_two(a, b, c, d, s, t, u):
    L = []
    l_1 = s * a + t * b + u
    l_2 = s * c + t * d + u
    if l_1 < 0 and l_2 < 0 or l_1 > 0 and l_2 > 0:
        L[:] = ['Точки (A, B) и (C, D) принадлежат одной плоскости']
    else:
        L[:] = ['Точки (A, B) и (C, D) принадлежат разным плоскостям']
    del a, b, c, d, s, t, u
    return (L)

while True:
    task = int(input("Введите номер задачи"))
    for i in home_work:
        if i == task:
            home_work.remove(task)
    if task == 1:
        x = int(input("Введите Х"))
        y = int(input("Введите Y"))
        z = int(input("Введите Z"))
        #print(*eleven_b(x, y, z),sep ='\n')
        print (*eleven_b(x, y, z))
        if len(home_work) == 0:
            sys.exit()
    elif task == 2:
        print("Введите стороны треугольника")
        a = int(input("Введите A"))
        b = int(input("Введите B"))
        c = int(input("Введите C"))
        print(*twenty_three_a(a, b, c))
        if len(home_work) == 0:
            sys.exit()
    elif task == 3:
        print("Возвести в степень число за 5 действий, используя только умножение")
        a = int(input("Введите число"))
        print(thirty_one_3(a))
        if len(home_work) == 0:
            sys.exit()
    elif task == 4:
        print("Верно ли равенство A < B < C")
        a = int(input("Введите A"))
        b = int(input("Введите B"))
        c = int(input("Введите C"))
        print(*thirty_six(a, b, c))
        if len(home_work) == 0:
            sys.exit()
    elif task == 5:
        print("ВВедите числа a, b, c, d, s, t, u (s и t одновременно не равны нулю)")
        a = int(input("Введите A"))
        b = int(input("Введите B"))
        c = int(input("Введите C"))
        d = int(input("Введите D"))
        s = int(input("Введите S"))
        t = int(input("Введите T"))
        if s == 0 and t == 0:
            print("s и t одновременно не равны нулю")
            s = int(input("Введите S"))
            t = int(input("Введите T"))
        u = int(input("Введите U"))
        print(*fifty_two(a, b, c, d, s, t, u))
        if len(home_work) == 0:
            sys.exit()
    else:
        print("Нет такого номера")
