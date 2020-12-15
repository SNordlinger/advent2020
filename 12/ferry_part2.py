import math


class Ferry:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1

    def follow_inst(self, inst):
        cmd = inst[0]
        value = int(inst[1:])

        if cmd == 'N':
            self.waypoint_y += value
        elif cmd == 'E':
            self.waypoint_x += value
        elif cmd == 'S':
            self.waypoint_y -= value
        elif cmd == 'W':
            self.waypoint_x -= value
        elif cmd == 'R':
            self.rotate(-value)
        elif cmd == 'L':
            self.rotate(value)
        elif cmd == 'F':
            self.x = round(self.x + value * self.waypoint_x)
            self.y = round(self.y + value * self.waypoint_y)
        else:
            raise Exception(f'Unrecognized command {cmd}')

    def rotate(self, value):
        x = self.waypoint_x
        y = self.waypoint_y
        rot = math.radians(value)
        self.waypoint_x = x * math.cos(rot) - y * math.sin(rot)
        self.waypoint_y = y * math.cos(rot) + x * math.sin(rot)

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
    print(f'Part 2: {distance}')


if __name__ == '__main__':
    main()
