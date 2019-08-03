# grid size
N = 20

grid = []
grid_size = N + 1

for i in range(0, grid_size):
    line = []
    for j in range(0, grid_size):
        line.append(0)
    grid.append(line)

#  fill the edges

for i in range(0, grid_size):
    grid[grid_size - 1][i] = 1
    grid[i][grid_size - 1] = 1

for i in range(grid_size - 2, -1, -1):
    for j in range(grid_size - 2, -1, -1):
        grid[i][j] = grid[i][j + 1] + grid[i + 1][j]

print(grid[0][0])
