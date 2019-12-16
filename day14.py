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
        return dict([(reactif, self.reactifs[reactif] * howManyReactionRequired)
                     for reactif in self.reactifs])


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


def solve(reactions):
    required = {'FUEL': 1}
    while len(required) != 1 or 'ORE' not in required:
        for p in list(required):
            if p != 'ORE':
                reaction = findTheOneThatOutput(reactions, p)
                tempToAdd = reaction.whatINeedToProduce(
                    reactions, p, required[p])
                del required[p]
                required = combine_dicts(required, tempToAdd)

    return required['ORE']
