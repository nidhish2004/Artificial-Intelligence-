import random
class VacuumCleaner:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.current_row = random.randint(0, grid_size - 1)
        self.current_col = random.randint(0, grid_size - 1)
        self.grid = [[random.choice([0, 1]) for _ in range(grid_size)] for _ in range(grid_size)]
    def clean(self):
        print("Initial Grid:")
        self.print_grid()
        while True:
            print(f"Current Position: ({self.current_row}, {self.current_col})")
            if self.grid[self.current_row][self.current_col] == 1:
                print("Cell is dirty. Cleaning...")
                self.grid[self.current_row][self.current_col] = 0
            else:
                print("Cell is already clean.")
            self.move_randomly()
            print("\nUpdated Grid:")
            self.print_grid()
            if self.check_all_clean():
                print("All cells are clean. Cleaning process completed.")
                break
    def move_randomly(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        random_direction = random.choice(directions)
        new_row = self.current_row + random_direction[0]
        new_col = self.current_col + random_direction[1]
        if 0 <= new_row < self.grid_size and 0 <= new_col < self.grid_size:
            self.current_row = new_row
            self.current_col = new_col
    def print_grid(self):
        for row in self.grid:
            print(row)
    def check_all_clean(self):
        for row in self.grid:
            if 1 in row:
                return False
        return True
if __name__ == "__main__":
    grid_size = 3  
    cleaner = VacuumCleaner(grid_size)
    cleaner.clean()
