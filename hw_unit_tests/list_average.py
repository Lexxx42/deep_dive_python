""" Module containing a function that compares averages of two lists of numbers. """


class NumberList:
    """ Class for representing a list of numbers. """

    def __init__(self, numbers: list[int | float]):
        self.numbers = numbers

    def is_valid(self) -> bool:
        """ Checks if a list contains only numbers.

        :return: returns True if the list contains only numbers, False otherwise.
        """
        return all(isinstance(num, (int, float)) for num in self.numbers)

    def calculate_average(self) -> float | None:
        """ Calculates the average value of a list of numbers.

        :return: average value.
        """
        if not self.numbers:
            return None

        if not self.is_valid():
            raise ValueError('List contains non-numeric values')

        return sum(self.numbers) / len(self.numbers)

    def compare_averages(self, other_list) -> str:
        """ Compares averages of two lists numbers.

        :return: compare results.
        """
        if not isinstance(other_list, NumberList):
            raise ValueError('Input must be a NumberList object')

        if not self.is_valid() or not other_list.is_valid():
            raise ValueError('Input lists must contain only numeric values')

        average1 = self.calculate_average()
        average2 = other_list.calculate_average()

        if average1 > average2:
            return 'The first list has a larger average'

        if average1 < average2:
            return 'The second list has a higher average'

        return 'The average values are equal'
