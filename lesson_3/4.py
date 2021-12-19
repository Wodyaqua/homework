def thesaurus_adv(*names_surnames):
    dict_names_surnames = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        dict_names_surnames.setdefault(surname[0], {})
        dict_names_surnames[surname[0]].setdefault(name[0], [])
        dict_names_surnames[surname[0]][name[0]].append(name_surname)
    return dict_names_surnames


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
