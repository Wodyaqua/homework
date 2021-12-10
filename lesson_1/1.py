duration = int(input('Введите кол-во секунд: '))
days = duration // 86400
duration %= 86400
hours = duration // 3600
duration %= 3600
minutes = duration // 60
duration %= 60

if days != 0:
    print(f'{days} days, {hours} hours, {minutes} minutes, {duration} seconds')
elif hours != 0:
    print(f'{hours} hours, {minutes} minutes, {duration} seconds')
elif minutes != 0:
    print(f'{minutes} minutes, {duration} seconds')
elif duration >= 0:
    print(f'{duration} seconds')
