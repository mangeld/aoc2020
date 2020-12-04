from . import day4

TEST_DATA = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

INVALID_PASSPORTS = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

VALID_PASSPORTS = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
VALID_KEYS = REQUIRED_KEYS + ['cid']


def test_parse_passports():
    assert len(day4.parse_passports(TEST_DATA)) == 4


def test_count_required_headers():
    passports = day4.parse_passports(TEST_DATA)
    assert day4.count_required_headers(REQUIRED_KEYS, passports) == 2


def test_count_invalid_passport():
    passports = day4.parse_passports(INVALID_PASSPORTS)
    assert day4.count_valid_passports(REQUIRED_KEYS, passports) == 0


def test_count_valid_passport():
    passports = day4.parse_passports(VALID_PASSPORTS)
    assert day4.count_valid_passports(REQUIRED_KEYS, passports) == 4


def test_byr_validator():
    assert not day4.VALIDATORS['byr']('2020')
    assert day4.VALIDATORS['byr']('2000')

def test_hgt_validator():
    assert not day4.VALIDATORS['hgt']('190in')
    assert not day4.VALIDATORS['hgt']('190')
    assert day4.VALIDATORS['hgt']('60in')
    assert day4.VALIDATORS['hgt']('190cm')

def test_pid_validator():
    assert not day4.VALIDATORS['pid']('0123456789')
    assert day4.VALIDATORS['pid']('000000001')