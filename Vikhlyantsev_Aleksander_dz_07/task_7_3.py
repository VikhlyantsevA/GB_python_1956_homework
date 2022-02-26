# Задание 3
'''
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html

> Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
> (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
> которая решена, например, во фреймворке django.
'''
import os
import shutil
from task_7_1 import read_config, create_tree


if __name__ == '__main__':
    # Создается структура файлов и папок как в задании 2
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path2config = os.path.join(base_dir, 'project_tree_2.json')
    project_tree = read_config(path2config, encoding='utf-8')
    create_tree(base_dir, project_tree)

    # Собирается папка с шаблонами
    project_folder = project_tree[0]
    project_dir = os.path.join(base_dir, project_folder)
    templates_folder = 'templates'
    if os.path.basename(project_dir) == templates_folder:
        raise OSError("Using of name 'templates' prohibited for project directory.")

    for dir_, folders, files in os.walk(project_dir):
        child_folder = os.path.basename(dir_)
        if child_folder == templates_folder:
            parent_folder = os.path.basename(os.path.dirname(dir_))
            if parent_folder == project_folder:
                continue

            path2copy = os.path.join(project_dir, templates_folder, parent_folder)
            shutil.copytree(dir_, path2copy, dirs_exist_ok=True)
