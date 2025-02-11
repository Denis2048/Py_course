################ home work 2.1

number1, number2, number3, number4 = int(input("Число 1 --> ")), int(input("Число 2 --> ")),\
    int(input("Число 3 --> ")), int(input("Число 4 --> "))
max_number = number1         # За максимальное число принимаем первое значение и сравниваем с остальными
if number2 > max_number:
    max_number = number2

if number3 > max_number:
    max_number = number3

if number4 > max_number:
    max_number = number4

print(f'Максимальное число {max_number}\n {type(max_number)}')



################# home work 2.4

import time
for i in range(1, 6, 1):
    print(f'{i} Mississippi')
    time.sleep(1)
print("Ready or not, here I come!")



################## home work 2.6

operation = input("Введите операцию '+' '-' '*' '/'\nили exit для выхода --> ")
while operation != "exit":
    num1, num2 = int(input("Введите первое число --> ")), int(input("Введите второе число --> "))
    if operation == "+":
        print(f'Результат = {num1 + num2}')
    elif operation == "-":
        print(f'Результат = {num1 - num2}')
    elif operation == "*":
        print(f'Результат = {num1 * num2}')
    elif operation == "/":
        print(f'Результат = {num1 / num2}')
    operation = input("Введите операцию '+' '-' '*' '/'\nили exit для выхода --> ")

