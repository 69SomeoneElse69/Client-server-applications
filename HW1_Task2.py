"""2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных."""


WORD_1 = 'class'
WORD_2 = 'function'
WORD_3 = 'method'

WORDS_LIST = [WORD_1, WORD_2, WORD_3]

for item in WORDS_LIST:
    get_value = eval(f"b'{item}'")
    print("value: ", get_value, "\ntype:", type(get_value), "\nbytes lenght: ", len(get_value), "\n**********")
