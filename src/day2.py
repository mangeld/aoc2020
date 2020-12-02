from typing import Tuple
from dataclasses import dataclass
import re
import sys


@dataclass
class PasswordPolicy:
    word: str


@dataclass
class MinMaxPasswordPolicy(PasswordPolicy):
    min_occurrences: int
    max_occurrences: int


@dataclass
class OnlyOneIndexedPasswordPolicy(PasswordPolicy):
    first_pos: int
    second_pos: int


def handle_min_max(password: str, policy: MinMaxPasswordPolicy) -> bool:
    occurrences = 0
    for char in password:
        if char == policy.word:
            occurrences += 1
        if occurrences > policy.max_occurrences:
            return False
    if occurrences < policy.min_occurrences:
        return False
    return True


def handle_indexed(password: str, policy: OnlyOneIndexedPasswordPolicy) -> bool:
   first = password[policy.first_pos - 1] == policy.word
   second = password[policy.second_pos -1] == policy.word
   return (first or second) and not (first and second)


def is_valid_password(password: str, policy: PasswordPolicy) -> bool:
    handlers = {
        MinMaxPasswordPolicy: handle_min_max,
        OnlyOneIndexedPasswordPolicy: handle_indexed
    }
    return handlers[type(policy)](password, policy)


def parse_line(raw_input: str, policy_type: PasswordPolicy) -> Tuple[str, PasswordPolicy]:
    result = re.search(r'^(\d+)-(\d+) (\w): (\w+)$', raw_input).groups()
    min_occurrences, max_occurrences, word, password = result
    return (
        password,
        policy_type(
            word,
            int(min_occurrences),
            int(max_occurrences),
    ))


if __name__ == '__main__':
    min_max_valids = 0
    index_valids = 0

    with open(sys.argv[1]) as input_data:
        for line in input_data.readlines():
            policy_min_max = parse_line(line, MinMaxPasswordPolicy)
            policy_indexed = parse_line(line, OnlyOneIndexedPasswordPolicy)
            if is_valid_password(*policy_min_max):
                min_max_valids += 1
            if is_valid_password(*policy_indexed):
                index_valids += 1

    print(f'Found {min_max_valids} min max valid passwords')
    print(f'Found {index_valids} only one index valid passwords')