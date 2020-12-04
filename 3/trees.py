import math


def parse_line(line):
    return [c == '#' for c in line.strip()]


def parse_input(filename):
    with open(filename) as infile:
        lines = infile.readlines()
    return [parse_line(line) for line in lines]


def has_tree(grid, x, y):
    grid_x = x % len(grid[y])
    return grid[y][grid_x]


def count_trees(grid, x_step, y_step):
    x_pos = 0
    y_pos = 0
    tree_count = 0
    while (y_pos < len(grid)):
        if has_tree(grid, x_pos, y_pos):
            tree_count += 1
        x_pos += x_step
        y_pos += y_step

    return tree_count


def all_slopes_trees(grid):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return [count_trees(grid, s[0], s[1]) for s in slopes]


def main():
    grid = parse_input('input.txt')
    print(f'Part 1: {count_trees(grid, 3, 1)}')

    tree_counts = all_slopes_trees(grid)
    print(f'Part 2: {math.prod(tree_counts)}')


if __name__ == '__main__':
    main()
