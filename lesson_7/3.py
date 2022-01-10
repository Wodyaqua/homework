import os
import shutil

main_path = os.getcwd()

files = [os.path.relpath(os.path.join(root, file), main_path)
         for root, _, files in os.walk(main_path) for file in files if file.endswith(".html")]

for rel_path in files:
    path, file = os.path.split(rel_path)
    test_path = os.path.join(main_path, "template", path)

    if not os.path.exists(test_path):
        os.makedirs(test_path)

    shutil.copyfile(os.path.join(main_path, rel_path), os.path.join(test_path, file))
