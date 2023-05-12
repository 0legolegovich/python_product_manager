"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
number = int(input('Введите целое положительное число n:'))
target_number = number + number*11 + number*111
print(target_number)