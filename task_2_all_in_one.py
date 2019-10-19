import sys
import random
import string
import textwrap
print("Программа состоит из десяти задач")
print("1 - 12")
print("2 - 25")
print("3 - 38")
print("4 - 51")
print("5 - 4")
print("6 - 17")
print("7 - 30")
print("8 - 43")
print("9 - 56")
print("10 - 9")
home_work = [1,2,3,4,5,6,7,8,9,10]

class Home_work_2(object):

    def __init__(self, a=0, s='', s_1='', s_2='', s_3=''):
        """Constructor"""
        self.a = a
        self.s = s
        self.s_1 = s_1
        self.s_2 = s_2
        self.s_3 = s_3

    def twelve(self, a):
        d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
             (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        roman = ''
        while a > 0:
            for i, r in d:
                while a >= i:
                    roman += r
                    a -= i
        return (roman)

    def twenty_five(self, a):
        out = ""
        b = " "
        for t in a:
            out += t + b
        return (out[:-1])

    def thirty_eight(self, s):
        s = s.replace('xabc', 'abc')
        return (s)

    def fifty_one(self, s_1, s_2):
        s_3 = ''
        output = ''
        for i in s_2:
            for j in s_1:
                if i == j:
                    s_3 = s_3[:] + j
        for x in s_3:
            if x not in output:
                output = output[:] + x
        return (output)

    def four(self, s):
        s_1 = s.split()
        return (' '.join(s_1))

    def seventeen(self, s):
        return (s[2::3])

    def thirty(self, s_1, s_2, s_3):
        s_4 = [s_1] + [s_2] + [s_3]
        return (sorted(s_4, key=len))

    def forty_three(self, s):
        counter = 0
        for i in s:
            if i.isdigit():
                counter += 1
        return (counter)

    def fifty_six(self, s):
        letter = ''
        s = s.lower()
        for c in string.punctuation:
            s = s.replace(c, "")
        for symbol in s:
            if 'aeiouyаоиеёэыуюя'.find(symbol) != -1:
                letter = letter[:] + symbol
        a = [x for x in letter]
        a.sort()
        a.insert(0, s)
        return (a)

    def nine(self, s):
        split_len = 3
        letter = ''
        a = ' '
        s = s.replace(' ', '')
        s = textwrap.wrap(s, 3)
        for i in s:
            index = 1
            a = random.choice(string.ascii_letters)
            try:
                while a == i[0]:
                    a = random.choice(string.ascii_letters)
            except:
                pass
            try:
                while a == i[2]:
                    a = random.choice(string.ascii_letters)
            except:
                pass
            i = i[:index] + a + i[index + 1:]
            letter = letter[:] + i
        letter = textwrap.wrap(letter, 3)
        letter.sort()
        return (letter)

if __name__ == "__main__":
    while True:
        task = int(input("Введите номер задачи"))
        for i in home_work:
            if i == task:
                home_work.remove(task)
        if task == 1:
            print("12.В строке записано десятичное число. Запишите данное число римскими цифрами.")
            a = int(input("Введите число"))
            task_1 = Home_work_2()
            print(task_1.twelve(a))
            if len(home_work) == 0:
                sys.exit()
        elif task == 2:
            print("25.Дана строка. Вставить после каждого символа пробел.")
            a = input("Введите cтроку")
            task_2 = Home_work_2(a)
            print(task_2.twenty_five(a))
            if len(home_work) == 0:
                sys.exit()
        elif task == 3:
            print("38.Удалите в строке все буквы 'x'. за которыми следует 'abc'.")
            s = (input("Введите строку"))
            task_3 = Home_work_2()
            print(task_3.thirty_eight(s))
            if len(home_work) == 0:
                sys.exit()
        elif task == 4:
            print("51.Даны две строки. Определите, можно ли из некоторых символов первой строки составить вторую строку.")
            s_1 = (input("Введите первую строку"))
            s_2 = (input("Введите вторую строку"))
            task_4 = Home_work_2()
            print(*task_4.fifty_one(s_1, s_2))
            if len(home_work) == 0:
                sys.exit()
        elif task == 5:
            print("4.В строке найдите все серии подряд идущих пробелов и замените каждую на один пробел.")
            s = (input("Введите строку"))
            task_5 = Home_work_2()
            print(task_5.four(s))
            if len(home_work) == 0:
                sys.exit()
        elif task == 6:
            print("17.Дана строка. Показать третий, шестой, девятый и так далее символы.")
            s = (input("Введите строку"))
            task_6 = Home_work_2()
            print(task_6.seventeen(s))
            if len(home_work) == 0:
                sys.exit()
        elif task == 7:
            print("30.Дан массив строк. Упорядочить массив по длине строк.")
            s_1 = (input("Введите первую строку"))
            s_2 = (input("Введите вторую строку"))
            s_3 = (input("Введите третью строку"))
            task_7 = Home_work_2()
            print(task_7.thirty(s_1, s_2, s_3))
            if len(home_work) == 0:
                sys.exit()
        elif task == 8:
            print("43.В данной строке найти количество цифр.")
            s = (input("Введите строку"))
            task_8 = Home_work_2()
            print(task_8.forty_three(s))
            if len(home_work) == 0:
                sys.exit()
        elif task == 9:
            print(
                "56. Вывести слова, в которых заменить каждую большую букву одно-именной малой; удалить все символы,\n"
                "не являющиеся буквами или цифрами; вывести в алфавитном порядке все гласные буквы, входящие в каждое\n "
                "слово строки.")
            s = (input("Введите строку"))
            task_9 = Home_work_2()
            print(task_9.fifty_six(s))
            if len(home_work) == 0:
                sys.exit()
        elif task == 10:
            print(
                "Дана строка. Разделить строку на фрагменты по три подряд идущих символа. В каждом фрагменте средний\n"
                " символ заменить на случайный символ, не совпадающий ни с одним из символов этого фрагмента.\n"
                "Показать фрагменты, упорядоченные по алфавиту.")
            s = (input("Введите строку"))
            task_10 = Home_work_2()
            print(task_10.nine(s))
            if len(home_work) == 0:
                sys.exit()
        else:
            print("Нет такого номера")