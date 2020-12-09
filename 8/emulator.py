class Emulator:
    def __init__(self, instructions):
        self.inst = 0
        self.acc = 0
        self.instructions = instructions

    def step(self):
        instruction = self.instructions[self.inst]
        opcode = instruction[:3]
        value = int(instruction[4:])

        if opcode == 'acc':
            self.acc += value
            self.inst += 1
        elif opcode == 'jmp':
            self.inst += value
        elif opcode == 'nop':
            self.inst += 1

    def run(self):
        seen_values = set()
        while self.inst < len(self.instructions):
            if self.inst in seen_values:
                return 1
            seen_values.add(self.inst)
            self.step()
        return 0


def get_input(file_path):
    with open(file_path) as infile:
        lines = infile.readlines()
    return [line.strip() for line in lines]


def find_acc_at_loop(instructions):
    emu = Emulator(instructions)
    emu.run()
    return emu.acc


def swap_instruction(instructions):
    last_index = len(instructions) - 1
    new_inst = 'nop +0'
    for i in range(last_index, -1, -1):
        inst = instructions[i]
        if inst[:3] == 'jmp':
            yield instructions[:i] + [new_inst] + instructions[i+1:]


def find_acc_at_termination(instructions):
    for replaced in swap_instruction(instructions):
        emu = Emulator(replaced)
        exit_code = emu.run()
        if exit_code == 0:
            return emu.acc


def main():
    instructions = get_input('input.txt')
    print(f'Part 1: {find_acc_at_loop(instructions)}')
    print(f'Part 2: {find_acc_at_termination(instructions)}')


if __name__ == '__main__':
    main()
