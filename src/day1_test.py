from .day1 import find_2020_entries

TEST_INPUT = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

def test_find_two_2020_entries():
    result = find_2020_entries(TEST_INPUT)
    assert result == [1721, 299]

def test_find_three_2020_entries():
    result = find_2020_entries(TEST_INPUT, 3)
    assert result == [979, 366, 675]