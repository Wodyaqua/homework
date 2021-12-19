import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes_adv(amount, repeats=True):
    jokes = []
    if not repeats:
        if amount > min(len(nouns), len(adverbs), len(adjectives)):
            return 'No way'
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(amount):
                jokes.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    else:
        for num in range(amount):
            noun = random.choice(nouns)
            adverb = random.choice(adverbs)
            adjective = random.choice(adjectives)
            jokes.append(f'{noun} {adverb} {adjective}')
    return jokes


print(get_jokes_adv(6, True))
print(get_jokes_adv(5, False))
print(get_jokes_adv(6, False))
