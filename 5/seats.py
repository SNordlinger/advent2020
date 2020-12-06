from dataclasses import dataclass
from itertools import dropwhile


@dataclass
class Seat:
    row: int
    col: int

    def get_id(self):
        return self.row * 8 + self.col

    def from_id(seat_id):
        col = seat_id % 8
        row = (seat_id - col) // 8
        return Seat(row, col)


def get_input():
    with open('input.txt') as input_file:
        return [line.strip() for line in input_file.readlines()]


def parse_seat(boarding_pass):
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7

    for char in boarding_pass[:7]:
        if char == 'F':
            max_row = find_midpoint(min_row, max_row)
        else:
            min_row = find_midpoint(min_row, max_row) + 1

    for char in boarding_pass[7:]:
        if char == 'L':
            max_col = find_midpoint(min_col, max_col)
        else:
            min_col = find_midpoint(min_col, max_col) + 1

    return Seat(min_row, min_col)


def find_midpoint(min_idx, max_idx):
    return min_idx + (max_idx - min_idx) // 2


def find_max_id(seats):
    return max(s.get_id() for s in seats)


def find_open_seat(seats):
    seat_availability = [True] * 128 * 8
    for seat in seats:
        seat_id = seat.get_id()
        seat_availability[seat_id] = False

    seat_iter = dropwhile(lambda x: x[1], enumerate(seat_availability))

    for seat_id, is_open in seat_iter:
        if is_open:
            seat = Seat.from_id(seat_id)
            if seat.row != 0 and seat.row != 127:
                return seat

    raise Exception('Cannot find open seat')


def main():
    boarding_passes = get_input()
    seats = [parse_seat(p) for p in boarding_passes]
    print(f'Part 1: {find_max_id(seats)}')
    print(f'Part 2: {find_open_seat(seats).get_id()}')


if __name__ == '__main__':
    main()
