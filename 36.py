import math
a = int(input("Введите A"))
b = int(input("Введите B"))
c = int(input("Введите C"))
if a < b:
    print (a < b)
    if b < c:
        print ("Равенство верно")
    else:
       print ("равенство ложно")
else:
    print ("равенство ложно")