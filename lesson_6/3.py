from itertools import zip_longest
import json

users_hobby = {}

with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        amount_users = sum(1 for line in users)
        amount_hobby = sum(1 for line in hobby)
        if amount_hobby > amount_users:
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for user, user_hobby in zip_longest(users, hobby):
            users_hobby[user.replace(',', ' ').strip()] = user_hobby.strip() if user_hobby is not None else user_hobby

with open('users_hobby.json', 'w', encoding='utf-8') as f:
    json.dump(users_hobby, f, ensure_ascii=False)
print(users_hobby)
