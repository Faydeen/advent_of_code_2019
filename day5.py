import intcodeComputer


def parse(lines):
    return list(map(int, lines[0].split(",")))


def solve(input, id):
    return intcodeComputer.process(input, id)
