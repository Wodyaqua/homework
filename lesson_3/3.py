def thesaurus(*names):
    dict_names = {}
    for name in names:
        dict_names.setdefault(name[0], [])
        dict_names[name[0]].append(name)
    return dict_names


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
