from sys import argv
from typing import List, Tuple
from itertools import combinations
from functools import reduce


def find_2020_entries(entries: List[int], n_products=2) -> Tuple[int, ...]:
    for combination in combinations(entries, n_products):
        if sum(combination) == 2020:
            return combination
    return ()


if __name__ == '__main__':
    with open(argv[1]) as quizz_input:
        numbers = list(map(int, quizz_input.readlines()))
        multiply = lambda int_list: reduce(lambda a, b: a * b, int_list)

        answer = find_2020_entries(numbers)
        print("First answer:", multiply(answer))

        answer = find_2020_entries(numbers, 3)
        print("Second answer:", multiply(answer))