"""
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
- имя файла без расширения или название каталога;
- расширение, если это файл;
- флаг каталога;
- название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""
import os
import logging
import argparse
from collections import namedtuple

DataEntry = namedtuple('DataEntry', ['type', 'path', 'size'])

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('crawler.log'),
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger(__name__)


def traverse_directory(directory_path: str) -> list[DataEntry]:
    """
    Collect data about a directory.
    :param directory_path: path to the directory (absolute or relative).
    :return: collected data.
    """
    data: list[DataEntry] = []

    for root, dirs, files in os.walk(directory_path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size = sum(
                os.path.getsize(os.path.join(dir_path, filename)) for filename in
                os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, filename))
            )
            data.append(DataEntry('directory', os.path.relpath(dir_path, directory_path), dir_size))

        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            data.append(DataEntry('file', os.path.relpath(file_path, directory_path), file_size))

    return data


def directory_crawler(directory_path: str, output_file_prefix: str) -> None:
    """
    Function to collect and log data.
    :param directory_path: path to the directory (absolute or relative).
    :param output_file_prefix: file prefix for output data.
    """
    data = traverse_directory(directory_path)

    for entry in data:
        logger.info(f'Type: {entry.type}, Path: {entry.path}, Size: {entry.size}')

    logger.info(
        f'Directory crawling completed for {directory_path}. '
        f'Output files with prefix {output_file_prefix} generated.'
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl a directory and log data.")
    parser.add_argument("directory_path", help="Path to the directory to crawl")
    parser.add_argument("output_file_prefix", help="File prefix for output data")
    args = parser.parse_args()

    directory_crawler(directory_path=args.directory_path, output_file_prefix=args.output_file_prefix)

# python logging_task.py test_dir output_prefix
