import os

with open('config.yaml') as f:
    config = f.readlines()

    for i in config:

        main_path = os.getcwd()

        if i[:3] == '|--':
            main_dir = i[3:].strip()
            if os.path.exists(main_dir) is False:
                os.mkdir(main_dir)

        elif i.count(' ') == 3:
            os.chdir(os.path.join(os.getcwd(), main_dir))
            name = i[6:].strip()

            if '.' in name:
                with open(name, 'w+'):
                    pass
            else:
                if os.path.exists(name) is False:
                    os.mkdir(name)

            os.chdir(main_path)

        elif i.count(' ') == 5:
            os.chdir(os.path.join(os.getcwd(), main_dir, name))
            name_2 = i[9:].strip()

            if '.' in name_2:
                with open(name_2, 'w+'):
                    pass
            else:
                if os.path.exists(name_2) is False:
                    os.mkdir(name_2)

            os.chdir(main_path)

        elif i.count(' ') == 8:
            os.chdir(os.path.join(os.getcwd(), main_dir, name, name_2))
            name_3 = i[12:].strip()

            if '.' in name_3:
                with open(name_3, 'w+'):
                    pass
            else:
                if os.path.exists(name_3) is False:
                    os.mkdir(name_3)

            os.chdir(main_path)

        elif i.count(' ') == 11:
            os.chdir(os.path.join(os.getcwd(), main_dir, name, name_2, name_3))
            name_4 = i[15:].strip()

            if '.' in name_4:
                with open(name_4, 'w+'):
                    pass
            else:
                if os.path.exists(name_4) is False:
                    os.mkdir(name_4)

            os.chdir(main_path)
