class Ferry:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 90

    def move(self, cmd, value):
        if cmd == 'N':
            self.y += value
        elif cmd == 'E':
            self.x += value
        elif cmd == 'S':
            self.y -= value
        elif cmd == 'W':
            self.x -= value
        elif cmd == 'R':
            self.heading = (self.heading + value) % 360
        elif cmd == 'L':
            self.heading = (self.heading - value) % 360
        elif cmd == 'F':
            self.move_with_heading(value)
        else:
            raise Exception(f'Unrecognized command {cmd}')

    def move_with_heading(self, value):
        if self.heading == 0:
            self.y += value
        elif self.heading == 90:
            self.x += value
        elif self.heading == 180:
            self.y -= value
        elif self.heading == 270:
            self.x -= value
        else:
            raise Exception(f'Unrecognized angle {self.heading}')

    def follow_inst(self, inst):
        cmd = inst[0]
        value = int(inst[1:])
        self.move(cmd, value)

    def follow_route(self, route):
        for inst in route:
            self.follow_inst(inst)


def get_input(input_path):
    with open(input_path) as infile:
        return infile.readlines()


def main():
    instructions = get_input('input.txt')
    ferry = Ferry()
    ferry.follow_route(instructions)
    distance = abs(ferry.x) + abs(ferry.y)
    print(f'Part 1: {distance}')


if __name__ == '__main__':
    main()
