import sys
def parseOrderToCoordinate(orders):
    currentPosition = (0,0)
    coords = [currentPosition]
    for order in orders:
        direction = order[0]
        distance = int(order[1:])
        if direction == 'R':
            currentPosition = (currentPosition[0] + distance, currentPosition[1])
        if direction == 'L':
            currentPosition = (currentPosition[0] - distance, currentPosition[1])
        if direction == 'U':
            currentPosition = (currentPosition[0], currentPosition[1] + distance)
        if direction == 'D':
            currentPosition = (currentPosition[0], currentPosition[1] - distance)
        coords.append(currentPosition)
    return coords

def parse(lines):
    coordsWireOne = parseOrderToCoordinate(lines[0].split(","))
    coordsWiretwo = parseOrderToCoordinate(lines[1].split(","))
    return coordsWireOne, coordsWiretwo
    
def manhatanDistance(point):
    return abs(point[0])+abs(point[1])

def intersectionPoint(segment1, segment2):
    p1, p2 = segment1
    p3, p4 = segment2
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    x4,y4 = p4
    if p1 == p3 or p1 == p4:
        return True, p1
    elif p2==p3 or p2==p4:
        return True, p4
    else:
        if (min(x3,x4)<x1<max(x3,x4) and min(y1,y2) <y3 <max(y1,y2)):
            return True, (x1, y3)
        elif (min(x1,x2)<x3<max(x1,x2) and min(y3,y4) < y1 <max(y3,y4)):
            return True, (x3, y1)

    return False, (0,0)

def nbStep(coords, targetPoint):
    result = 0
    for i in range(len(coords)-1):
        x1,y1 = coords[i] 
        x2,y2 = coords[i+1]
        xt,yt = targetPoint
        if xt == x1 == x2 or yt == y1 == y2:
            result = result + abs(xt-x1) + abs(yt-y1)
            break
        else:
            result =  result + abs(x2-x1) + abs(y2-y1)
    return result

def solve(input):
    result = []
    coordsWireOne, coordsWiretwo = input
    for i in range(len(coordsWireOne)-1):
        segment1 = (coordsWireOne[i], coordsWireOne[i+1])
        for j in range(len(coordsWiretwo)-1):
            segment2 = (coordsWiretwo[j],coordsWiretwo[j+1])
            intersect, point = intersectionPoint(segment1, segment2)
            if intersect and point != (0,0):
                result.append(point)
    print(result)
    minimumDistance = sys.maxsize
    resultPointClosest = (0,0)
    for point in result:
        distance = manhatanDistance(point)
        if distance != 0 and  distance < minimumDistance:
            resultPointClosest = point
            minimumDistance = distance
        
    # pour chaque result, calculer le nombre d'etape
    fewestCombinedStep = sys.maxsize
    for res in result:
        print(res)
        stepWireOne = nbStep(coordsWireOne, res)
        stepWireTwo = nbStep(coordsWiretwo, res)
        print(stepWireOne)
        print(stepWireTwo)
        if (stepWireOne+ stepWireTwo) < fewestCombinedStep:
            fewestCombinedStep = stepWireOne+ stepWireTwo
    return resultPointClosest, fewestCombinedStep

