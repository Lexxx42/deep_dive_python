"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""
import collections
from typing import List, Union


def get_dupes(list_duplicates: List[Union[str, int]]) -> List[Union[str, int]]:
    """ Get a list of duplicates from a list of duplicates.
    :param list_duplicates: list of duplicates in it.
    :return: list of duplicates.
    """
    return [item for item, count in collections.Counter(list_duplicates).items() if count > 1]


list_with_duplicates: list[str] = ['a', 'b', 'c', 'd', 'e', 'e', 'a']
another_list_with_duplicates: list[int] = [1, 2, 2, 1, 0, 0, -1]

print(get_dupes(list_duplicates=list_with_duplicates))
print(get_dupes(list_duplicates=another_list_with_duplicates))
