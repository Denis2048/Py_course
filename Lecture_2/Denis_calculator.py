# OLD
# first_number = input("Put first integer number:")
# second_number = input("Put second integer number:")
# first_number = int(first_number)
# second_number = int(second_number)
#
# print("\nResult of match! + - * /")
# print(first_number, "+", second_number, "=", first_number + second_number)
# print(first_number, "-", second_number, "=", first_number - second_number)
# print(first_number, "*", second_number, "=", first_number * second_number)
# print(first_number, "/", second_number, "=", first_number / second_number)

# Refactoring
first_number, second_number = int(input("Put first integer number: ")),\
    int(input("Put second integer number: "))

print("\nResult of match! + - * /")
print(f'{first_number} + {second_number} = {first_number + second_number}')
print(f'{first_number} - {second_number} = {first_number - second_number}')
print(f'{first_number} * {second_number} = {first_number * second_number}')
print(f'{first_number} / {second_number} = {first_number / second_number}')
