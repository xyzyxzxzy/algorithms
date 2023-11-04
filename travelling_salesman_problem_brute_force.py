# You have a list of cities, and the distances between each pair of cities are known.
# The goal is to find the shortest possible route that visits each city once and
# returns to the original city (completing the circuit). This route is often referred to as the "optimal tour."
# O(n! * m), where n is the number of cities, m is the number of additional actions within each permutation.

import itertools

def calculate_total_distance(path, distances):
    # function to calculate the total distance in a route
    total_distance = 0
    n = len(path)
    for i in range(n - 1):
        total_distance += distances[path[i]][path[i + 1]]
    total_distance += distances[path[n - 1]][path[0]]  # return to the starting city
    return total_distance

def brute_force_tsp(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    min_distance = float("inf")
    best_path = None

    # using itertools.permutations to iterate through all possible routes
    for path in itertools.permutations(cities):
        total_distance = calculate_total_distance(path, distances)
        if total_distance < min_distance:
            min_distance = total_distance
            best_path = path

    return best_path, min_distance

# cities
distances = [
    [0, 29, 20, 21],
    [29, 0, 15, 18],
    [20, 15, 0, 16],
    [21, 18, 16, 0]
]

best_path, min_distance = brute_force_tsp(distances)
print("Best path:", best_path)
print("Minimum distance:", min_distance)
