from time import process_time
from collections import Counter
import Greedy_algoritm as gg
import Greedy_algoritm2 as ggs

def tsp(algorithm, cities):
    t0 = process_time()
    tour = algorithm(cities)
    t1 = process_time()
    assert Counter(tour) == Counter(cities)
    ggs.visualize_tour(tour)
    print("{}:{} cities => tour length {:.0f}(in {:.3f} sec)".format(name(algorithm), len(tour), gg.distance_tour(tour), t1-t0))

def name(algorithm): return algorithm.__name__.replace('_tsp_','') 
def greedy_algorithm(cities, start=None):
    C = start or first(cities)
    tour = [C]
    unvisited = set(cities - {C})
    while unvisited:
        C = nearest_neighbor(C, unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour

def first(collection): return next(iter(collection))

def nearest_neighbor(A, cities):
    return min(cities, key=lambda C: gg.distance_point(C, A)) 

tsp(greedy_algorithm, gg.generate_cities(10))