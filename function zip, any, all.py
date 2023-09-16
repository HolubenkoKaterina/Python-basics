# Задача на сложение элементов из двух списков, используя функцию zip.
# list1 = [5, 15, 20, 25]
# list2 = [10, 15, 20, 25]
# suuma_listov = [elem + element for elem, element in zip(list1, list2)]
# print(suuma_listov)

# Найти произведение элементов из двух списков, объединенных через zip.
# list1 = [5, 15, 20, 25]
# list2 = [10, 15, 20, 25]
# resalt_multiplace = [elem * element for elem, element in zip(list1, list2)]
# print(resalt_multiplace)

# Создать словарь из двух списков: один список ключей, другой - значений, используя zip.
# list1 = [4, 5, 'priz', 'lastik']
# list2 = ['loshadi', 'horse', '54', 55]
# union = list(zip(list1, list2))
# dict_out = {elem[0]: elem[1] for elem in union}
# print(dict_out)

# Проверить, есть ли хотя бы одно отрицательное число в списке, используя any.
# list1 = [5, 15, 20, 25]
# check = any(elem < 0 for elem in list1)
# print(check)

# Проверить, есть ли хотя бы одна строка с длиной более 10 символов в списке, используя any.
# list1 = ['priz', 'lastik']
# check = any(len(elem) > 10 for elem in list1)
# print(check)

# Подсчитать количество пар элементов с одинаковыми индексами из двух списков, (используя zip) которые равны между собой.
# Создать список строк, объединяя элементы из двух списков с помощью zip.
# list1 = [4, 5, 'priz', 'lastik']
# list2 = ['loshadi', 'horse', '54', 55]
# list_out = list(zip(list1, list2))
# print(list_out)

# Найти разницу между соответствующими элементами из двух списков, объединенных через zip.
# list1 = [5, 15, 20, 25]
# list2 = [10, 15, 20, 25]
# resalt = [elem - element for elem, element in zip(list1, list2)]
# print(resalt)

# Проверить, все ли элементы в списке положительные числа, используя all.
# list1 = [4, 5, 6, -18]
# check = all(elem for elem in list1 if elem > 0)
# if check == True: print(True)
# if check != True: print(False)

# Проверить, все ли строки в списке имеют длину более 5 символов, используя all.
# text = ['my mind', 'coffe is fu', 'mama help me!']
# for element in text:
# check = all(len(element) > 5 for element in text)
# if check == True: print(True)
# if check != True: print(False)

# Проверить, все ли элементы в списке являются четными числами, используя all.
# list1 = [4, 5, 6, -18]
# check = all(elem % 2 == 0 for elem in list1 )
# print(check)

# Проверить, есть ли хотя бы одно нечетное число в списке, используя any.
# list1 = [4, 5, 6, -18]
# check = any(elem < 0 for elem in list1)
# print(check)

# Проверить, есть ли хотя бы один элемент в списке, удовлетворяющий определенному условию, используя any.
# list1 = [4, 5, 6, 18]
# check = any(elem < 0 and elem % 2 == 0 for elem in list1)
# print(check)

# Проверить, есть ли хотя бы одна пара элементов с одинаковыми индексами, которые больше заданного порога.
# list1 = [5, 5, 2, 3]
# list2 = [10, 5, 2, 13]
# some_number = int(input("введите ваше число..."))
# check = any(elem > some_number and element > some_number for elem, element in zip(list1, list2))
# print(check)

# Написать функцию, которая объединяет несколько списков в один, используя zip.
# list1 = [5, 15, 20, 25]
# list2 = [10, 15, 20, 25]
# resalt = list(zip(list1, list2))
# print(resalt)

# Создать новый список, содержащий только четные элементы из двух списков, объединенных через zip.
# list1 = [5, 15, 20, 25]
# list2 = [10, 15, 20, 25]
#
# Проверить, все ли элементы в списке удовлетворяют определенному условию, используя all.
# list1 = [5, 15, 20, 25]
# check = all(elem % 2 == 0 for elem in list1)
# print(check)

# Проверить, все ли слова в списке начинаются с заглавной буквы, используя all.
# text = ['My Mind', 'Coffe Is Fu', 'Mama Help Me!']
# check = all(elem.istitle() for elem in text)
# print(check)

# Проверить, все ли элементы в списке находятся в диапазоне от 10 до 20, используя all.
# list1 = [15, 20, 19]
# check = all(elem in range(10, 21) for elem in list1)
# print(check)

# Проверить, есть ли хотя бы одна строка в списке, начинающаяся с заглавной буквы, используя any.
# text = ['My Mind', 'Coffe Is Fu', 'Mama Help Me!']
# check = any(elem.istitle() for elem in text)
# print(check)

# Проверить, есть ли хотя бы один элемент в списке, находящийся в диапазоне от 5 до 15, используя any.
# list1 = [16, 20, 19]
# check = any(elem in range(5, 16) for elem in list1)
# print(check)

# Проверить, все ли элементы с одинаковыми индексами из двух списков равны между собой.
# list1 = [10, 15, 20, 25]
# list2 = [10, 15, 20, 25]
# check = all(elem == element for elem, element in zip(list1, list2))
# print(check)

# Создать список, состоящий из строк, где каждая строка содержит
# элементы с одинаковыми индексами из разных списков, объединенных через zip.
# list1 = ['we can', 'she can', 'he can']
# list2 = [10, 15, 20, 25]
# resalt_union = list(zip(list1, list2))
# print(resalt_union)

# Найти максимальное значение среди сумм пар элементов с одинаковыми индексами из двух списков, объединенных через zip.
# list1 = [5, 15, 20, 25]
# list2 = [10, 15, 20, 25]

# Проверить, все ли числа в списке принадлежат к простым числам, используя all.
# list1 = [7, 2]
# def is_prime(number: int):
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
# check = all(is_prime(elem) for elem in list1)
# print(check) #жесть просто с этими простыми числами

# Проверить, все ли элементы вложенных списков положительны, используя all.
# list_some = [
#     [1, 2, 3],
#     [4, 5, -6],
#     [7, 8, 9]]
# check = all(all(elem > 0 for elem in element) for element in list_some)
# print(check)

# Проверить, все ли элементы в списке являются степенями двойки, используя all.
# def is_power_of_two(number: int):
#     return number > 0 and (number & (number - 1)) == 0
# list1 = [8, 2, 16]
# check = all(is_power_of_two(elem) for elem in list1)
# print(check)

# Проверить, есть ли хотя бы один элемент в списке, являющийся степенью двойки, используя any.
# def check_stepen_2(elem: int):
#     return elem > 0 and (elem & (elem - 1)) == 0
# list1 = [8, 2, 16, 22]
# check = any(check_stepen_2(elem) for elem in list1)
# print(check)

# Проверить, есть ли хотя бы одна строка в списке, содержащая хотя бы одну цифру, используя any.
# list1 = ['16', '14', 'abc', 'abc111']
# check = any(any(element.isdigit() for element in elem) for elem in list1) # ну тут не очень
# print(check)

