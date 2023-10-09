# Filter:

# 1. Фильтрация чисел больше 10 из списка.
#import random
#list_numbers = list(random.randint(-5, 45) for _ in range(5))
# print(list_numbers)
# list_out = list(filter(lambda elem: elem > 10, list_numbers))
# print(list_out)

# 2. Фильтрация строк длиннее 5 символов.
# list1 = ["apple", "banana", "cherry", "date"]
# list_out = list(filter(lambda elem: len(elem) > 5, list1))
# print(list_out)

# 3. Выбор всех четных чисел из списка.
# list_out = list(filter(lambda elem: elem % 2 == 0, list_numbers))
# print(list_out)

# 4. Фильтрация отрицательных чисел.
# list_out = list(filter(lambda elem: elem < 0, list_numbers))
# print(list_out)

# 5. Отбор имён, начинающихся на определенную букву.
# list1 = ["apple", "banana", "cherry", "date"]
# letter = 'a'
# list_out = list(filter(lambda elem: str(elem).startswith(letter), list1))
# print(list_out)

# 6. Фильтрация положительных и нулевых значений.
# list_out = list(filter(lambda elem: elem <= 0, list_numbers))
# print(list_out)

# 7. Отбор слов, содержащих определенную подстроку.
# list1 = ["apple", "banana", "cherry", "date"]
# substr = 'ap'
# list_out = list(filter(lambda elem: substr in elem, list1))
# print(list_out)

# 8. Фильтрация чисел, делящихся на 3.
# list_out = list(filter(lambda elem: elem % 3 == 0, list_numbers))
# print(list_out)

# 9. Отбор элементов списка, превышающих среднее значение.
# aver = 0
# summa = 0
# for elem in list_numbers:
#     summa += elem
#     aver = summa / len(list_numbers)
#     list_out = list(filter(lambda elem: elem > aver, list_numbers))
# print(list_out, aver)

# 10. Отбор дат, находящихся в будущем.
# import datetime
# now_date = datetime.date.today()
# dates = ["2023-10-01", "2023-10-12", "2023-10-03", "2023-10-04", "2023-10-05"]
# # Преобразуем строки с датами в объекты datetime.date
# dates = [datetime.date.fromisoformat(date) for date in dates]
# # Отфильтруем даты, оставив только те, что находятся в будущем
# list_out = [date for date in dates if date > now_date]
# print(list_out)

# Sorted:
#
# 1. Сортировка списка чисел по возрастанию.
# import random
# list_numbers = random.sample(range(5, 45), random.randint(2, 14))
# print(list_numbers)
# list_out = sorted(list_numbers, key=lambda elem: elem)
# print(list_out)

# 2. Сортировка списка строк в алфавитном порядке.
# list1 = ["banana", "cherry", "date", "apple"]
# list_out = list(sorted(list1, key=lambda elem: elem))
# print(list_out)

# 3. Сортировка списка чисел по убыванию.
# list_out = list(sorted(list_numbers, key=lambda elem: elem, reverse=True))
# print(list_out)

# 4. Сортировка строк по длине.
# list1 = ["banana", "cherry", "date", "apple"]
# list_out = list(sorted(list1, key=lambda elem: len(elem)))
# print(list_out)

# 5. Сортировка списка кортежей по второму элементу.
# my_tuples = [(1, 'apple'), (2, 'banana'), (3, 'cherry'), (12, 'bananas')]
# list_out = list(sorted(my_tuples, key=lambda elem: elem[1]))
# print(list_out)

# 6. Сортировка списка словарей по значению определенного ключа.
# my_list = [
#     {'name': 'John Doe', 'age': 30, 'city': 'New York'},
#     {'name': 'Jane Smith', 'age': 25, 'city': 'Los Angeles'},
#     {'name': 'Bob Johnson', 'age': 35, 'city': 'Chicago'}
# ]
# list_out = list(sorted(my_list, key=lambda elem: elem['age']))
# print(list_out)

# # 7. Сортировка списка строк с учетом регистра.
# list1 = ["apple", "Banana", "cherry", "DaTe"]
# list_out = list(sorted(list1, key=lambda elem: elem))
# print(list_out)

# 8. Сортировка списка чисел по остатку от деления на 5.
# list_out = list(sorted(list_numbers, key=lambda elem: elem % 5))
# print(list_out)

# 9. Сортировка списка строк по количеству гласных букв.
# my_list = ['apple', 'banana', 'cherry', 'bananas']
# vowes = 'aeouiy'
# list_out = []
#
# for elem in my_list:
#     counter = 0
#     for letter in elem:
#         if letter in vowes:
#             counter += 1
#     list_out.append((counter, elem))
# list_out.sort()  # Сортируем список по количеству гласных
# sorted_elements = [elem for _, elem in list_out]
# print(sorted_elements)

# # 10. Сортировка списка дат по возрастанию.
# import datetime
# dates = ["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05"]
# new_date = []
# for date in dates:
#     new_date.append(datetime.datetime.fromisoformat(date))
# print(new_date)
# dates_out = sorted(new_date, key=lambda elem: elem)
# print(dates_out)