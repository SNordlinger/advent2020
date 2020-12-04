import passport


def test_part1_example():
    passports = passport.get_passport_data('example_inputs/part1.txt')
    assert passport.count_has_fields(passports) == 2


def test_part2_invalid():
    passports = passport.get_passport_data('example_inputs/invalid.txt')
    assert passport.count_valid(passports) == 0


def test_part2_valid():
    passports = passport.get_passport_data('example_inputs/valid.txt')
    assert passport.count_valid(passports) == 4
