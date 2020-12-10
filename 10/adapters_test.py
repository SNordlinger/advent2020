import adapters


def test_part1_example():
    joltages = adapters.get_input('example_input.txt')
    differences = adapters.get_jolt_differences(joltages)

    assert differences[1] == 22
    assert differences[3] == 10


def test_part2_example():
    joltages = adapters.get_input('example_input.txt')
    arragements = adapters.count_arrangements(joltages)

    assert arragements == 19208
