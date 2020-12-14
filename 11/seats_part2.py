from enum import Enum


class SeatState(Enum):
    FLOOR = 0
    EMPTY = 1
    OCCUPIED = 2


def parse_line(line):
    def parse_char(chr):
        if chr == '.':
            return SeatState.FLOOR
        elif chr == 'L':
            return SeatState.EMPTY
        elif chr == '#':
            return SeatState.OCCUPIED
        else:
            raise Exception(f'Unrecognized character {chr}')

    return [parse_char(c) for c in line.strip()]


def direction_occupied(seats, row, col, row_step, col_step):
    y = row + row_step
    x = col + col_step
    while y >= 0 and x >= 0 and y < len(seats) and x < len(seats[y]):
        if seats[y][x] == SeatState.OCCUPIED:
            return True
        if seats[y][x] == SeatState.EMPTY:
            return False
        y += row_step
        x += col_step
    return False


def get_surrounding_count(seats, row, col):
    count = 0
    for row_step in range(-1, 2):
        for col_step in range(-1, 2):
            if row_step == 0 and col_step == 0:
                continue
            if direction_occupied(seats, row, col, row_step, col_step):
                count += 1
    return count


def next_seat_state(seats, row, col):
    state = seats[row][col]
    if state == SeatState.FLOOR:
        return SeatState.FLOOR

    surrounding = get_surrounding_count(seats, row, col)
    if state == SeatState.EMPTY and surrounding == 0:
        return SeatState.OCCUPIED
    if state == SeatState.OCCUPIED and surrounding >= 5:
        return SeatState.EMPTY
    return state


def step(seats):
    new_seats = []
    for row in range(len(seats)):
        row_size = len(seats[row])
        new_row = [next_seat_state(seats, row, col) for col in range(row_size)]
        new_seats.append(new_row)
    return new_seats


def step_till_stable(seats):
    current = step(seats)
    while True:
        next_seats = step(current)
        if next_seats == current:
            return next_seats
        current = next_seats


def count_occupied(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == SeatState.OCCUPIED:
                count += 1
    return count


def parse_input(filename):
    with open(filename) as infile:
        lines = infile.readlines()
    return [parse_line(line) for line in lines]


def main():
    seat_chart = parse_input('input.txt')
    final_seats = step_till_stable(seat_chart)
    print(f'Part 2: {count_occupied(final_seats)}')


if __name__ == '__main__':
    main()
