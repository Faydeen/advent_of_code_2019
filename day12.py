import itertools


class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"<x= {self.x} y= {self.y} z= {self.z} >"

    def __str__(self):
        return f"<x= {self.x} y= {self.y} z= {self.z} >"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


class Planet(object):
    def __init__(self, id,  x, y, z):
        self.id = id
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
        self.kinetic_energy = abs(self.velocite.x) + \
            abs(self.velocite.y) + abs(self.velocite.z)

    def updatePosition(self):
        self.position.x += self.velocite.x
        self.position.y += self.velocite.y
        self.position.z += self.velocite.z
        self.updatePotentialEnergy()

    def updateVelocite(self, x, y, z):
        dx = -1
        dy = -1
        dz = -1
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

    def get_total_energy(self):
        return self.kinetic_energy * self.potential_energy

    def __str__(self):
        return f"{self.position} {self.velocite}"

    def __repr__(self):
        return f"self.id: \n\t{self.position}\n\t{self.velocite}"

    def __eq__(self, other):
        return self.velocite == other.velocite and self.position == other.position


def parse(lines):
    planets = []
    planetsName = ["Io", "Europa", "Ganymede", "Callisto"]
    for line in lines:
        x = int(line.split("x=")[1].split(", ")[0])
        y = int(line.split("y=")[1].split(", ")[0])
        z = int(line.split("z=")[1].split(">")[0])
        planets.append(Planet(planetsName[0], x, y, z))
        planetsName = planetsName[1:]
    return planets


def updateVelocity(p1, p2):
    p1.updateVelocite(p2.position.x, p2.position.y, p2.position.z)


def simulate(planets):
    # Update velocity
    for pair in itertools.permutations(planets, 2):
        updateVelocity(*pair)
    # Update position
    for planet in planets:
        planet.updatePosition()


def solve(planets, nbStep):
    all_pairs = itertools.permutations(planets, 2)
    print(f"After 0 step:")
    for planet in planets:
        print(planet)
    for step in range(1, nbStep + 1):
        simulate(planets)
        print(f"After {step} step:")
        for planet in planets:
            print(planet)
    return sum(map(lambda p: p.get_total_energy(), planets))


def solve2(planets):
    steps = 1
    initial_x_proj = [planet.position.x for planet in planets]
    initial_y_proj = [planet.position.y for planet in planets]
    initial_z_proj = [planet.position.z for planet in planets]
    x_sol = None
    y_sol = None
    z_sol = None
    while x_sol == None or y_sol == None or z_sol == None:
        simulate(planets)
        y_proj = [planet.position.y for planet in planets]
        z_proj = [planet.position.z for planet in planets]
        if x_sol == None:
            pos_proj = [planet.position.x for planet in planets]
            vel_proj = [planet.velocite.x for planet in planets]
            if pos_proj == initial_x_proj and vel_proj == [0, 0, 0, 0]:
                x_sol = steps
        if y_sol == None:
            pos_proj = [planet.position.y for planet in planets]
            vel_proj = [planet.velocite.y for planet in planets]
            if pos_proj == initial_y_proj and vel_proj == [0, 0, 0, 0]:
                y_sol = steps
        if z_sol == None:
            pos_proj = [planet.position.z for planet in planets]
            vel_proj = [planet.velocite.z for planet in planets]
            if pos_proj == initial_z_proj and vel_proj == [0, 0, 0, 0]:
                z_sol = steps
        steps += 1
    return ppcm(x_sol, y_sol, z_sol)


def ppcm(*n):
    """Calcul du 'Plus Petit Commun Multiple' de n (>=2) valeurs entières (Euclide)"""
    def _pgcd(a, b):
        while b:
            a, b = b, a % b
        return a
    p = abs(n[0]*n[1])//_pgcd(n[0], n[1])
    for x in n[2:]:
        p = abs(p*x)//_pgcd(p, x)
    return p
