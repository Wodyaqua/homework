price_list = [9.12, 99.95, 77.6, 72.3, 33.5, 92, 86.23, 59.9, 17.2, 45, 53.65, 79.9, 74, 26.25, 95, 19]
new_price = []

# A

for i in price_list:
    rub = int(i)
    kk = round((i - rub) * 100)
    new_price.append(f'{rub:02d} руб {kk:02d} коп')

print(', '.join(new_price), '\n')

# B

id_before = id(new_price)
print(', '.join(sorted(new_price, reverse=True)))
id_after = id(new_price)
print('id before = id after : ', id_before == id_after, '\n')

# C

new_price_2 = sorted(new_price[:])
print(', '.join(new_price_2), '\n')

# print(', '.join(sorted(new_price)))

# D

top_5 = sorted(new_price, reverse=True)[:5]
print('Топ 5 самых дорогих товаров:')
print(', '.join(top_5))
