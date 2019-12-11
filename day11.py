from intcodeComputer_v_2 import Computer
import matplotlib.pyplot as plt


def parse(lines):
    return list(map(int, lines[0].split(",")))


def solve(instruction):
    computer = Computer(instruction)
    """ 0: up, 1: right, 2: down, 3: left """
    robot_direction = 0
    x = 100
    y = 100
    panel = [[0 for j in range(200)] for i in range(200)]
    running = True
    panelPainted = {}
    while running is True:
        try:
            computer.put(panel[x][y])
            new_color = computer.eval()

            # Count panels
            if (x, y) in panelPainted:
                panelPainted[(x, y)] = panelPainted[(x, y)] + 1
            else:
                panelPainted[(x, y)] = 1

            panel[x][y] = new_color
            new_direction = computer.eval()
            # orientation
            if new_direction == 0:
                robot_direction = (robot_direction - 1) % 4
            else:
                robot_direction = (robot_direction + 1) % 4
            # movement
            if robot_direction == 0:
                y = y-1
            elif robot_direction == 2:
                y = y+1
            elif robot_direction == 1:
                x = x+1
            elif robot_direction == 3:
                x = x-1
        except StopIteration:
            running = False

    plt.imshow(panel, 'gray')
    plt.show()
    return panelPainted


def solve2(instruction):
    computer = Computer(instruction)
    """ 0: up, 1: right, 2: down, 3: left """
    robot_direction = 0
    x = 50
    y = 50
    panel = [[0 for j in range(100)] for i in range(100)]
    panel[x][y] = 1
    running = True
    panelPainted = {}
    while running is True:
        try:
            computer.put(panel[y][x])
            new_color = computer.eval()

            # Count panels
            if (x, y) in panelPainted:
                panelPainted[(x, y)] += 1
            else:
                panelPainted[(x, y)] = 1

            panel[y][x] = new_color

            new_direction = computer.eval()
            # orientation
            if new_direction == 0:
                robot_direction = (robot_direction - 1) % 4
            else:
                robot_direction = (robot_direction + 1) % 4
            # movement
            if robot_direction == 0:
                y = y-1
            elif robot_direction == 2:
                y = y+1
            elif robot_direction == 1:
                x = x+1
            elif robot_direction == 3:
                x = x-1
        except StopIteration:
            running = False

    plt.imshow(panel, 'gray')
    plt.show()
    return panel
