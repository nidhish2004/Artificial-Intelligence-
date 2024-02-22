def water_jug_problem(capacity_a, capacity_b, target):
    queue = [(0, 0)] 
    visited = set(queue)
    while queue:
        current_state = queue.pop(0)
        if current_state[0] == target or current_state[1] == target:
            return current_state
        if (capacity_a, current_state[1]) not in visited:
            queue.append((capacity_a, current_state[1]))
            visited.add((capacity_a, current_state[1]))
        if (current_state[0], capacity_b) not in visited:
            queue.append((current_state[0], capacity_b))
            visited.add((current_state[0], capacity_b))
        if (0, current_state[1]) not in visited:
            queue.append((0, current_state[1]))
            visited.add((0, current_state[1]))
        if (current_state[0], 0) not in visited:
            queue.append((current_state[0], 0))
            visited.add((current_state[0], 0))
        pour_amount = min(current_state[0], capacity_b - current_state[1])
        if (current_state[0] - pour_amount, current_state[1] + pour_amount) not in visited:
            queue.append((current_state[0] - pour_amount, current_state[1] + pour_amount))
            visited.add((current_state[0] - pour_amount, current_state[1] + pour_amount))
        pour_amount = min(current_state[1], capacity_a - current_state[0])
        if (current_state[0] + pour_amount, current_state[1] - pour_amount) not in visited:
            queue.append((current_state[0] + pour_amount, current_state[1] - pour_amount))
            visited.add((current_state[0] + pour_amount, current_state[1] - pour_amount))
    return None 
capacity_a = 4
capacity_b = 3
target = 2
result = water_jug_problem(capacity_a, capacity_b, target)
if result:
    print("Solution found:", result)
else:
    print("No solution found.")
