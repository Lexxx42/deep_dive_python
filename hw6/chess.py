"""
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""
import random


def is_attack(x1, y1, x2, y2):
    # Check if two queens attack each other
    return (
            x1 == x2 or  # Same row
            y1 == y2 or  # Same column
            abs(x1 - x2) == abs(y1 - y2)  # Same diagonal
    )


def queens_attack(arrangement):
    for i in range(len(arrangement)):
        for j in range(i + 1, len(arrangement)):
            x1, y1 = arrangement[i]
            x2, y2 = arrangement[j]
            if is_attack(x1, y1, x2, y2):
                return False  # Two queens attack each other
    return True  # No queens attack each other


# # Input the positions of 8 queens as pairs of numbers
# queens_positions = []
# for _ in range(8):
#     x, y = map(int, input().split())
#     queens_positions.append((x, y))
#
# result = queens_attack(queens_positions)
# print(result)

# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

def random_queens_arrangement():
    while True:
        queens_positions = [(i, random.randint(1, 8)) for i in range(1, 9)]
        if queens_attack(queens_positions):
            continue  # Queens attack each other, generate a new arrangement
        return queens_positions


def test_random_arrangements(num_tests=4):
    successful_arrangements = []
    for _ in range(num_tests):
        arrangement = random_queens_arrangement()
        successful_arrangements.append(arrangement)
    return successful_arrangements


def print_chessboard(arrangement):
    for i in range(1, 9):
        row = ['Q' if (i, j) in arrangement else '.' for j in range(1, 9)]
        print(' '.join(row))


# Test and print 4 successful arrangements
successful_arrangements = test_random_arrangements()
for i, arrangement in enumerate(successful_arrangements, 1):
    print(f"Successful Arrangement {i}:")
    print_chessboard(arrangement)
    print()
