# 10. Создать файл, содержащий несколько абзацев текста. Подсчитать количество слов в каждом абзаце и записать результаты в другой файл.
text = """
    Природа великолепна и удивительна в своей красоте. 
Зеленые леса, пестрые цветами поля, могучие горы и тихие озера — все это создает неповторимую картину нашей планеты.
Каждый уголок природы обладает своей уникальной аурой и привлекает своей неповторимостью.

    Звуки природы - это настоящая симфония жизни. 
Щебет птиц, шум листвы под ногами, журчание ручья — все эти звуки успокаивают, приносят гармонию и внутренний покой.
В природе можно услышать настоящую музыку, которая звучит вечно.

    Природа обладает невероятной силой и мудростью.
В ней все устроено с особой точностью и гармонией.
Разнообразие видов растений и животных показывает нам великое разнообразие жизни на Земле.
Каждый организм, каждый элемент природы играет свою роль в общей карте жизни.

    Путешествия в природу - это возможность открыть для себя что-то новое и удивительное.
Каждая прогулка в лесу, по горам или у реки приносит новый опыт и воспоминания.
Природа дарит нам великое сокровище — возможность наслаждаться красотой и гармонией мира вокруг нас.
"""

# def write_text(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             my_file.write(data)
#     except FileNotFoundError as ex:
#         print(ex)
# def read_count(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             paragraphs = my_file.read().split('\n\n') #После чтения файла, полученная строка разбивается на подстроки
#             # с использованием разделителя, который мы указываем в скобках метода `split`.
#             # В данном случае разделителем является двойной перевод строки (`\n\n`).
#
#             word_counts = [len(paragraph.split()) for paragraph in paragraphs] #разделили слова по пробелам в каждом отдельном параграфе
#         return word_counts
#     except FileNotFoundError as ex:
#         print(ex)
# write_text('textik.txt', text)
# resalt = read_count('textik.txt')
# print(resalt)

# 11. Создать файл, содержащий числа через запятую. Прочитать файл, вычислить среднее значение чисел и записать его в другой файл.
# numbers_generator = '1, 2, 3, 4, 5'
#
# def write_file(path, data):
#     try:
#         with open(path, 'w') as my_file:
#             my_file.write(data)
#     except FileNotFoundError as ex:
#         print(ex)
# def read_aver(path):
#     aver = 0
#     summa = 0
#     counter = len(numbers_generator)
#     try:
#         with open(path, 'r') as my_file:
#             content = my_file.readline()
#             for elem in content.split(','):
#                 elem = int(elem)
#                 summa += elem
#                 aver = summa / counter
#         return aver
#     except FileNotFoundError as ex:
#         print(ex)
# write_file('num_str.txt', numbers_generator)
# resalt = read_aver('num_str.txt')
# print(resalt)

# 12. Создать файл, содержащий данные о сотрудниках в формате "имя фамилия, возраст, должность".
# Прочитать файл, вывести средний возраст сотрудников каждой должности.
# import pickle
# def write_file(path, data):
#     try:
#         with open(path, 'wb') as my_file:
#             pickle.dump(data, my_file)
#     except FileNotFoundError as er:
#         print(er)
#
# def read_aver_age(path):
#     try:
#         with open(path, 'rb') as my_file:
#             content = pickle.load(my_file)
#             avg_age_by_position = {}
#
#             for employee in content:
#                 _, age, position = employee.split(", ")
#                 age = int(age)
#
#                 if position in avg_age_by_position:
#                     avg_age_by_position[position][0] += age
#                     avg_age_by_position[position][1] += 1
#                 else:
#                     avg_age_by_position[position] = [age, 1]
#
#             for position, (total_age, num_employees) in avg_age_by_position.items():
#                 avg_age = total_age / num_employees
#                 print(f"Должность: {position}, Средний возраст: {avg_age}")
#
#     except FileNotFoundError as er:
#         print(er)
#
# employees_data = [
#     "Иван Иванов, 30, Менеджер",
#     "Петр Петров, 35, Разработчик",
#     "Мария Сидорова, 28, Аналитик",
#     "Ольга Николаева, 40, Менеджер",
#     "Алексей Кузнецов, 32, Разработчик",
#     "Екатерина Иванова, 27, Аналитик",
#     "Владимир Смирнов, 45, Директор",
# ]
# write_file('emp.bin', employees_data)
# read_aver_age('emp.bin')
