import re

FIELD_RE = re.compile(r'([a-z]{3}):(\S+)')
HAIR_COLOR_RE = re.compile(r'^#[a-f0-9]{6}$')
EYE_COLOR_RE = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
PID_RE = re.compile(r'^[0-9]{9}$')


def validate_field(key, value):
    if key == 'byr':
        year = int(value)
        return year >= 1920 and year <= 2002
    elif key == 'iyr':
        year = int(value)
        return year >= 2010 and year <= 2020
    elif key == 'eyr':
        year = int(value)
        return year >= 2020 and year <= 2030
    elif key == 'hgt':
        if value.endswith('cm'):
            height = int(value[:-2])
            return height >= 150 and height <= 193
        elif value.endswith('in'):
            height = int(value[:-2])
            return height >= 59 and height <= 76
        else:
            return False
    elif key == 'hcl':
        return re.match(HAIR_COLOR_RE, value) is not None
    elif key == 'ecl':
        return re.match(EYE_COLOR_RE, value) is not None
    elif key == 'pid':
        return re.match(PID_RE, value) is not None
    elif key == 'cid':
        return True

    raise Exception(f'Invalid field {key}')


def get_passport_data(file_path):
    with open(file_path) as infile:
        contents = infile.read()
        passports = contents.split('\n\n')
    return passports


def get_field_name(field_data):
    matches = re.match(FIELD_RE, field_data)
    return matches[1]


def get_field_info(field_data):
    matches = re.match(FIELD_RE, field_data)
    return (matches[1], matches[2])


def check_fields_exist(passport_data):
    field_names = set([get_field_name(f) for f in passport_data.split()])
    expected_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    return field_names.issuperset(expected_fields)


def check_fields_valid(passport_data):
    fields = passport_data.split()
    for field in fields:
        key, value = get_field_info(field)
        if not validate_field(key, value):
            return False

    return True


def count_has_fields(passports):
    return sum(1 for p in passports if check_fields_exist(p))


def count_valid(passports):
    count = 0
    for p in passports:
        if check_fields_exist(p) and check_fields_valid(p):
            count += 1
    return count


def main():
    passports = get_passport_data('input.txt')
    print(f'Part 1: {count_has_fields(passports)}')
    print(f'Part 2: {count_valid(passports)}')


if __name__ == '__main__':
    main()
