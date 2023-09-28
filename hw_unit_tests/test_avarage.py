""" Tests of average method. """
import allure
import pytest
from allure import step

from list_average import NumberList

get_average_runs = [
    (
        NumberList([10, 15, 20, 25]),
        NumberList([5, 10, 15, 20, 25]),
        'The first list has a larger average'
    ),
    (
        NumberList([1, 2, 3]),
        NumberList([4.1, 5.2, 6.3]),
        'The second list has a higher average'
    ),
    (
        NumberList([1, 2, 3]),
        NumberList([1, 2, 3]),
        'The average values are equal'
    ),
    (
        NumberList([]),
        NumberList([]),
        TypeError
    ),
    (
        NumberList([1, 2, 3]),
        NumberList([4, 5, 'six']),
        ValueError
    ),
    (
        NumberList([1, 2, 3]),
        NumberList([4, 5, None]),
        ValueError
    )
]


@allure.story('Test of average function')
@pytest.mark.parametrize('list1, list2, expected_result', get_average_runs)
def test_compare_averages(
        list1: NumberList,
        list2: NumberList,
        expected_result: str | TypeError | ValueError
):
    """ Test average method.
    :param list1: first NumberList to compare.
    :param list2: second NumberList to compare.
    :param expected_result: expected comparison result.
    """
    with step(title=f'Test averages with {list1=}, {list2=}, {expected_result}'):
        if isinstance(expected_result, str):
            result = list1.compare_averages(list2)
            assert result == expected_result
        else:
            with pytest.raises(expected_result):
                list1.compare_averages(list2)
