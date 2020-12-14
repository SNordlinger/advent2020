import seats_part1
import seats_part2


def test_part1_example():
    seat_chart = seats_part1.parse_input('example_input.txt')
    final_seats = seats_part1.step_till_stable(seat_chart)
    assert seats_part1.count_occupied(final_seats) == 37


def test_part2_example():
    seat_chart = seats_part2.parse_input('example_input.txt')
    final_seats = seats_part2.step_till_stable(seat_chart)
    assert seats_part2.count_occupied(final_seats) == 26
