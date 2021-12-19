from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(amount):
    jokes = []
    for num in range(amount):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        jokes.append(f'{noun} {adverb} {adjective}')
    return jokes


print(get_jokes(int(input('Введите количество шуток: '))))
