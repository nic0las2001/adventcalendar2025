
input = open("inputs/d4.txt","r")

grid = []
for line in input:
    if len(line) > 1:
        grid.append(list(line[:-1]))

roll_count = 0
prev_count = 0


def forklift_removal(grid, roll_count):
    x_max = len(grid)
    y_max = len(grid[0])

    new_grid = []

    for x in range(x_max):
        new_grid.append([])
        for y in range(y_max):
            new_grid[x].append(grid[x][y])
            if grid[x][y] == "@":
                neighbour_count = 0
                neighbours = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
                valid = []

                # handle spots around edges
                for cell in neighbours:
                    if cell[0] >= 0 and cell[0] < x_max:
                        if cell[1] >= 0 and cell[1] < y_max:
                            valid.append(cell)

                for cell2 in valid:
                    if grid[cell2[0]][cell2[1]] == "@":
                        neighbour_count += 1
                
                if neighbour_count < 4:
                    roll_count += 1
                    new_grid[x][y] = "X"

    return new_grid, roll_count

# Part 1
grid, roll_count = forklift_removal(grid, roll_count)
print("P1:", roll_count)

# P2 
while roll_count > prev_count:
    prev_count = roll_count
    grid, roll_count = forklift_removal(grid, roll_count)

print("P2:", roll_count)