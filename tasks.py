# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Дана последовательность чисел. Получить список уникальных элементов 
# заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


def single_numbers(numbers):
    set1 = set()
    n = len(numbers)
    for i in numbers:
        if i in set1:
            set1.remove(i)
        else:
            set1.add(i)
    print("Неповторяющиеся элементы списка : " + " ".join(map(str, set1)))
    

numbers = list(map(str, input('Введите числа списка через пробел: ').split()))
single_numbers(numbers)

# Найти сумму чисел списка стоящих на нечетной позиции

# import random


# def odd_sum(a, n):
#     odd_sum = sum(a[1::2])
#     print(f'Сумма чисел, стоящих на нечётных позициях = {odd_sum}')


# my_list = [random.randrange(1, 20) for i in range(10)]
# print ("Строка случайных чисел: " + str(my_list))
# n = len(my_list)
# odd_sum(my_list, n)
