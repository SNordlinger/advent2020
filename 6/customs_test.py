import customs


def test_part1():
    forms = customs.get_input('example_input.txt')
    answer_list = (customs.answers_from_form(f) for f in forms)
    count = customs.count_any_affirmative(answer_list)
    assert count == 11


def test_part2():
    forms = customs.get_input('example_input.txt')
    answer_list = (customs.answers_from_form(f) for f in forms)
    count = customs.count_all_affirmative(answer_list)
    assert count == 6
