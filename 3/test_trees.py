import trees
import math


def test_count_trees():
    grid = trees.parse_input('example_input.txt')
    assert trees.count_trees(grid, 3, 1) == 7


def test_all_slopes():
    grid = trees.parse_input('example_input.txt')
    tree_counts = trees.all_slopes_trees(grid)
    assert math.prod(tree_counts) == 336
