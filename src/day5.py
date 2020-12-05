
from typing import List
from dataclasses import dataclass


@dataclass
class Range:
    lower: int
    upper: int


def search_row(boarding_id: str) -> int:
    boarding_id = boarding_id[:7]
    row_range = Range(0, 127)
    for char in boarding_id:
        _range = row_range.upper - row_range.lower
        if char == 'F':
            row_range.upper = row_range.upper - round(_range / 2)
        if char == 'B':
            row_range.lower = row_range.lower + round(_range / 2)
    return row_range.lower if boarding_id[-1] == 'F' else row_range.upper


def search_seat(boarding_id: str) -> int:
    boarding_id = boarding_id[7:]
    seat_range = Range(0, 7)
    for char in boarding_id:
        _range = seat_range.upper - seat_range.lower
        if char == 'L':
            seat_range.upper = seat_range.upper - round(_range / 2)
        if char == 'R':
            seat_range.lower = seat_range.lower + round(_range / 2)
    return seat_range.lower if boarding_id[-1] == 'L' else seat_range.upper


def calc_seat_id(row: int, seat: int) -> int:
    return (row * 8) + seat


def search(values: List[int]) -> int:
    values = sorted(values)
    for i in range(0, len(values) - 1):
        diff = values[i+1] - values[i]
        if diff != 1:
            return values[i] + 1
    return None


if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as data:
        seat_ids = [
            calc_seat_id(
                search_row(boarding_id.strip()),
                search_seat(boarding_id.strip())
            )
            for boarding_id in data.readlines()
        ]
        print('Found', len(seat_ids), 'seat id\'s')
        print('Highest seat ID:', max(seat_ids))
        print(search(seat_ids))