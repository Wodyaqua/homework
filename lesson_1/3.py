for num in range(1, 101):
    if num % 10 == 1 and num != 11:
        print(f'{num} процент')
    elif num <= 4:
        print(f'{num} процента')
    else:
        print(f'{num} процентов')
