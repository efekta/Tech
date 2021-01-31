# Напишите программу, которая считает площадь прямоугольника,
# спрашивая у пользователя длину двух сторон

#a = int(input('Введите одну сторону прямоугольника: '))
#b = int(input('Введите другую сторону прямоугольника: '))
#s = a * b
#print(s)

# Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-".
# В зависимости от знака выводит их сумму или разницу

# num_1 = input('Введите число: ')
# num_2 = input('Введите второе число: ')
# quiz_operation = input('Введите знак + или - : ')
#
# if quiz_operation == '+':
#     if num_1.isdigit() or num_2.isdigit():
#         result = int(num_1) + int(num_2)
#         print('Результат операции над {} и {} равен: {}'.format(num_1, num_2, result))
#     else:
#         print('Введите число!')
# elif quiz_operation == '-':
#     if num_1.isdigit() or num_2.isdigit():
#         result = int(num_1) - int(num_2)
#         print('Результат операции над {} и {} равен: {}'.format(num_1, num_2, result))
#     else:
#         print('Введите число!')
# elif quiz_operation != '-' and quiz_operation != '+':
#     print('Нужно вводить знак либо +, либо - !!!')

# Напишите программу, которая находит все простые числа между 0 и пользовательским числом

# n = int(input("Введите верхнюю границу диапазона: "))
# sieve = set(range(2, n + 1))
# while sieve:
#     prime = min(sieve)
#     print(prime, end="\t")
#     sieve -= set(range(prime, n + 1, prime))

# Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами

# num_first = int(input('Введите число: '))
# num_second = int(input('Введите второе число: '))
#
# def Fived(a, b):
#     if num_first >= num_second:
#         print('Второе число должно быть больше, чем первое!')
#     else:
#         for i in range(num_first, num_second + 1):
#             if i % 5 == 0:
#                 print(i)
# Fived(num_first, num_second)







