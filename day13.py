from intcodeComputer_v_2 import Computer
import matplotlib.pyplot as plt


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

    for y in range(len(screen)):
        print("".join([str(screen[y][x]) for x in range(len(screen[y]))]))
        print("\n")
    plt.imshow(screen, 'gray')
    plt.show()
    return sum([sum([1 if x == 1 else 0 for x in screen]) for y in screen])
