import math
from expenses import find_sum, find_triple_sum


def test_part1_example():
    expenses = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]

    sum_expenses = find_sum(expenses, 2020)
    assert sum(sum_expenses) == 2020
    assert math.prod(sum_expenses) == 514579


def test_part2_example():
    expenses = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]

    expenses = find_triple_sum(expenses, 2020)
    assert len(expenses) == 3
    assert sum(expenses) == 2020
    assert math.prod(expenses) == 241861950
