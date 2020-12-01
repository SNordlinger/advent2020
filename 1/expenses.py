import math


def parse_input():
    with open('input.txt') as infile:
        lines = infile.readlines()
    return [int(line) for line in lines]


def find_sum(expenses, target_sum):
    expense_set = set(expenses)
    for expense in expense_set:
        matching = target_sum - expense
        if matching in expense_set:
            return [expense, matching]

    return None


def find_triple_sum(expenses, target_sum):
    for num in expenses:
        remainder = 2020 - num
        vals = find_sum(expenses, remainder)
        if vals is not None:
            vals.append(num)
            return vals


def main():
    expenses = parse_input()
    sum_expenses = find_sum(expenses, 2020)
    print(f'Part 1 expenses: {sum_expenses}')
    print(f'Part 1 multiplied: {math.prod(sum_expenses)}')

    triple_expenses = find_triple_sum(expenses, 2020)
    print(f'Part 2 expenses: {triple_expenses}')
    print(f'Part 2 multiplied: {math.prod(triple_expenses)}')


if __name__ == '__main__':
    main()
