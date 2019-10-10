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
    print ("a =", a)
    print ("b =", b)
    del x, y, z, a, b
    if len(home_work) == 0:
        sys.exit()

def twenty_three_a(a, b, c):
    p = (a + b + c) / 2
    h_1 = 2 / a * math.sqrt(p * (p - a) * (p - b) * (p - c))
    h_2 = 2 / b * math.sqrt(p * (p - a) * (p - b) * (p - c))
    h_3 = 2 / c * math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("h_1 =", h_1)
    print("h_2 =", h_2)
    print("h_3 =", h_3)
    del a, b, c
    if len(home_work) == 0:
        sys.exit()

def thirty_one_3(a):
    a_1 = a * a
    print("a_1 =", a_1)
    a_2 = a_1 * a
    print("a_2 =", a_2)
    a_3 = a_2 * a_2
    print("a_3 =", a_3)
    a_4 = a_3 * a_2
    print("a_4 =", a_4)
    a_5 = a_4 * a_3
    print("a_5 =", a_5)
    check = pow(a, 15)
    print("check =", check)
    a = 0
    if len(home_work) == 0:
        sys.exit()

def thirty_six(a, b, c):
    if a < b:
        print(a < b)
        if b < c:
            print("Равенство верно")
        else:
            print("равенство ложно")
    else:
        print("равенство ложно")
    del a, b, c
    if len(home_work) == 0:
        sys.exit()

def fifty_two(a, b, c, d, s, t, u):
    l_1 = s * a + t * b + u
    l_2 = s * c + t * d + u
    if l_1 < 0 and l_2 < 0 or l_1 > 0 and l_2 > 0:
        print("Точки (A, B) и (C, D) принадлежат одной плоскости")
    else:
        print("Точки (A, B) и (C, D) принадлежат разным плоскостям")
    del a, b, c, d, s, t, u
    if len(home_work) == 0:
        sys.exit()

while True:
    task = int(input("Введите номер задачи"))
    for i in home_work:
        if i == task:
            home_work.remove(task)
    if task == 1:
        x = int(input("Введите Х"))
        y = int(input("Введите Y"))
        z = int(input("Введите Z"))
        eleven_b(x, y, z)
    elif task == 2:
        a = int(input("Введите A"))
        b = int(input("Введите B"))
        c = int(input("Введите C"))
        twenty_three_a(a, b, c)
    elif task == 3:
        a = int(input("Введите A"))
        thirty_one_3(a)
    elif task == 4:
        a = int(input("Введите A"))
        b = int(input("Введите B"))
        c = int(input("Введите C"))
        thirty_six(a, b, c)
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
        fifty_two(a, b, c, d, s, t, u)
    else:
        print("Нет такого номера")