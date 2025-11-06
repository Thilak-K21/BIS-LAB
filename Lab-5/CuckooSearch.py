import numpy as np

def distance(route, cities):
    d = 0
    for i in range(len(route)):
        d += np.linalg.norm(cities[route[i % len(route)]] - cities[route[(i + 1) % len(route)]])
    return d

def fitness(route):
    return -distance(route, cities)

def levy_flight(Lambda):
    u = np.random.normal(0, 1, size=dimension)
    v = np.random.normal(0, 1, size=dimension)
    step = u / (np.abs(v) ** (1 / Lambda))
    return step

def random_permutation(n):
    return np.random.permutation(n)

def swap(route):
    a, b = np.random.randint(0, len(route), 2)
    route[a], route[b] = route[b], route[a]
    return route

n = 15
Pa = 0.25
Maxt = 100
dimension = 10

cities = np.random.rand(dimension, 2) * 100
nest = [random_permutation(dimension) for _ in range(n)]
fitness_values = np.array([fitness(x) for x in nest])

for t in range(Maxt):
    new_nest = nest.copy()
    for i in range(n):
        new_route = swap(nest[i].copy())
        fnew = fitness(new_route)
        if fnew > fitness_values[i]:
            new_nest[i] = new_route
            fitness_values[i] = fnew

    K = np.random.rand(n) < Pa
    for i in range(n):
        if K[i]:
            new_route = swap(nest[i].copy())
            new_nest[i] = new_route
            fitness_values[i] = fitness(new_route)

    nest = new_nest.copy()
    best_index = np.argmax(fitness_values)
    best_nest = nest[best_index]

print("Best route:", best_nest)
print("Best distance:", -fitness(best_nest))
