import re

email_pattern = re.compile(r'([a-zA-z0-9]+)@([a-zA-z0-9]+\.[a-z]+)')


def email_parse(email):
    user_address = email_pattern.findall(email)
    user_address_dict = {}

    if user_address:
        user, address = user_address[0]

        user_address_dict.setdefault('username', user)
        user_address_dict.setdefault('domain', address)
    else:
        raise ValueError(f'Wrong email: {email}')

    return user_address_dict


print(email_parse('vlwasd@yandex.ru'))
print(email_parse('someone@geekbrains.ru'))
