import random
from itertools import permutations

alltours = permutations

def distance_tour(aTour):
    return sum(distance_point(aTour[i-1],aTour[i]) for i in range(len(aTour)))

aCity = complex

def distance_point(first,second):
    return abs (first - second)

def generate_cities(number_of_cities):
    seed=111;width=500;height=300
    random.seed((number_of_cities, seed))
    return frozenset(aCity(random.randint(1,width),random.randint(1,height)) for c in range(number_of_cities))

