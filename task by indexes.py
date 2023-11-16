fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# Напишите программу, которая выводит первый элемент из списка.
# print(fruits[1])

# Выведите последний элемент из списка.
# print(fruits[-1])

# Выведите второй элемент из списка.
# print(fruits[2])

# Выведите предпоследний элемент из списка.
# print(fruits[-1::])

# Напишите программу, которая выводит все элементы списка в обратном порядке.
# print(fruits[::-1])

# Выведите все элементы списка, начиная с третьего и до конца.
# print(fruits[3::])

# Выведите каждый второй элемент из списка.
# print(fruits[2::2])

# Создайте новый список, который содержит первые пять элементов из исходного списка.
# print(fruits[:6])

# Создайте новый список, который содержит последние пять элементов из исходного списка.
# print(fruits[-5:])

# Выведите сумму всех элементов в списке.
numbers = [10, 20, 30, 40, 50, 30, 56, 30]
# summa = 0
# for index in range(len(numbers)):
#     summa += numbers[index]
# print(summa)

# Найдите среднее значение всех элементов в списке.
# summa = 0
# for index in range(len(numbers)):
#     summa += numbers[index]
# aver = summa / len(numbers)
# print(aver)

# Определите, сколько раз встречается определенное значение в списке.
# element_find = 30
# count = 0
# for index in range(len(numbers)):
#     if numbers[index] == element_find:
#         count += 1
#
# print(f"Значение {element_find} встречается {count} раз(а) в списке.")

# Определите, какие элементы списка больше заданного числа.
# num = 35
# list_num = []
# for index in range(len(numbers)):
#     if numbers[index] > num:
#         list_num.append(numbers[index])
# print(list_num)

# Выведите индекс первого вхождения определенного элемента в список.
# print(numbers)
# elem_find = 30
# for index in range(len(numbers)):
#     if numbers[index] == elem_find:
#         print(index)
#         break

# Найдите индекс последнего вхождения определенного элемента в список.
# elem_find = 30
# last_index = None
# for index in range(len(numbers)-1, -1, -1):
#     if numbers[index] == elem_find:
#         last_index = index
#         break
# print(last_index)

#чтобы найти второй индекс вхождения элемента в списке
# elem_find = 30
# count = 0  # Переменная для отслеживания количества вхождений
# for index in range(len(numbers)):
#     if numbers[index] == elem_find:
#         count += 1
#         if count == 2:  # Когда мы найдем второе вхождение
#             print(index)
#             break  # Прерываем цикл, так как нам больше не нужен

# Найдите индексы всех вхождений определенного элемента в список.
# element_find = 30
# for index in range(len(numbers)):
#     if element_find == numbers[index]:
#         print(index)

# Найдите минимальное значение в списке.
# min_el = float('inf')
# for index in range(len(numbers)):
#     if numbers[index] < min_el:
#         min_el = numbers[index]
# print(min_el)

# Найдите максимальное значение в списке.
# max_el = float('-inf')
# for index in range(len(numbers)):
#     if numbers[index] > max_el:
#         max_el = numbers[index]
# print(max_el)

# Отсортируйте список в порядке возрастания.
# list_sort = []
# for num in numbers:
#     for ind in range(len(list_sort)):
#         if num < list_sort[ind]:
#             list_sort.insert(ind, num)
#             break
#     else:
#         list_sort.append(num)
# print(list_sort)

# Отсортируйте список в порядке убывания.
# list_out = []
# for num in numbers:
#     for ind in range(len(list_out)):
#         if num > list_out[ind]:
#             list_out.insert(ind, num)
#             break
#     else:
#         list_out.append(num)
# print(list_out)

# Поменяйте местами два элемента списка по их индексам.
# print(numbers)
# ind_change1 = 2
# ind_change2 = 4
# # Check if the indices are valid
# if ind_change1 < len(numbers) and ind_change2 < len(numbers):
#     # Swap the elements
#     numbers[ind_change1], numbers[ind_change2] = numbers[ind_change2], numbers[ind_change1]
# print(numbers)

# Создайте новый список, который содержит только уникальные элементы исходного списка.
# print(numbers)
# list_out = []
# for ind in range(len(numbers)):
#     if numbers[ind] not in list_out:
#         list_out.append(numbers[ind])
#     else:
#         pass
# print(list_out)

