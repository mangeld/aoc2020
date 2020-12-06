from . import day6
import pytest


INPUT = """abc

a
b
c

ab
ac

a
a
a
a

b
"""

@pytest.mark.parametrize('input,expected', [
    ('ab\nac\n', 1),
    ('abc\n', 3),
    ('a\nb\nc\n', 0),
    ('a\na\na\na\n', 1),
    ('b\n', 1)
])
def test_count_group_anwers(input, expected):
    assert len(day6.group_answers(input)) == expected


def test_count_answers():
    assert day6.answers_count(INPUT) == 6