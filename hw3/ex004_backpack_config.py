"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
"""
from itertools import chain, combinations
from typing import List, Dict


def powerset(iterable: range) -> chain:
    """
    Function is used to generate all possible subsets of a given iterable.
    :param iterable: given iterable.
    :return: different combinations of items that could be placed in the backpack.
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def find_backpack_configurations(
        items: List[str],
        weights: List[int],
        max_capacity: int
) -> List[Dict[str, int]]:
    """
    Find all valid configurations of a backpack.
    :param items: items to put in the backpack.
    :param weights: weights of the items.
    :param max_capacity: maximum capacity of the backpack.
    :return: all configurations of the backpack.
    """
    valid_configs: List[Dict[str, int]] = []

    for subset in powerset(iterable=range(len(items))):
        total_weight = sum(weights[i] for i in subset)
        if total_weight <= max_capacity:
            valid_configs.append({items[i]: weights[i] for i in subset})

    return valid_configs


ITEMS: List[str] = ["Water", "Shovel", "Backpack", "Map", "Nails"]
WEIGHTS: List[int] = [1, 2, 3, 1, 2]
MAX_CAPACITY = 5

valid_configurations = find_backpack_configurations(
    items=ITEMS,
    weights=WEIGHTS,
    max_capacity=MAX_CAPACITY
)

for config in valid_configurations:
    print(config)
