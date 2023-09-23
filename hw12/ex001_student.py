"""
Создайте класс студента.

1. Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.

2. Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы.

3. Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).

4. Также экземпляр должен сообщать средний балл по тестам для каждого предмета
и по оценкам всех предметов вместе взятых.
"""

import csv


class NameValidator:
    """ Descriptor for name validation. """

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not value.replace(' ', '').isalpha() or not value[0].isupper():
            raise ValueError(
                'Name must start with a capital letter and contain only letters (including spaces).'
            )

        instance.__dict__[self.name] = value


class Subject:
    """ Descriptor for subject grades and test results. """

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not (2 <= value <= 5) and not (0 <= value <= 100):
            raise ValueError('Grades must be between 2 and 5, and test results between 0 and 100.')

        instance.__dict__[self.name] = value


# Student class
class Student:
    """ Student class. """
    name = NameValidator()

    def __init__(self, csv_file: str):
        self.item_names: list[str] = self.load_subject_names(csv_file=csv_file)
        self.grades: dict[str, int] = {}
        self.test_results: dict[str, dict[str, int]] = {}

    @staticmethod
    def load_subject_names(csv_file: str) -> list[str]:
        """ Load subject names from a csv file.

        :param csv_file: csv file name.
        """
        try:
            with open(csv_file, 'r', encoding='utf-8') as file1:
                reader = csv.reader(file1)
                item_names = next(reader)
                return item_names
        except FileNotFoundError:
            raise FileNotFoundError('CSV file not found.')
        except csv.Error:
            raise ValueError('Invalid CSV file format.')

    def add_grade(self, subject: str, grade: int) -> None:
        """ Add a grade info for a student.

        :param subject: student's subject name.
        :param grade: student's grade.
        """
        if subject not in self.item_names:
            raise ValueError(f"Invalid subject '{subject}'.")

        self.grades[subject] = grade

    def add_test_result(self, subject: str, result: dict[str, int]) -> None:
        """ Add info about tests for a student.

        :param subject: student's subject name.
        :param result: test results.
        """
        if subject not in self.item_names:
            raise ValueError(f'Invalid subject "{subject}:.')

        self.test_results[subject] = result

    def average_test_score(self, subject: str) -> float | None:
        """ Calculates the average test score.

        :param subject: student's subject name.
        """
        if subject not in self.test_results:
            return None

        return sum(self.test_results[subject].values()) / len(self.test_results[subject])

    def overall_average(self) -> float | None:
        """ Calculates the overall score. """
        if not self.test_results:
            return None

        total_score = 0
        total_count = 0
        for subject in self.item_names:

            if subject in self.test_results:
                subject_avg = self.average_test_score(subject)

                if subject_avg is not None:
                    total_score += subject_avg
                    total_count += 1

        return total_score / total_count if total_count > 0 else None


ITEM_NAMES_CSV_FILE = 'item_names.csv'
with open(ITEM_NAMES_CSV_FILE, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Math', 'Physics', 'Chemistry'])


student = Student(ITEM_NAMES_CSV_FILE)
student.name = 'Alexander Konyukhov'

student.add_grade('Math', 5)
student.add_grade('Physics', 5)
# student.add_grade('Chemistry1', 3)  # ValueError: Invalid subject 'Chemistry1'.
student.add_test_result('Math', {'Test1': 90, 'Test2': 85})
student.add_test_result('Physics', {'Test1': 80})


math_avg = student.average_test_score('Math')
physics_avg = student.average_test_score('Physics')
overall_avg = student.overall_average()


print(f'Math Average: {math_avg}')
print(f'Physics Average: {physics_avg}')
print(f'Overall Average: {overall_avg}')
