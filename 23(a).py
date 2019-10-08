import math
a = int(input("Введите A"))
b = int(input("Введите B"))
c = int(input("Введите C"))
p = (a + b + c)/2
h_1 = 2/ a*math.sqrt(p*(p - a)*(p - b)*(p - c))
h_2 = 2/ b*math.sqrt(p*(p - a)*(p - b)*(p - c))
h_3 = 2/ c*math.sqrt(p*(p - a)*(p - b)*(p - c))
print ("h_1 =", h_1)
print ("h_2 =", h_2)
print ("h_3 =", h_3)
