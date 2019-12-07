from intcodeComputer_v_2 import Computer
from itertools import permutations
from aoc import read_file


def parse(lines):
    return list(map(int, lines[0].split(",")))


def solve(input):
    finalResult = 0
    for order in permutations(range(0, 5)):
        last_amp = 0
        for i in order:
            computer = Computer(input)
            computer.put(i)
            computer.put(last_amp)
            last_amp = computer.eval()

        finalResult = max(finalResult, last_amp)
    return finalResult


def solve2(initialInstruction):
    result = 0
    for ordre in permutations(range(5, 10)):
        amps = []
        for x in range(len(ordre)):
            amps.append(Computer(initialInstruction))
            amps[x].put(ordre[x])
        amp = 0
        running = True
        while running is True:
            for x in range(5):
                amps[x].put(amp)
                try:
                    amp = amps[x].eval()
                except StopIteration:
                    running = False
        result = max(result, amp)
    return result


data = parse(read_file("07", "1"))
result = solve2(data)

print(f"Solution: {result}")
