"""3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""

WORD_1 = 'attribute'
WORD_2 = 'класс'
WORD_3 = 'функция'
WORD_4 = 'type'

WORDS_LIST = [WORD_1, WORD_2, WORD_3, WORD_4]

for item in WORDS_LIST:
    if item.isascii():
        print(f'возможно записать в байтовом типе: {item}')
    else:
        print(f'не возможно записать в байтовом типе: {item}')
    print("*" * 30)
