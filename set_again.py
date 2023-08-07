# Сформируйте множество из символов строки, которые не являются цифрами.
# text = "abc123xyz456"
# set_out = {element for element in text if element.isnumeric()}
# print(set_out)

# Создайте множество из длин строк в списке ['яблоко', 'груша', 'апельсин', 'киви'].
# text = ['яблоко', 'груша', 'апельсин', 'киви']
# set_out = {len(element) for element in text}
# print(set_out)

# Найдите множество всех буквенных символов в строке "Hello, World!" без учета регистра.
# text = "Hello, World!"
# set_out = {element.lower() for element in text if element.isalpha()}
# print(set_out)

# Получите множество всех слов в строке
# text = "Эти задачи на set comprehension интересны"
# set_out = {element for element in text.split()}
# print(set_out)

# Создайте множество из букв строки "абракадабра", которые встречаются более одного раза.
# text = "абракадабра" #а,б,р
# count_letter = set(filter(lambda letter: text.count(letter) > 1, text))
# print(count_letter)

# Найдите множество всех делителей числа 42.
# def divisors(number: int):
#     list_out_divisors = [divisor for divisor in range(1, number + 1) if number % divisor == 0]
#     return list_out_divisors
# resalt = divisors(42)
# print(resalt)

# Сформируйте множество из длин слов в списке ['солнце', 'небо', 'облако', 'дождь'].
# text = ['солнце', 'небо', 'облако', 'дождь', '55']
# find_lenght = {len(element) for element in text}
# print(find_lenght)

# Создайте множество из символов строки "abcdefg", которые не являются гласными буквами.
# text = "abcdefg"
# set_out = {letter for letter in text if letter not in 'aeoui'}
# print(set_out)

# Получите множество всех слов в списке ['яблоко', 'груша', 'киви', 'груша'].
# text = ['яблоко', 'груша', 'киви', 'груша']
# set_out = {element for element in text}
# print(set_out)

# Создайте множество из цифр в строке "abc123xyz456".
# text = "abc123xyz456"
# list_out = {element for element in text if element.isnumeric()}
# print(list_out)

# Найдите множество всех букв в строке "Hello, World!" без повторений.
# text = "Hello, World!"
# set_out = {letter.lower() for letter in text if letter.isalpha()}
# print(set_out)

# Сформируйте множество из длин строк в списке ['apple', 'banana', 'cherry', 'date'].
# text = ['apple', 'banana', 'cherry', 'date']
# ser_out = {len(element) for element in text}
# print(ser_out)