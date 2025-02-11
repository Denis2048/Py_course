# input
Pass = input("Введите пароль\n")
print("Пароль", Pass)

# type
Pass = input("Введите пароль\n")
print("Пароль", type(Pass))

Pass = int(input("Введите пароль\n"))   # Преобразование в инт
print("Пароль", type(Pass))

# String operators, autoConcatenation
str1 = "first" "last"
print(str1)

str1 = ("first" "last"
        "123")
print(str1)

str1 = ("first" "last"\
        "123")
print(str1)

str1 = input("Введите что-нибудь--->")   # Funk len()
print(len(str1))

str1, str2 = input("Введите что-нибудь--->"), input("Введите ещё--->")   # Summ str
print(str1 + str2)

# format
str1, str2 = input("Введите что-нибудь--->"), input("Введите ещё--->")   # Summ str
print(f'{str1} + {str2}')

# right-sided
print(3**2**2) # Если более 2х

# Python keywords
import keyword
print(keyword.kwlist)

# calculator
a = 6
b = 3
c = 1
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)
print(a, "/", b, "=", a / b)

a = 6
b = 3
c = 1
print(f'{a} + {b} = {a + b}')  # Steel++++ ;)
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
