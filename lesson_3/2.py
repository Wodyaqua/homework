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


def num_translate_adv(eng):
    if eng[0].isupper():
        return num_translate_dict.get(eng.lower()).capitalize()
    else:
        return num_translate_dict.get(eng)


num_eng = input('num_eng: ')
print(num_translate_adv(num_eng))
