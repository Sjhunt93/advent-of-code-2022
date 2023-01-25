import re
coordinates = []

COMPAS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
DIRS = ">v<^"
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

def print_coord():
    for row in coordinates:
        for x in row:
            print(x, end="")
        print("")
    
    print("")


ROTATE_LEFT = 0
ROTATE_RIGHT = 0




def check_boundries(position, new_pos, increment):
    cy, cx = position
    y, x = new_pos
    new_inc = increment
    # -------------------------- A //tested
    if y < 0 and x < 100: ## A - F
        y = (x - 50) + 150
        x = 0
        new_inc = COMPAS[RIGHT]
        #print("AF")

    elif x == 49 and y < 50: ## A - D //tested
        y = 100 + (49-y)
        x = 0    
        new_inc = COMPAS[RIGHT]
        #print("AD")
    # AC and AB
    # -------------------------- B
    elif y < 0 and x < 150: ## B - F
        y = 199
        x = x-100
        new_inc = COMPAS[UP]
        #print("AD")
    elif y == 50 and x >= 100 and cy == 49: ## B - C
        y = (x - 100) + 50
        x = 99
        new_inc = COMPAS[LEFT]
    elif x == 150: ## B - E
        y = (49-y) + 100
        x = 99
        new_inc = COMPAS[LEFT]
    # BA
    # -------------------------- C
    elif x == 49 and y < 100 and cx == 50: ## C - D //tested
        x = y - 50
        y = 100
        new_inc = COMPAS[DOWN]
    elif y < 100 and x == 100 and cx == 99 and y >= 50: ## C - B
        x = (y - 50) + 100
        y = 49
        new_inc = COMPAS[UP]
    # CE CA
    # -------------------------- D
    elif x < 50 and y == 99 and cy == 100: ## D - C //tesed
        y = 50+x
        x = 50
        new_inc = COMPAS[RIGHT]

    elif x < 0 and y < 150: ## D - A //tesed
        y = 49-(y-100)
        x = 50
        new_inc = COMPAS[RIGHT]
    # DE DF
    # -------------------------- E
    elif x == 100 and y < 150 and y >= 100: ## E - B
        y = 49-(y-100)
        x = 149
        new_inc = COMPAS[LEFT]
    elif y == 150 and x >= 50 and cy == 149: ## E - F
        y = (x-50) + 150
        x = 49
        new_inc = COMPAS[LEFT]
    # ED EC
    # -------------------------- F
    elif y == 200: # F - B
        x = x + 100
        y = 0
        new_inc = COMPAS[DOWN]
    elif x < 0 and y >= 150: ## F - A
        x = (y - 150) + 50
        y = 0
        new_inc = COMPAS[DOWN]

    elif x == 50 and y >= 150 and cx == 49: ## F - E
        x = (y - 150) + 50
        y = 149
        new_inc = COMPAS[UP]

    return [y, x], new_inc

#           A
#   B   C   D
#           E   F

#   A B
#   C
# D E
# F


with open("input.txt") as f:
    grid, code = f.read().split("\n\n")

    glines = grid.split("\n")
    x_size = max([len(x) for x in glines])
    y_size = len(glines)
    print(x_size, y_size)

    line = [" " for x in range(0, x_size)]
    coordinates = [list(line) for y in range(0, y_size)]
    
    for y, row in enumerate(glines):
        for x, c in enumerate(row):
            if c in ".#":
                coordinates[y][x] = c


    position = [0, glines[0].find(".")]
    items = [int(x) for x in re.split(r"[LR]", code)]
    rotations = re.split(r"\d+", code)[1:]
    

    increment = [0, 1]
    c_inc = 0
    for steps, rotation in zip(items, rotations):
        
        while steps:
            
            steps -= 1

            new_pos = [(position[0] + increment[0]), (position[1] + increment[1])]
            new_pos, new_inc = check_boundries(position, new_pos, increment)

            
            if coordinates[new_pos[0]][new_pos[1]] == "#":
                break
        
            increment = new_inc
            c_inc = COMPAS.index(increment)
            position = new_pos
            coordinates[position[0]][position[1]] = DIRS[c_inc]
            
        
        if rotation == "R":
            c_inc = (c_inc+1) % 4
        elif rotation == "L":
            c_inc = (c_inc-1) % 4

        increment = COMPAS[c_inc]


    result = 1000 * (position[0]+1) + 4 * (position[1]+1) + COMPAS.index(increment)
    print(result)