# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(num1, num2, num3):
    # Функция возвращает сумму наибольших двух аргументов

    lst = [num1, num2, num3]
    summ = sum(lst) - min(lst)
    return summ


print(my_func(100, 50, 30))
