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


def get_surrounding_count(seats, row, col):
    count = 0
    for y in range(row - 1, row + 2):
        for x in range(col - 1, col + 2):
            if y == row and x == col:
                continue
            if y < 0 or y >= len(seats):
                continue
            if x < 0 or x >= len(seats[y]):
                continue
            if seats[y][x] == SeatState.OCCUPIED:
                count += 1
    return count


def next_seat_state(seats, row, col):
    state = seats[row][col]
    if state == SeatState.FLOOR:
        return SeatState.FLOOR

    surrounding = get_surrounding_count(seats, row, col)
    if state == SeatState.EMPTY and surrounding == 0:
        return SeatState.OCCUPIED
    if state == SeatState.OCCUPIED and surrounding >= 4:
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
    print(f'Part 1: {count_occupied(final_seats)}')


if __name__ == '__main__':
    main()
