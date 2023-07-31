"""
3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.

Используйте правило для проверки:
“Число является простым, если делится нацело только на единицу и на себя”.

Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""
from typing import Union

ERROR_MESSAGE = 'Entered not valid number. Number must be integer, [0, 100000]'

def is_prime(number: int) -> bool:
    """
    Check if a number is a prime.

    :param number: number to check.
    :return: True if number is prime, False otherwise.
    """

    if number <= 1:
        return False

    for divider in range(2, number):

        if not number % divider:
            return False

    return True


def check_input() -> Union[int, str]:
    """ Check input to be positive and lower than 100k.

    :return: number entered or error message.
    """
    try:
        number = int(input('Please enter a number to check for prime: '))

    except ValueError:
        return ERROR_MESSAGE

    if 0 <= number <= 100000:
        return number

    else:
        return ERROR_MESSAGE

print(is_prime(number) if isinstance(number:=check_input(), int) else number)
