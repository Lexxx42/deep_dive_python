"""
Напишите функцию группового переименования файлов.
Она должна:

✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.

✔ принимать параметр количество цифр в порядковом номере.

✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.

✔ принимать параметр расширение конечного файла.

✔ принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.

3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""

import os


def batch_rename_files(source_dir, end_name, num_digits, source_extension, destination_extension, name_range):
    matching_files = [f for f in os.listdir(source_dir) if f.endswith(source_extension)]

    for i, filename in enumerate(matching_files, 1):
        name_part = filename[name_range[0] - 1:name_range[1]]
        new_name = f"{name_part}_{end_name}{str(i).zfill(num_digits)}.{destination_extension}"

        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(source_dir, new_name)

        os.rename(source_path, destination_path)


source_directory = 'files_to_rename'
desired_end_name = 'newname'
num_digits_in_ordinal = 3
source_file_extension = '.one'
destination_file_extension = 'doc'
name_range = (3, 6)

batch_rename_files(
    source_directory,
    desired_end_name,
    num_digits_in_ordinal,
    source_file_extension,
    destination_file_extension,
    name_range
)
