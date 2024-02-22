from itertools import permutations
def solve_cryptarithmetic(puzzle):
    letters = set(puzzle.replace(' ', ''))
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if all(mapping[word[0]] != 0 for word in puzzle.split()):
            numeric_puzzle = ''.join(str(mapping[char]) if char.isalpha() else char for char in puzzle)
            if eval(numeric_puzzle):
                return mapping
    return None
if __name__ == "__main__":
    puzzle = "SEND + MORE = MONEY"
    solution = solve_cryptarithmetic(puzzle)
    if solution:
        print("Solution found:")
        for key, value in solution.items():
            print(f"{key} = {value}")
    else:
        print("No solution found.")
