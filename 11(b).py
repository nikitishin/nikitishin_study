import math
x = int(input("Введите Х"))
y = int(input("Введите Y"))
z = int(input("Введите Z"))
a = (3 + math.exp(y - 1))/ (1+ pow(x,2)* math.fabs(y - math.tan(z)))
b = 1 + math.fabs(y - x) + pow(y - x,2)/ 2 + pow(math.fabs(y - x), 3)/ 3
print ("a =", a)
print ("b =", b)
