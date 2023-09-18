"""
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства.
Задания должны решаться через вызов методов экземпляра.
"""


class HexConverter:
    """ HW 2.
    Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
    Функцию hex используйте для проверки своего результата.
    """
    def __init__(self, number: int):
        self.number = number

    def convert_to_hex(self) -> str:
        """
        Turns the stored number into a hex representation.
        :return: hex string representation.
        """
        return f'0x{self.number:0x}'


# Example usage:
converter = HexConverter(100500)
assert hex(100500) == converter.convert_to_hex(), \
    f'Expected "{hex(100500)}" to be equal to "{converter.convert_to_hex()}"'
