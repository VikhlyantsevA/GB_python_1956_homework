# Задание 1
'''
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

- Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
- как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
- можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
'''
import os
import json


def create_tree(path: str, folder_tree: list):
    """
    Создает в директории path вложенную структуру: папку dirname, подпапки folders, файлы files.
    @param path: абсолютный путь к папке.
    @param folder_tree: файловая структура директории.
    """
    dirname, folders, files = folder_tree
    path2folder = os.path.join(path, dirname)
    os.makedirs(path2folder, exist_ok=True)

    for file in files:
        path2file = os.path.join(path2folder, file)
        open(path2file, 'a').close()

    for sub_folder_tree in folders:
        create_tree(path2folder, sub_folder_tree)


def read_config(path2config, *args, **kwargs):
    with open(path2config, *args, **kwargs) as fr:
        project_tree = json.load(fr)
    return project_tree


if __name__ == '__main__':
    '''
    Работает с деревом проекта по аналогии с os.walk().
    Структура проекта project_tree задается в формате вложенных списков, каждый из которых имеет три элемента: 
    - название корневой директории, 
    - список вложенных папок, 
    - список вложенных файлов.
    '''
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path2config = os.path.join(base_dir, 'project_tree.json')
    project_tree = read_config(path2config, encoding='utf-8')
    create_tree(base_dir, project_tree)
