for num in range(1, 101):
    if num % 10 == 1 and num != 11:
        print(f'{num} процент')
    if num % 10 == 2 or num % 10 == 3 or num % 10 == 4:
        print(f'{num} процента')
    if num % 10 == 5 or num % 10 == 6 or num % 10 == 7 or num % 10 == 8 or num % 10 == 9 or num % 10 == 0 or num == 11:
        print(f'{num} процентов')
