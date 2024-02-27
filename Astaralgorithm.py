import heapq

def astar(graph, start, end):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (0, start))
    while open_list:
        cost, current_node = heapq.heappop(open_list)
        if current_node == end:
            return cost
        if current_node in closed_set:
            continue
        closed_set.add(current_node)
        for neighbor, neighbor_cost in graph[current_node].items():
            if neighbor not in closed_set:
                heapq.heappush(open_list, (cost + neighbor_cost, neighbor))
    return float('inf')

# Example Usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
end_node = 'D'
shortest_path_cost = astar(graph, start_node, end_node)
print(f"The shortest path cost from {start_node} to {end_node} is: {shortest_path_cost}")
