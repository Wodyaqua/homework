num_translate_dict = {'zero': 'ноль',
                      'one': 'один',
                      'two': 'два',
                      'three': 'три',
                      'four': 'четыре',
                      'five': 'пять',
                      'six': 'шесть',
                      'seven': 'семь',
                      'eight': 'восемь',
                      'nine': 'девять',
                      'ten': 'десять'}


def num_translate(num_eng):
    return num_translate_dict.get(num_eng)


print(num_translate(input('num_eng: ')))
