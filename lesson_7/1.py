import os

main_dir = 'my_project'
dir_1 = 'settings'
dir_2 = 'mainapp'
dir_3 = 'adminapp'
dir_4 = 'authapp'

if os.path.exists(main_dir) is False:
    os.mkdir(main_dir)

os.chdir(main_dir)

if os.path.exists(dir_1) is False:
    os.mkdir(dir_1)
if os.path.exists(dir_2) is False:
    os.mkdir(dir_2)
if os.path.exists(dir_3) is False:
    os.mkdir(dir_3)
if os.path.exists(dir_4) is False:
    os.mkdir(dir_4)
