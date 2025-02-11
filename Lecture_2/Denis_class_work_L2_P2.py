# Равенства
a, b = 3, 5
print(a > b)
print(a < b)
print(a == b)
print(a <= b)


# Условие
AdminPass = "123"
Pass = input("Введите пароль\n")
if Pass == AdminPass:
    print("Пароль Админа")
else:
    print("Вы ввели -->", Pass)



# Условие с проверкой равенства
AdminPass = 123
while True:
    Pass = int(input("Угадайте число, иначе программа не закроется)\n"))
    if Pass == AdminPass:
        print("Угадали")
        break
    elif Pass > AdminPass:
        print("Загаданное число меньше")
    elif Pass < AdminPass:
        print("Загаданное число больше")
    else:
        print("Вы Угадали!!")


# Цикл while
number = 0
while number < 6:
    print(number)
    number += 1


# Цикл for
import time
for i in range(1, 4, 2):         # range --> c 1 to 4 step 2
    time.sleep(2)
    print(i)

# Проверка вхождения
st = "qwerty 236"
find = "0"
if find in st:
    print("Est")
else:
    print("Net")


# No print in
noPrint = "asdf"
st = input("Введите что-нибудь\n")
for s in st:
    if s in noPrint:
        continue
    print(s)


# and\or\not
times = 22             # and
age = 9

if times >= 21 and age < 18:
    print("Пора спать")
else:
    print("Чилим")


times = 22    # or
age = 91

if times < 21 or age < 18:
    print("Одно из условий истинно")
else:
    print("No")

print(not not not not True)   # not
True
