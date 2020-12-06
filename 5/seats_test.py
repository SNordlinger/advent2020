import seats


def test_parse_seat():
    seat = seats.parse_seat('FBFBBFFRLR')
    assert seat.get_id() == 357


def test_from_id():
    seat = seats.Seat.from_id(567)
    assert seat.row == 70
    assert seat.col == 7
