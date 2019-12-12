import itertools


class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Planet(object):
    def __init__(self, x, y, z):
        self.position = Vector(x, y, z)
        self.velocite = Vector(0, 0, 0)
        self.potential_energy = 0
        self.kinetic_energy = 0
        self.updatePotentialEnergy()
        self.updateKineticEnergy()

    def updatePotentialEnergy(self):
        self.potential_energy = abs(
            self.position.x) + abs(self.position.y) + abs(self.position.z)

    def updateKineticEnergy(self):
        self.kinetic_energy = abs(self.position.x) + \
            abs(self.position.y) + abs(self.position.z)

    def updatePosition(self):
        self.position.x += self.velocite.x
        self.position.y += self.velocite.y
        self.position.z += self.velocite.z
        self.updatePotentialEnergy()

    def updateVelocite(self, x, y, z):
        dx = 1
        dy = 1
        dz = 1
        if self.position.x < x:
            dx = 1
        elif self.position.x == x:
            dx = 0
        if self.position.y < y:
            dy = 1
        elif self.position.y == y:
            dy = 0
        if self.position.z < z:
            dz = 1
        elif self.position.z == z:
            dz = 0
        self.velocite.x += dx * 1
        self.velocite.y += dy * 1
        self.velocite.z += dz * 1
        self.updateKineticEnergy()


def parse(lines):
    planets = []
    for line in lines:
        x = int(line.split("x=")[1].split(", ")[0])
        y = int(line.split("y=")[1].split(", ")[0])
        z = int(line.split("z=")[1].split(">")[0])
        planets.append(Planet(x, y, z))
    return planets


def updateVelocity(p1, p2):
    p1.updateVelocite(p2.position.x, p2.position.y, p2.position.z)


def solve(planets, nbStep):
    all_pairs = itertools.permutations(planets, 2)
    for step in range(nbStep + 1):
        # Update velocity
        for pair in all_pairs:
            updateVelocity(*pair)
        # Update position
        for planet in planets:
            planet.updatePosition()
        print(f'Step: {step} planets : {planets}')
    return sum(map(lambda p: p.potential_energy, planets))
