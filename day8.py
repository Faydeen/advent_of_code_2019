import numpy as np
import collections


def parse(lines, wide, tall):
    nbOfPixelPerLayer = wide * tall
    layers = [
        (np.reshape(
            list(map(int, lines[0][i*nbOfPixelPerLayer:i *
                                   nbOfPixelPerLayer+nbOfPixelPerLayer])),
            (tall, wide)))
        for i in range(round(len(lines[0])/(nbOfPixelPerLayer)))]
    return layers


def numberOfInLayer(digit, layer):
    return sum([collections.Counter(line)[digit] for line in layer])


def countZeroOnLayer(layer):
    return numberOfInLayer(0, layer), numberOfInLayer(1, layer) * numberOfInLayer(2, layer)


def solve(layers):
    mapped = list(map(countZeroOnLayer, layers))
    return min(list(mapped), key=lambda t: t[0])


def findPixelAtPosition(line, colomn, layers):
    for layer in layers:
        if layer[line][colomn] != 2:
            return layer[line][colomn]
    return 0


def solve2(layers):
    image = []
    for i in range(6):
        row = []
        for j in range(25):
            row.append(findPixelAtPosition(i, j, layers))
        image.append(row)
    return image
