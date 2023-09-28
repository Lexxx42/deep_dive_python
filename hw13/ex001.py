# Введите ваше решение ниже
class NegativeValueError(Exception):
    pass


class Rectangle:
    def __init__(self, width, height=0):
        if width < 0:
            raise NegativeValueError(f"Ширина должна быть положительной, а не {width}")
        if height < 0:
            raise NegativeValueError(f"Высота должна быть положительной, а не {height}")
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        if value < 0:
            raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")
        self._width = value

    @height.setter
    def height(self, value):
        if value < 0:
            raise NegativeValueError(f"Высота должна быть положительной, а не {value}")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)
