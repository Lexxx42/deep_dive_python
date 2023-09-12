"""
Напишите следующие функции:
1. нахождение корней квадратного уравнения;
2. генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк;
3. декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла;
4. декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""

import math
import csv
import random
import json


def quadratic_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # Check if the discriminant is non-negative
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    else:
        # No real roots
        return None


def generate_random_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(100):
            row = [random.random() for _ in range(3)]
            writer.writerow(row)


def calculate_roots_for_csv(func):
    def wrapper(csv_filename):
        with open(csv_filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                a, b, c = map(float, row)
                roots = func(a, b, c)
                print(f"For coefficients {a}, {b}, {c}, roots are: {roots}")

    return wrapper


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                'parameters': args,
                'result': result
            }
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            return result

        return wrapper

    return decorator


# 1. Calculate roots of a quadratic equation
roots = quadratic_roots(1, -3, 2)
print("Quadratic Equation Roots:", roots)

# 2. Generate a CSV file with random numbers
generate_random_csv('random_numbers.csv')


# 3. Decorator to calculate roots for CSV data
@calculate_roots_for_csv
def roots_from_csv(a, b, c):
    return quadratic_roots(a, b, c)


roots_from_csv('random_numbers.csv')


# 4. Decorator to save parameters and results to JSON
@save_to_json('results.json')
def example_function(x, y):
    return x + y


result = example_function(5, 3)
