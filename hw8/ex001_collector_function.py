"""
Напишите функцию, которая получает на вход директорию
и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.

1. Для дочерних объектов указывайте родительскую директорию.
2. Для каждого объекта укажите файл это или директория.
3. Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import os
import json
import csv
import pickle


def traverse_directory(directory_path: str) -> list[dict[str, str | int | bytes]]:
    """
    Collect data about a directory.
    :param directory_path: path to the directory (absolute or relative).
    :return: collected data.
    """
    data: list[dict[str, str | int | bytes]] = []

    for root, dirs, files in os.walk(directory_path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size = sum(
                os.path.getsize(os.path.join(dir_path, filename)) for filename in
                os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, filename))
            )
            data.append({
                'type': 'directory',
                'path': os.path.relpath(dir_path, directory_path),
                'size': dir_size
            })

        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            data.append({
                'type': 'file',
                'path': os.path.relpath(file_path, directory_path),
                'size': file_size
            })

    return data


def save_to_json(data: list[dict[str, str | int | bytes]], output_file: str) -> None:
    """
    Save data to .json format.
    :param data: data to save.
    :param output_file: output filename.
    """
    with open(output_file + '.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


def save_to_csv(data: list[dict[str, str | int | bytes]], output_file: str) -> None:
    """
    Save data to .csv format.
    :param data: data to save.
    :param output_file: output filename.
    """
    with open(output_file + '.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['type', 'path', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)


def save_to_pickle(data: list[dict[str, str | int | bytes]], output_file: str) -> None:
    """
    Save data to .pickle format.
    :param data: data to save.
    :param output_file: output filename.
    """
    with open(output_file + '.pkl', 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


def directory_crawler(directory_path: str, output_file_prefix: str) -> None:
    """
    Function to save obtained data to files.
    :param directory_path: path to the directory (absolute or relative).
    :param output_file_prefix: file prefix for output data.
    """
    data = traverse_directory(directory_path)

    # Save data to JSON, CSV, and Pickle files
    save_to_json(data=data, output_file=output_file_prefix)
    save_to_csv(data=data, output_file=output_file_prefix)
    save_to_pickle(data=data, output_file=output_file_prefix)


DIRECTORY_PATH = 'test_dir'
OUTPUT_FILE_PREFIX = 'result'
directory_crawler(directory_path=DIRECTORY_PATH, output_file_prefix=OUTPUT_FILE_PREFIX)
