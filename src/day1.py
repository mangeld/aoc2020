from sys import argv
from typing import List
from itertools import combinations
from functools import reduce


def find_2020_entries(entries: List[int], n_products=2) -> List[int]:
    for combination in combinations(entries, n_products):
        if sum(combination) == 2020:
            return list(combination)


if __name__ == '__main__':
    with open(argv[1]) as quizz_input:
        numbers = list(map(int, quizz_input.readlines()))
        answer = find_2020_entries(numbers)
        print("2020 Entries:", answer)
        print("First answer:", answer[0] * answer[1])
        answer = find_2020_entries(numbers, 3)
        print("Second answer:", reduce(lambda a, b: a * b, answer))