# Переверните список так, чтобы его порядок был обратным, но при этом оригинальный список оставался без изменений.
# list_reverse = []
# print(numbers)
# for index in range(len(numbers)-1, -1, -1):
#     list_reverse.append(numbers[index])
# print(list_reverse)

# Удалите первый элемент из списка.
# print(numbers)
# numbers.pop(1)
# print(numbers)

# Удалите последний элемент из списка.
# print(numbers)
# numbers.pop(-1)
# print(numbers)

# Вставьте новый элемент в середину списка.
# print(numbers)
# element_insert = 15
# numbers.insert(3, element_insert)
# print(numbers)

# Удалите все вхождения определенного элемента из списка.
# print(numbers)
# elem_del = 30
# index = 0
# while index < len(numbers):
#     if numbers[index] == elem_del:
#         numbers.pop(index)
#     else:
#         index += 1
# print(numbers)

# Подсчитайте, сколько элементов в списке меньше заданного значения.
# counter = 0
# elem = 30
# for ind in range(len(numbers)):
#     if numbers[ind] < elem:
#         counter += 1
# print(counter)

# Подсчитайте, сколько элементов в списке больше заданного значения.
# counter = 0
# elem = 30
# for ind in range(len(numbers)):
#     if numbers[ind] > elem:
#         counter += 1
# print(counter)

# Создайте список, который состоит из копий элементов исходного списка, умноженных на определенное число.
# list_out = []
# for ind in range(len(numbers)):
#     list_out.append(numbers[ind] ** 2)
# print(list_out)

# list_out = [num ** 2 for num in numbers]
# print(list_out)

# Найдите разницу между соседними элементами списка.
# print(numbers)
# list_out = []
# for ind in range(len(numbers)-1):
#     list_out.append((numbers[ind+1] - numbers[ind-1]))
# print(list_out)

# Найдите сумму всех элементов списка, стоящих на четных позициях.
# print(numbers)
# summa = 0
# for ind in range(2, len(numbers), 2):
#     summa += numbers[ind]
# print(summa)

# Найдите произведение всех элементов списка, стоящих на нечетных позициях.
# multiplace = 1
# for index in range(1, len(numbers), 2):
#     multiplace *= numbers[index]
# print(multiplace)

# Выведите элементы списка в обратном порядке, используя только срезы.
# print(numbers)
# list_out = []
# for ind in range(len(numbers)):
#     list_out.append(numbers[-(ind + 1)])
# print(list_out)

# Определите, является ли список палиндромом (читается одинаково слева направо и справа налево).
# is_palindrome = True
# for i in range(len(numbers)//2):
#     if numbers[i] != numbers[-(i+1)]:
#         is_palindrome = False
#         break
#
# if is_palindrome:
#     print("Список является палиндромом")
# else:
#     print("Список не является палиндромом")

# Создайте новый список, в котором каждый элемент равен сумме элемента исходного списка и его индекса.
# print(numbers)
# list_out = []
# for index, el in enumerate(numbers):
#     list_out.append((el + index))
# print(list_out)

# Создайте новый список, который содержит только элементы с четными индексами.
# print(numbers)
# list_out = []
# for ind in range(0, len(numbers),2):
#     list_out.append(numbers[ind])
# print(list_out)

# Создайте новый список, который содержит только элементы с нечетными индексами.
# list_new = []
# for ind in range(len(numbers)):
#     if ind % 2 != 0:
#         list_new.append(numbers[ind])
# print(list_new)

# list_new = []
# for ind in range(1, len(numbers), 2):
#     list_new.append(numbers[ind])
# print(list_new)

# Создайте новый список, в котором элементы исходного списка упорядочены по убыванию.
# new = sorted(numbers, key=lambda elem: elem, reverse=True)
# print(new)

# sorted_numbers = []
# for num in numbers:
#     for index in range(len(sorted_numbers)):
#         if num > sorted_numbers[index]:
#             sorted_numbers.insert(index, num)
#             break
#     else:
#         sorted_numbers.append(num)
# print(sorted_numbers)

# Создайте новый список, который содержит элементы исходного списка в обратном порядке исходного списка.
# list_reverse = []
# for index in range(len(numbers)-1, -1, -1):
#     list_reverse.append(numbers[index])
# print(list_reverse)