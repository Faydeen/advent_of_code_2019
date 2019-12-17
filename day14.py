import math
import operator


class Reaction(object):
    def __init__(self, reactifs, produits):
        self.reactifs = reactifs
        self.produits = produits

    def whatINeedToProduce(self, reactions, name, howManyOutput):
        result = {}
        howManyReactionRequired = math.ceil(
            howManyOutput / self.produits[name])
        resultReactif = dict([(reactif, self.reactifs[reactif] * howManyReactionRequired)
                              for reactif in self.reactifs])
        resultProduit = dict([(produit, -1 * self.produits[produit] * howManyReactionRequired)
                              for produit in self.produits])
        return combine_dicts(resultReactif, resultProduit)


def parse(lines):
    reactions = []
    for line in lines:
        reactifs = line.split(" => ")[0].split(', ')
        produits = line.split("=> ")[1].split(', ')
        p = dict([(p.split(" ")[1], int(p.split(" ")[0])) for p in produits])
        r = dict([(p.split(" ")[1], int(p.split(" ")[0])) for p in reactifs])
        reactions.append(Reaction(r, p))
    return reactions


def findTheOneThatOutput(reactions, produit):
    for r in reactions:
        if produit in r.produits:
            return r


def combine_dicts(a, b, op=operator.add):
    return {x: a.get(x, 0) + b.get(x, 0) for x in set(a).union(b)}


def isReactionOver(required):
    for r in required:
        if r != 'ORE' and required[r] > 0:
            return False
    return 'ORE' in required


def solve(reactions):
    required = {'FUEL': 1}
    while not isReactionOver(required):
        for p in list(required):
            if p != 'ORE' and required[p] > 0:
                reaction = findTheOneThatOutput(reactions, p)
                tempToAdd = reaction.whatINeedToProduce(
                    reactions, p, required[p])
                required = combine_dicts(required, tempToAdd)

    return required['ORE']


def solve2(reactions):
    i = math.floor(1000000000000 / solve(reactions))
    required = {'FUEL': i, 'ORE': 0}
    while required['ORE'] < 1000000000000:

        required = {'FUEL': i, 'ORE': 0}
        while not isReactionOver(required):
            for p in list(required):
                if p != 'ORE' and required[p] > 0:
                    reaction = findTheOneThatOutput(reactions, p)
                    tempToAdd = reaction.whatINeedToProduce(
                        reactions, p, required[p])
                    required = combine_dicts(required, tempToAdd)
        print(f"i : {i}, ORE: {required['ORE']}")
        i = math.floor(i * 1000000000000/required['ORE'])

    return i
