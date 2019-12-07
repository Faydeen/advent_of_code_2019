import intcodeComputer
from copy import copy
from itertools import permutations
from aoc import read_file


def parse(lines):
    return list(map(int, lines[0].split(",")))


def allAccu(instructions, initInput):
    previousResult = 0
    for i in initInput:
        input = copy(instructions)
        ampliResult = intcodeComputer.process(input, [i, previousResult])
        previousResult = ampliResult[-1]

    return previousResult


def solve(input):
    finalResult = 0
    for order in itertools.permutations([0, 1, 2, 3, 4], 5):
        last_amp = 0
        for i in order:
            instructions = copy(input)
            last_amp = intcodeComputer.process(
                instructions, 0, [i, last_amp])[-1]

        finalResult = max(finalResult, last_amp)
    return finalResult


def solve2(initialInstruction):
    result = 0
    for ordre in permutations([5, 6, 7, 8, 9]):
        regs = []
        inps = []
        for x in range(5):
            regs.append(copy(initialInstruction))
            inps.append([ordre[x]])
        ips = [0] * 5
        amp = 0
        while amp is not None:
            for x in range(5):
                inps[x].append(amp)
                regs[x], ips[x], inps[x], amp = intcodeComputer.process(
                    regs[x], ips[x], inps[x])
            last_amp = last_amp if amp is None else amp
        result = max(result, last_amp)
    return result


data = parse(read_file("07", "1"))
result = solve2(data)

print(f"Solution: {result}")
