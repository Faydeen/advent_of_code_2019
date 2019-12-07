import intcodeComputer


def parse(lines):
    return list(map(int, lines[0].split(",")))


def solve(input, noun=0, verb=0):
    input[1] = noun
    input[2] = verb
    return intcodeComputer.process(input)
