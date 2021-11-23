import string
import locale

str_list = []
uni_list = []
SITE_UNI_LIST = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
            '\u0441\u043e\u043a\u0435\u0442',
            '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for number in range(3):
    user_word = input(f'введите {number+1} слово: ')
    str_list.append(user_word)
    uni_list.append(user_word.encode('unicode_escape'))

"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных."""


def print_value_and_type(items: list):
    for item in items:
        print(f'вы ввели: {item}  введенный тип: {type(item)}')
    print("-" * 30)


print_value_and_type(str_list)
print_value_and_type(uni_list)
print_value_and_type(SITE_UNI_LIST)
