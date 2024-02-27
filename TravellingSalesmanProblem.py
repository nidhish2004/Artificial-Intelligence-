import itertools

def tsp_brute_force(graph, start):
    all_nodes = set(graph.keys())
    all_nodes.remove(start)
    min_cost = float('inf')
    best_path = None

    for path in itertools.permutations(all_nodes):
        path = (start,) + path + (start,)
        cost = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
        
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

# Example Usage
graph = {
    'A': {'A': 0, 'B': 2, 'C': 9, 'D': 6},
    'B': {'A': 1, 'B': 0, 'C': 3, 'D': 7},
    'C': {'A': 4, 'B': 5, 'C': 0, 'D': 8},
    'D': {'A': 3, 'B': 6, 'C': 2, 'D': 0}
}

start_node = 'A'
best_path, min_cost = tsp_brute_force(graph, start_node)
print("Best Path:", best_path)
print("Minimum Cost:", min_cost)
