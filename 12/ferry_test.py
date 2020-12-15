import ferry_part1
import ferry_part2


def test_part1_example():
    instructions = ferry_part1.get_input('example_input.txt')
    boat = ferry_part1.Ferry()
    boat.follow_route(instructions)
    assert abs(boat.x) + abs(boat.y) == 25


def test_part2_example():
    instructions = ferry_part2.get_input('example_input.txt')
    boat = ferry_part2.Ferry()
    boat.follow_route(instructions)
    assert abs(boat.x) + abs(boat.y) == 286
