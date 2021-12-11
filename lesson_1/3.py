for num in range(1, 101):
    if num % 10 == 1 and num != 11:
        print(f'{num} процент')
    elif num <= 4 or num % 10 == 2 and num != 12 or num % 10 == 3 and num != 13 or num % 10 == 4 and num != 14:
        print(f'{num} процента')
    else:
        print(f'{num} процентов')
