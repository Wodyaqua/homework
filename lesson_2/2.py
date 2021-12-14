my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
right_list = []

for i in my_list:
    if i.isdigit():
        right_list.append(f'"{int(i):02d}"')
    elif i[0] == '+':
        right_list.append(f'"+{int(i):02d}"')
    else:
        right_list.append(i)

print(' '.join(right_list))
