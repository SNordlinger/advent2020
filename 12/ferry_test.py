import ferry


def test_part1_example():
    instructions = ferry.get_input('example_input.txt')
    boat = ferry.Ferry()
    boat.follow_route(instructions)
    assert abs(boat.x) + abs(boat.y) == 25
