def calculate_distance(points_order, distances):
    total_distance = 0
    for i in range(len(points_order) - 1):
        total_distance += distances[points_order[i]][points_order[i+1]]
    total_distance += distances[points_order[-1]][points_order[0]]  
    return total_distance
def permutations(arr):
    if len(arr) == 1:
        return [arr]
    result = []
    for i, val in enumerate(arr):
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest):
            result.append([val] + p)
    return result
def traveling_salesman_brute_force(distances):
    num_points = len(distances)
    best_order = None
    min_distance = float('inf')
    for order in permutations(range(num_points)):
        distance = calculate_distance(order, distances)
        if distance < min_distance:
            min_distance = distance
            best_order = order
    return best_order, min_distance
if __name__ == "__main__":
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]
    best_order, min_distance = traveling_salesman_brute_force(distances)
    print("Best order:", best_order)
    print("Minimum distance:", min_distance)
