"""
2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.

Требуется сравнить длину каждого отрезка-стороны с суммой двух других.

Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.

Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""


class Triangle:
    def __init__(self, a: int, b: int, c: int):
        """ Triangle figure.

        :param a: side of a triangle.
        :param b: side of a triangle.
        :param c: side of a triangle.
        """
        self.a = a
        self.b = b
        self.c = c

    def tell_about_type(self) -> str:
        """ Get the type of triangle.

        :return: type of triangle.
        """
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 'Triangle doesn\'t exist'

        elif self.a == self.b == self.c:
            return 'Equilateral triangle'

        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return 'Isosceles triangle'

        else:
            return 'Scalene triangle'


cool_triangle = Triangle(*(int(input()) for _ in range(3)))
print(cool_triangle.tell_about_type())
