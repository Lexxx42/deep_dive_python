"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def make_dict(**kwargs: int | str | bool) -> dict[str, str]:
    """ Create dictionary from keywords. """
    return {str(value): key for key, value in kwargs.items()}


print(make_dict(vasya=23, is_cool=False, boolean=True))
