def parse(lines):
    return list(map(int, lines[0].split(",")))


def checkForDoublon(possibleCode):
    return any((str(i) + str(i) in str(possibleCode) and not str(i) + str(i)+str(i) in str(possibleCode)) for i in range(1, 10))


def solve(minVal, maxVal):
    result = []
    for a in range(int(str(minVal)[0]), 9):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    for e in range(d, 10):
                        for f in range(e, 10):
                            possibleCode = int(''.join(
                                map(str, [a, b, c, d, e, f])))
                            if minVal <= possibleCode <= maxVal and checkForDoublon(possibleCode):
                                result.append(possibleCode)
    return len(result)
