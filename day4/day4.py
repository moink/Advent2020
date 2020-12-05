import re

def process_input(data):
    passports = [{}]
    for line in data:
        if not line:
            passports.append({})
        else:
            for term in line.split():
                key, val = term.split(':')
                passports[-1][key] = val
    return passports


def run_part_1(passports):
    return sum(is_valid_part_one(passport) for passport in passports)


def run_part_2(passports):
    return sum(is_valid_part_two(passport) for passport in passports)


def is_valid_part_one(passport):
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    diff = required.difference(passport.keys())
    return not bool(diff)


def is_valid_part_two(row):
    try:
        if int(row['byr']) < 1920 or int(row['byr']) > 2002:
            return False
        if int(row['iyr']) < 2010 or int(row['iyr']) > 2020:
            return False
        if int(row['eyr']) < 2020 or int(row['eyr']) > 2030:
            return False
        height = int(row['hgt'][:-2])
        if row['hgt'].endswith('cm'):
            if height < 150 or height > 193:
                return False
        elif row['hgt'].endswith('in'):
            if height < 59 or height > 76:
                return False
        else:
            return False
        if not row['hcl'].startswith('#'):
            return False
        if len(row['hcl']) != 7:
            return False
        if not re.match(r'[0-9, a-f]*', row['hcl']):
            return False
        if row['ecl'] not in 'amb blu brn gry grn hzl oth':
            return False
        if len(row['ecl']) !=3:
            return False
        if len(row['pid']) != 9:
            return False
        int(row['pid'])
    except (KeyError, ValueError):
        return False
    return True


if __name__ == '__main__':
    with open('input.txt') as in_file:
        data = in_file.read().splitlines()
    processed = process_input(data)
    print(run_part_1(processed))
    print(run_part_2(processed))