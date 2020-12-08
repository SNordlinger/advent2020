from collections import namedtuple
from queue import Queue
import re

LINE_RE = re.compile(r'^(.+) bags contain(.+)\.$')
INNER_BAG_RE = re.compile(r'^ ([0-9]+) (.+) bags?$')

Contents = namedtuple('Contents', ['bag', 'quantity'])


class Bag:
    def __init__(self, color):
        self.color = color
        self.outer_bags = []
        self.inner_bags = []

    def add_outer_bag(self, parent):
        self.outer_bags.append(parent)

    def add_inner_bag(self, child, quantity):
        self.inner_bags.append(Contents(child, quantity))


def get_input(file_path):
    with open(file_path) as infile:
        lines = infile.readlines()
    return [line.strip() for line in lines]


def parse_bags(bag_rules):
    bags = {}

    for rule in bag_rules:
        line_matches = re.match(LINE_RE, rule)
        color = line_matches[1]
        inner_bags = line_matches[2]
        if color not in bags:
            bags[color] = Bag(color)
        bag = bags[color]

        if inner_bags == ' no other bags':
            continue

        for bag_info in inner_bags.split(','):
            inner_bag_matches = re.match(INNER_BAG_RE, bag_info)
            inner_quantity = int(inner_bag_matches[1])
            inner_color = inner_bag_matches[2]

            if inner_color not in bags:
                bags[inner_color] = Bag(inner_color)
            inner_bag = bags[inner_color]
            bag.add_inner_bag(inner_bag, inner_quantity)
            inner_bag.add_outer_bag(bag)

    return bags


def count_contains(target_bag):
    to_search = Queue()
    counted = set()
    to_search.put(target_bag)
    while not to_search.empty():
        bag = to_search.get()
        for outer in bag.outer_bags:
            if outer.color not in counted:
                counted.add(outer.color)
                to_search.put(outer)

    return len(counted)


def count_inside(target_bag):
    bag_count = 0
    for contents in target_bag.inner_bags:
        bag_count += contents.quantity
        bag_count += contents.quantity * count_inside(contents.bag)

    return bag_count


def main():
    rules = get_input('input.txt')
    bag_list = parse_bags(rules)
    shiny_gold = bag_list['shiny gold']
    print(f'Part 1: {count_contains(shiny_gold)}')
    print(f'Part 2: {count_inside(shiny_gold)}')


if __name__ == '__main__':
    main()
