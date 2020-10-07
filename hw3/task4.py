"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
** Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def pow1(x, y):
    return 1 / (x ** (-y))


def pow2(x, y):
    counter = 1
    buff = x
    while (-y) > counter:
        x *= buff
        counter += 1
    return 1/x


x = float(input("Enter a real number (separator is a dot): "))
y = int(input("Enter a negative integer: "))
while y >= 0:
    y = int(input("Enter a negative integer: "))
print(pow1(x, y))
print(pow2(x, y))
