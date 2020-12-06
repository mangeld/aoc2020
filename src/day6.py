from typing import Set
from functools import reduce


def group_answers(group: str) -> Set[str]:
    return reduce(
        lambda a,b: set(a) & set(b),
        group.strip().split()
    )


def answers_count(data: str) -> Set[str]:
    group_counts = [
        len(group_answers(group))
        for group in data.strip().split('\n\n')
    ]
    return reduce(lambda a,b: a + b, group_counts)


if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as data:
        count = answers_count(data.read())
        print('Found', count, 'answers on different groups')