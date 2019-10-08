print ("ВВедите числа a, b, c, d, s, t, u (s и t одновременно не равны нулю)")
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
l_1 = s*a + t*b + u
l_2 = s*c + t*d + u
if l_1 < 0 and l_2 < 0 or l_1 > 0 and l_2 > 0:
    print ("Точки (A, B) и (C, D) принадлежат одной плоскости")
else:
    print("Точки (A, B) и (C, D) принадлежат разным плоскостям")