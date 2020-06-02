# Напишите программу, которая считает площадь прямоугольника, спрашивая у пользователя длину двух сторон
a = int(input('Введи длину одной стороны прямоугольника: '))
b = int(input('Введи длину другой стороны прямоугольника: '))
s = a * b
print(s)

# Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-"
while True:
    number_one = int(input('Введи первое число: '))
    number_two = int(input('Введи второе число: '))
    action = input('Какое действие будем делать над числами? (+ или -): ')
    if action == '+':
        result = number_one + number_two
        print(result)
        break
    elif action == '-':
        result = number_one - number_two
        print(result)
        break
    else:
        print('Нужно ввести + или -')

# Напишите программу, которая находит все простые числа между 0 и пользовательским числом
user_input = int(input('Введите число: '))
for i in range(0, user_input + 1):
    if i % 2 != 0:
        print(i)

# Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами
while True:
    num_one = int(input('Введите первое число: '))
    num_two = int(input('Введите второе число, оно должно быть больше первого: '))
    if num_two < num_one:
        print('Второе число должно быть больше первого!')
        continue
    else:
        for i in range(num_one, num_two + 1):
            if i % 5 == 0:
                print(i)
        break

