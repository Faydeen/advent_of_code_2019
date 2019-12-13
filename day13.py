from intcodeComputer_v_2 import Computer
import numpy as np
from collections import Counter
import ffmpeg


def parse(lines):
    return list(map(int, lines[0].split(",")))


def solve(instruction):
    computer = Computer(instruction)
    running = True
    screenSize = 50
    screen = [[0 for i in range(38)] for j in range(20)]
    while running is True:
        try:
            x = computer.eval()
            y = computer.eval()
            tileId = computer.eval()
            screen[y][x] = tileId
        except StopIteration:
            running = False

    return sum([Counter(line)[2] for line in screen])


def solve2(instruction):
    screens = []
    instruction[0] = 2
    computer = Computer(instruction)
    running = True
    screenSize = 50
    screen = [[0 for i in range(38)] for j in range(20)]
    next_input = 0
    score = 0
    while running is True:
        try:
            computer.clear()
            computer.put(screen_input(screen))
            x = computer.eval()
            y = computer.eval()
            tileId = computer.eval()
            if x == -1 and y == 0:
                score = tileId
                print(f"Score : {score}")
            else:
                screen[y][x] = tileId
                screens.append(screen)

        except StopIteration:
            running = False

    return score


def screen_input(screen):
    ball_x = -1
    paddle_x = -1
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if screen[y][x] == 4:
                ball_x = x
            if screen[y][x] == 3:
                paddle_x = x
    return np.sign(ball_x - paddle_x)
