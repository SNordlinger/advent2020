import emulator


def test_part1_example():
    program = emulator.get_input('example_input.txt')
    assert emulator.find_acc_at_loop(program) == 5


def test_part2_example():
    program = emulator.get_input('example_input.txt')
    assert emulator.find_acc_at_termination(program) == 8
