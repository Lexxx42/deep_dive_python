"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж: путь, имя файла, расширение файла.
"""
from os import path


def get_file_path_name_extension(abs_path: str) -> tuple[str]:
    """
    Get path to a file, filename and file extension.
    :param abs_path: Absolute path to the file.
    :return: File path, filename and file extension.
    """
    filename, extension = abs_path.split('\\')[-1].split('.')
    return abs_path, filename, extension


print(get_file_path_name_extension(abs_path=path.abspath('ex001_file_tuple.py')))
