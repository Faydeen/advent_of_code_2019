from collections import Counter
import math
import sys


def parse(lines):
    asteroids = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "#":
                asteroids.append((x, y))
    return asteroids


def in_sight(asteroids, asteroid):
    pentes = {}
    for toCheck in asteroids:
        if toCheck != asteroid:
            p = compute_angle(asteroid, toCheck)
            if p not in pentes:
                pentes[p] = [toCheck]
            else:
                pentes[p].append(toCheck)
                pentes[p].sort(key=lambda x: abs(
                    x[0]-asteroid[0])+abs(x[1]-asteroid[1]))
    return len(pentes), sorted(list(zip(pentes.keys(), pentes.values())), key=lambda x: x[0])


def solve(asteroids):
    result = ((), 0)
    for asteroid in asteroids:
        nbOfSight = len(in_sight(asteroids, asteroid))
        if nbOfSight >= result[1]:
            result = (asteroid, nbOfSight)
    return result


def solve_2(asteroids, laserPosition):
    sighableAst = in_sight(asteroids, laserPosition)
    idx = [x[0] for x in sighableAst[1]].index(0)
    for i in range(201):
        if(i == 200):
            return sighableAst[1][idx]
        sighableAst[1][idx] = sighableAst[1][idx][1:]
        idx = (idx + 1) % len(sighableAst[1])


def compute_angle(p1, p2):
    "Return true if q is between p and r (inclusive)."
    deltaX = p1[0] - p2[0]
    deltaY = p2[1] - p1[1]
    return math.atan2(deltaY, deltaX)
    # q = p2[0] - p1[0]
    # p = p2[1] - p1[1]
    # s = 0
    # if p > 0:
    #     s = 1
    # elif p < 0:
    #     s = -1

    # if q == 0:
    #     return (sys.maxsize, s)

    # return (p / q, s)
