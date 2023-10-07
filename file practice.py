# 1. Создать текстовый файл и записать в него строку "Hello, World!".
# 2. Открыть файл из предыдущей задачи, прочитать его содержимое и вывести на экран.
# text = "Hello, World!"
# def create_some_file(my_text, path):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             my_file.write(my_text)
#     except FileNotFoundError as error:
#         print(error)
#
# def read_some_file(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:  # Исправил 'path' на path
#             content = my_file.read()
#             return content
#     except FileNotFoundError as er:
#         print(er)
#
# path = 'text_to_write.txt'
#
# # Вызываем функцию для создания файла
# create_some_file(text, path)
# # Вызываем функцию для чтения файла
# content = read_some_file(path)
# # Печатаем содержимое файла
# print(content)

# 3. Создать файл, в котором каждая строка содержит число от 1 до 10, каждое число на новой строке.
# text_to_write = [elem for elem in range(1, 11)]
# def write_file(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             for elem in data:
#                 my_file.write(f'{elem} \n')
#     except FileNotFoundError as ex:
#         print(ex)
# write_file('pr.txt', text_to_write)

# 4. Прочитать файл из предыдущей задачи, преобразовать строки в числа и вычислить их сумму.
# def read_summa(path):
#     summa = 0
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             for element in my_file:
#                 elem = int(line.strip())  # Преобразуем строку в число
#                 summa += elem
#         return summa
#     except FileNotFoundError as ex:
#         print(ex)
# res = read_summa('pr.txt')
# print(res)

# 5. Создать файл, содержащий список слов, каждое слово на новой строке. Прочитать файл, отсортировать слова и записать их обратно.
# import itertools
# letters = 'abcABC'
# words = [''.join(word) for word in itertools.permutations(letters, 3)]
# print(words)
# def write_file(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             for elem in data:
#                 sorted_elem = ''.join(sorted(elem))  # Сортировка элемента
#                 my_file.write(f'{sorted_elem}\n')  # Запись элемента с переводом строки
#     except FileNotFoundError as error:
#         print(error)
#
# def read_file(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             my_file.readline()
#     except FileNotFoundError as ex:
#         print(ex)
# write_file('sorted_words', words)
# read_file('sorted_words')

# 6. Найти самое длинное слово в файле с предыдущей задачи.
# words = ['maman', 'nanani', 'o']
# def write_file(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             for elem in data:
#                 sorted_elem = ''.join(sorted(elem))  # Сортировка элемента
#                 my_file.write(f'{sorted_elem}\n')  # Запись элемента с переводом строки
#     except FileNotFoundError as error:
#         print(error)
#
# def read_file(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             max_len = float('-inf')
#             el = ''
#             for elem in my_file:
#                 if len(elem) > max_len:
#                     max_len = len(elem)
#                     el = elem.strip()
#         return max_len, el
#     except FileNotFoundError as ex:
#         print(ex)
#
#
# write_file('sorted_words.txt', words)
# max_len, longest_word = read_file('sorted_words.txt')
# print(f'Самое длинное слово: "{longest_word}", его длина: {max_len}')

# 7. Создать файл с данными о продуктах в формате "название:цена". Прочитать файл, вычислить среднюю цену продукта и вывести на экран.
# import pickle
# products = {
#     "Яблоки": 2.5,
#     "Молоко": 1.0,
#     "Хлеб": 0.8,
#     "Яйца": 1.2,
#     "Мясо": 5.0
# }
# def write_file(path, data):
#     try:
#         with open(path, 'wb') as my_file:
#             pickle.dump(data, my_file)
#     except FileNotFoundError as er:
#         print(er)
#
# def read_aver(path):
#     aver = 0
#     try:
#         with open(path, 'rb') as my_file:
#             content = pickle.load(my_file)
#             total_price = sum(content.values())
#             aver = total_price / len(content)
#         return aver
#     except FileNotFoundError as er:
#         print(er)
# write_file('products.bin', products)
# print(read_aver('products.bin'))

# 8. Создать файл с данными о студентах в формате "имя фамилия:средний балл". Прочитать файл, найти студента с максимальным и минимальным баллом.
# students = {
#     "Иван Петров": 4.5,
#     "Мария Иванова": 3.8,
#     "Алексей Сидоров": 4.2,
#     "Елена Кузнецова": 4.9,
#     "Павел Смирнов": 3.5
# }
# import pickle
# def write_file(path, data):
#     try:
#         with open(path, 'wb') as my_file:
#             pickle.dump(data, my_file)
#     except FileNotFoundError as ex:
#         print(ex)
#
# def read_max_min_grade(path):
#     max_grade_student = None
#     min_grade_student = None
#     min_grade = float('inf')
#     max_grade = float('-inf')
#     try:
#         with open(path, 'rb') as my_file:
#             content = pickle.load(my_file)
#             for student, grades in content.items():
#                 if grades < min_grade:
#                     min_grade = grades
#                     min_grade_student = student
#                 if grades > max_grade:
#                     max_grade = grades
#                     max_grade_student = student
#
#         return f'{min_grade} минимальная оценка , {max_grade} максимальная оценка,\n {max_grade_student} студент с максимальным баллом, \n{min_grade_student} студент с минимальным баллом'
#     except FileNotFoundError as ex:
#         print(ex)
# write_file('students.bin', students)
# resalt = read_max_min_grade('students.bin')
# print(resalt)