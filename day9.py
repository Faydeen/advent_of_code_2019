from intcodeComputer_v_2 import Computer


def parse(lines):
    return list(map(int, lines[0].split(",")))


def solve(instruction, input=[]):
    computer = Computer(instruction)

    for i in input:
        computer.put(i)
    answer = []
    running = True
    while running is True:
        try:
            answer.append(computer.eval())
        except StopIteration:
            running = False
    return answer
