x = int(input("Введите year"))
y = x
y = y % 400
a = y % 4
b = y % 100
c = y // 100
l_y = (0**a) * ((1-(0**b)) + 0**c)
if not l_y:
    print (x,":Обычный год")
else:
    print (x,":Высокосный год")