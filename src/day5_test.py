import pytest

from . import day5


@pytest.mark.parametrize('boarding_id,expected', [
    ('FFFFFFFFFF', 0),
    ('BBBBBBBBBB', 127),
    ('BFFFBBFRRR', 70),
    ('FFFBBBFRRR', 14),
    ('FBFBBFFRLR', 44),
    ('BBFFBBFRLL', 102),
    ('BBFBFBFLRL', 106)
])
def test_search_row(boarding_id, expected):
    assert day5.search_row(boarding_id) == expected


@pytest.mark.parametrize('boarding_id,expected', [
    ('FBFBBFFRLR', 5),
    ('FBFBBFFLLL', 0),
    ('BFFFBBFRRR', 7),
    ('FFFBBBFRRR', 7),
    ('BBFFBBFRLL', 4),
    ('BBFBFBFLRL', 2)
])
def test_search_seat(boarding_id, expected):
    assert day5.search_seat(boarding_id) == expected


def test_calc_seat_id():
    assert day5.calc_seat_id(70, 7) == 567
    assert day5.calc_seat_id(14, 7) == 119
    assert day5.calc_seat_id(44, 5) == 357
    assert day5.calc_seat_id(102, 4) == 820