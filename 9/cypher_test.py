import cypher


def test_part1_example():
    data = cypher.get_input('example_input.txt')
    preamble = data[:5]
    numbers = data[5:]
    assert cypher.find_invlid_num(preamble, numbers) == 127


def test_parts_example():
    data = cypher.get_input('example_input.txt')
    contiguous_nums = cypher.find_contiguous_sum(data, 127)
    assert contiguous_nums == [15, 25, 47, 40]
