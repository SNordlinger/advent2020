import re
from dataclasses import dataclass

PASS_RE = re.compile(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')


@dataclass
class PassInfo:
    min: int
    max: int
    letter: str
    password: str

    def valid_count(self):
        count = sum(1 for c in self.password if c == self.letter)
        return count >= self.min and count <= self.max

    def valid_position(self):
        in_min = self.__get_char(self.min) == self.letter
        in_max = self.__get_char(self.max) == self.letter
        return (in_min and not in_max) or (in_max and not in_min)

    def __get_char(self, pos):
        idx = pos - 1
        try:
            return self.password[idx]
        except (IndexError):
            return None


def parse_pass_info(info_line):
    matches = re.match(PASS_RE, info_line)
    min_count = int(matches.group(1))
    max_count = int(matches.group(2))
    letter = matches.group(3)
    password = matches.group(4)

    return PassInfo(min_count, max_count, letter, password)


def parse_input():
    with open('input.txt') as infile:
        lines = infile.readlines()
    return [parse_pass_info(line) for line in lines]


def main():
    passes = parse_input()
    valid_count = sum(1 for p in passes if p.valid_count())
    print(f'Part 1: {valid_count}')
    valid_pos_count = sum(1 for p in passes if p.valid_position())
    print(f'Part 2: {valid_pos_count}')


if __name__ == '__main__':
    main()
