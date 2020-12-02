import pytest

from . import day2


def test_min_max_invalid_password():
    policy = day2.MinMaxPasswordPolicy('b', 1, 3)
    assert day2.is_valid_password('cdefg', policy) == False


@pytest.mark.parametrize('password, policy', [
    ('abcde', day2.MinMaxPasswordPolicy('a', 1, 3)),
    ('ccccccccc', day2.MinMaxPasswordPolicy('c', 2, 9)),
])
def test_min_max_valid_password(password, policy):
    assert day2.is_valid_password(password, policy)


def test_parse_line():
    expect = (
        'djddbhddkdtkvt',
        day2.MinMaxPasswordPolicy('d', 1, 4)
    )
    line = day2.parse_line('1-4 d: djddbhddkdtkvt', day2.MinMaxPasswordPolicy)
    assert line == expect


@pytest.mark.parametrize('password, policy', [
    ('cdefg', day2.OnlyOneIndexedPasswordPolicy('a', 1, 3)),
    ('ccccccccc', day2.OnlyOneIndexedPasswordPolicy('c', 2, 9)),
])
def test_indexed_invalid_password(password, policy):
    assert day2.is_valid_password(password, policy) == False

def test_indexed_valid_password():
    assert day2.is_valid_password(
        'abcde',
        day2.OnlyOneIndexedPasswordPolicy('a', 1, 3)
    )