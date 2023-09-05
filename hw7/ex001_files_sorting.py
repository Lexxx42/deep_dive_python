"""
Задача с семинара:
✔Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔Каждая группа включает файлы с несколькими расширениями.
✔В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os
import shutil


def sort_files(directory_path):
    categories = {
        'videos': ('.mp4', '.mov', '.avi', '.mkv'),
        'images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp'),
        'text': ('.txt', '.pdf', '.doc', '.docx')
    }

    for category in categories:
        category_path = os.path.join(directory_path, category)
        os.makedirs(category_path, exist_ok=True)

    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    for file in files:
        file_extension = os.path.splitext(file)[1].lower()

        for category, extensions in categories.items():
            if file_extension in extensions:
                source_file_path = os.path.join(directory_path, file)
                destination_dir = os.path.join(directory_path, category)
                destination_file_path = os.path.join(destination_dir, file)

                shutil.move(source_file_path, destination_file_path)
                break


source_directory = 'files'
sort_files(source_directory)
