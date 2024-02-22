def valid_state(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True
def dfs(m_left, c_left, m_right, c_right, path, visited):
    if not valid_state(m_left, c_left, m_right, c_right):
        return False
    if (m_left, c_left, m_right, c_right) in visited:
        return False
    visited.add((m_left, c_left, m_right, c_right))
    path.append((m_left, c_left, m_right, c_right)) 
    if m_left == 0 and c_left == 0:
        return True
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for move in moves:
        next_m_left = m_left - move[0]
        next_c_left = c_left - move[1]
        next_m_right = m_right + move[0]
        next_c_right = c_right + move[1]
        if dfs(next_m_left, next_c_left, next_m_right, next_c_right, path, visited):
            return True
    path.pop()
    return False
def print_solution(path):
    print("Missionaries and Cannibals Problem Solution:")
    for state in path:
        print(state)
def solve_missionaries_cannibals():
    m_left, c_left, m_right, c_right = 3, 3, 0, 0
    path = []
    visited = set()
    dfs(m_left, c_left, m_right, c_right, path, visited)
    print_solution(path)
if __name__ == "__main__":
    solve_missionaries_cannibals()
