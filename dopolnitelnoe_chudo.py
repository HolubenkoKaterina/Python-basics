# Создайте список из квадратов чисел от 1 до 10.
# list_out = [num ** num for num in range(1, 11)]
# print(list_out)

# Переведите список строк в верхний регистр.
# some_list = ['i like python']
# def up_words(some_list: list):
#     list_out = [elem.upper() for elem in some_list]
#     return list_out
# resalt = up_words(some_list)
# print(resalt)

# Отфильтруйте только четные числа из списка.
# numbers = [elem for elem in range(1, 15) if elem % 2 == 0]
# print(numbers)

# numb = list(range(1, 15))
# list_out = list(filter(lambda elem: elem % 2 == 0, numb))
# print(list_out)

# Создайте список из первых букв каждого слова в строке.
# text = 'i work hard'
# list_out = [letter[0] for letter in text.split()]
# print(list_out)

# Удалите из списка все числа, меньшие 5.
# list_out = [elem for elem in range(1, 25) if elem > 5]
# print(list_out)

# Возведите каждое число в списке в куб.
# print([elem ** 3 for elem in range(1, 10)])

# Отфильтруйте только строки, содержащие букву "a".
# text = ['heelo', 'world', 'we we', 'ok we']
# letter = 'o'
# resalt = list(filter(lambda elem: letter in elem, text))
# print(resalt)

# Создайте список из длин строк в другом списке.
# spisok = ['hello world', 'learn python', 'can', 'do']
# list_out_lenght = [len(elem) for elem in spisok]
# print(list_out_lenght)

# Удалите из списка все элементы с отрицательными значениями.
# list_out = [elem  for elem in range(-40, 30) if elem > 0]
# print(list_out)

# Переведите список чисел в список строк.
# Отфильтруйте только элементы, являющиеся положительными числами.
# list_out = list(filter(lambda elem: elem > 0, range(-5, 15)))
# print(list_out)

# Создайте список из символов на нечетных позициях строки.
# some_text = 'we can do everything!'
# list_out = [elem for elem in some_text[1::2]]
# print(list_out)

# Удалите из списка все пробелы в строках.
# some_text = 'we can do everything!'
# list_out = [''.join(elem.split()) for elem in [some_text]]# неожиданно
# print(list_out)

# Отфильтруйте только числа, делящиеся на 3 без остатка.
# list_out = list(filter(lambda elem: elem % 3 == 0, range(-15, 15)))
# print(list_out)

# Создайте список, содержащий только уникальные элементы из исходного списка.
# some_text = ['lili', 'lili', 55, [5, 4], [5, 4]]
# unique_elements = []
# list_out_uniq = [elem for elem in some_text if elem not in unique_elements and (unique_elements.append(elem) or True)]
# print(list_out_uniq)
# вот это пока что слишком)

# Отсортируйте строки в списке по их длине.
# some_text = ['what are you doing?', 'hello', 'i learn my task']
# lenght_strings = sorted(some_text, key=lambda elem: len(elem), reverse=True)
# print(lenght_strings)

# Преобразуйте список списков в плоский список.
# some_spisok = [[2, 6, 8], [36, 25, 14], [5, 15, 25]]
# list_out = [el for element in some_spisok for el in element]
# print(list_out)

# Отфильтруйте только элементы, состоящие из буквенных символов.
# some_spisok = ['abba', 54, '48', [64, 'lisa'], (5, ), {28, 64}, {'mikka', 'uy'}]
# resalt = list(filter(lambda element: type(element) == str and element.isalpha(), some_spisok))
# print(resalt)

# Создайте список из квадратов четных чисел от 1 до 20.
# resalt = [elem ** 2 for elem in range(-10, 10)]
# print(resalt)

# Отфильтруйте только элементы, которые начинаются с гласной буквы.
# some_list = ['kiki', 'ikki', 'uppi', 'lala']
# resalt = list(filter(lambda elem: elem[0] in 'ui', some_list))
# print(resalt)
