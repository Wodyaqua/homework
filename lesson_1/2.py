my_list = []
sum_digits = 0
sum_digits17 = 0

for i in range(1, 1000, 2):
    num = i ** 3
    my_list.append(num)

    res = 0
    for dig in str(num):
        res += int(dig)
    if res % 7 == 0:
        sum_digits += num

for i in range(1, 1000, 2):
    num = i ** 3 + 17
    my_list.append(num)

    res = 0
    for dig in str(num):
        res += int(dig)
    if res % 7 == 0:
        sum_digits17 += num

print(f'Кратны 7:  {sum_digits}')
print(f'+17 кратны 7:  {sum_digits17}')
