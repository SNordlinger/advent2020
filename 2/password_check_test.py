from password_check import PassInfo, parse_pass_info


def test_parse_pass_info():
    info_line = '1-3 a: abcde'
    info = parse_pass_info(info_line)

    assert info == PassInfo(1, 3, 'a', 'abcde')


def test_part1_examples():
    pass1 = parse_pass_info('1-3 a: abcde')
    assert pass1.valid_count()
    pass2 = parse_pass_info('1-3 b: cdefg')
    assert not pass2.valid_count()


def test_part2_examples():
    pass1 = parse_pass_info('1-3 a: abcde')
    assert pass1.valid_position()
    pass2 = parse_pass_info('1-3 b: cdefg')
    assert not pass2.valid_position()
    pass3 = parse_pass_info('2-9 c: ccccccccc')
    assert not pass3.valid_position()
