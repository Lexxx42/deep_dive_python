"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction
from math import gcd


def get_sum_mult_of_two_fractions(fraction1: str, fraction2: str) -> tuple[str, str]:
    """
    Get sum and multiplication of two fractions.
    :param fraction1: first fraction in a format "a/b". Where a, b is integers.
    :param fraction2: second fraction in a format "a/b". Where a, b is integers.
    :return: tuple of results. Where 1st element is a sum result, second - mult result.
    """
    a, b = map(int, fraction1.split('/'))
    c, d = map(int, fraction2.split('/'))

    div_sum = gcd(a * d + c * b, b * d)
    div_mult = gcd(a * c, b * d)

    return f"{int((a * d + c * b) / div_sum)}/{int(b * d / div_sum)}", \
        f"{int(a * c / div_mult)}/{int(b * d / div_mult)}"


results = get_sum_mult_of_two_fractions(fraction1='18/3', fraction2='3/7')

fraction_sum = Fraction('18/3') + Fraction('3/7')
fraction_mult = Fraction('18/3') * Fraction('3/7')

assert results[0] == str(fraction_sum)
assert results[1] == str(fraction_mult)
