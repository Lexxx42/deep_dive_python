"""
Создайте функцию генератор чисел Фибоначчи.
"""

from time import perf_counter_ns
# Давно написал вот такой вариант, лень переписывать

t = perf_counter_ns()


def fibonacci_of(n):
    if n in cache:  # base case
        return cache[n]
    # Compute and cache the fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # recursive case
    return cache[n]


cache = {0: 0, 1: 1}
fib = [fibonacci_of(n) for n in range(1500)]
print(fib)
print('last fib: ', fib[-1])
print('timer: ', perf_counter_ns() - t)
