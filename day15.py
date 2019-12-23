from aoc import read_file
from intcodeComputer_v_2 import Computer
import sys
import math
import os


def parse(lines):
    return list(map(int, lines[0].split(",")))


def init(computer):
    res = []
    return min(res)


walls = set()


def getRangeIgnoringPreviousPosition(previousDirection):
    if previousDirection == 1:
        return [1, 3, 4]
    if previousDirection == 2:
        return [2, 3, 4]
    if previousDirection == 3:
        return [1, 2, 3]
    if previousDirection == 4:
        return [1, 2, 4]


def getNextPos(pos, direction):
    if direction == 1:
        return (pos[0], pos[1]-1)
    if direction == 2:
        return (pos[0], pos[1]+1)
    if direction == 3:
        return (pos[0]-1, pos[1])
    if direction == 4:
        return (pos[0]+1, pos[1])


def doMove(computer, direction, plan, pos):
    global walls
    nextPos = getNextPos(pos, direction)
    #alreadyVisitedOrWall = plan[nextPos[1]][nextPos[0]] != 0
    if nextPos in walls:
        return sys.maxsize
    newComputer = Computer(computer.memory, computer.pc, computer.rb)
    newComputer.put(direction)
    newState = newComputer.eval()
    if newState == 0:
        walls.add(nextPos)
        plan[nextPos[1]][nextPos[0]] = 2  # it's a wall
        return sys.maxsize
    elif newState == 2:
        return 1
    else:
        plan[pos[1]][pos[0]] = 1
        return 1 + min([doMove(newComputer, x, plan, getNextPos(pos, direction)) for x in getRangeIgnoringPreviousPosition(direction)])


def solve(input):
    """
    Commands:
        - 1 : North
        - 2 : South
        - 3 : West
        - 4 : East
    status codes:
        - 0 : hit a wall. Position not changed
        - 1 : The repair droid has moved one step in the requested direction
        - 2 : The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system
    part 1 : what is the fewest number of movement required
    """
    plan_size = 1000
    # sys.setrecursionlimit(10000)
    plan = [[0 for i in range(plan_size)] for y in range(plan_size)]
    position = (math.floor(plan_size/2), math.floor(plan_size/2))
    computer = Computer(input)
    return min(doMove(computer, 1, plan, position), doMove(computer, 2, plan, position), doMove(computer, 3, plan, position), doMove(computer, 4, plan, position))


def manual_input(position):
    print(f"position: {position}")
    direction = input("\n")
    if direction == 'z':
        direction = 1
    if direction == 's':
        direction = 2
    if direction == 'q':
        direction = 3
    if direction == 'd':
        direction = 4
    if direction not in [1, 2, 3, 4]:
        return manual_input(position)
    return direction


def print_grid(plan, position):
    global tank_location, walls
    grid = [['.' for val in row] for row in plan]
    if tank_location is not None:
        (tank_x, tank_y) = tank_location
        grid[tank_y][tank_x] = 'X'
    for wall in walls:
        (wall_x, wall_y) = wall
        grid[wall_y][wall_x] = '#'
    pos_x, pos_y = position
    grid[pos_y][pos_x] = '@'
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(" ".join(row))


tank_location = None


def manual(input):
    global tank_location, walls
    plan_size = 10
    plan = [[0 for i in range(plan_size)] for y in range(plan_size)]
    position = (math.floor(plan_size/2), math.floor(plan_size/2))
    computer = Computer(input)
    while True:
        print_grid(plan, position)
        newDirection = manual_input(position)
        computer.put(newDirection)
        newState = computer.eval()
        if newState == 0:
            walls.add(getNextPos(position, newDirection))
        elif newState == 2:
            position = getNextPos(position, newDirection)
            tank_location = getNextPos(position, newDirection)
        else:
            position = getNextPos(position, newDirection)


data = parse(read_file("15", "1"))
result = manual(data)
