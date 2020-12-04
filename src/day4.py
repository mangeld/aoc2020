from typing import List
import re


def parse_passports(data: str) -> dict:
    passports = data.split('\n'*2)
    passports_values = [
        re.findall(r'(\w+:[^\ \n]+)', passport)
        for passport in passports
    ]
    passports = [
        dict(i.split(':') for i in vals)
        for vals in passports_values
    ]
    return list(passports)


def count_required_headers(required_headers: List[str], passports: List[dict]) -> int:
    count = 0
    for passport in passports:
        if validate_headers(required_headers, passport):
            count += 1
    return count


def validate_headers(required_headers: List[str], passport: dict) -> bool:
    return all(
        required in passport.keys()
        for required in required_headers
    )

def validate_hgt(value):
    parsed = re.search(r'(\d+)(cm|in)', value)
    if not parsed:
        return False
    value, unit = parsed.groups()
    if unit == 'cm' and (150 <= int(value) <= 193):
        return True
    if unit == 'in' and (59 <= int(value) <= 76):
        return True
    return False

VALIDATORS = {
    'byr': lambda e: len(e) == 4 and (1920 <= int(e) <= 2002),
    'iyr': lambda e: len(e) == 4 and (2010 <= int(e) <= 2020),
    'eyr': lambda e: len(e) == 4 and (2020 <= int(e) <= 2030),
    'hgt': validate_hgt,
    'hcl': lambda e: len(re.findall(r'#[\da-f]{6}', e)) == 1,
    'ecl': lambda e: e in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda e: len(re.findall(r'^\d{9}$', e)) == 1,
}

def count_valid_passports(required_headers: List[str], passports: List[dict]) -> int:
    valid_count = 0
    get_validator = lambda name: VALIDATORS.get(name, lambda e: True)
    for passport in passports:
        valid_data = validate_headers(required_headers, passport)
        valid_data = valid_data and all(get_validator(key)(passport[key]) for key in passport)
        valid_count += 1 if valid_data else 0
    return valid_count


if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as data:
        required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        passports = parse_passports(data.read())
        required_headers_count = count_required_headers(required, passports)
        print('Found', required_headers_count, 'with required headers')
        valid_count = count_valid_passports(required, passports)
        print('Found', valid_count, 'passports with valid values')
        