import re
coordinates = []

COMPAS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
DIRS = ">v<^"

def print_coord():
    for row in coordinates:
        for x in row:
            print(x, end="")
        print("")

with open("test.txt") as f:
    grid, code = f.read().split("\n\n")

    glines = grid.split("\n")
    x_size = max([len(x) for x in glines])
    y_size = len(glines)
    print(x_size, y_size)

    line = [" " for x in range(0, x_size)]
    coordinates = [list(line) for y in range(0, y_size)]
    
    for y, row in enumerate(glines):
        print(y, row)
        for x, c in enumerate(row):
            
            if c in ".#":
                coordinates[y][x] = c

    # print(coordinates)
    print_coord()


    position = [0, glines[0].find(".")]
    print(position)
    

    items = [int(x) for x in re.split(r"[LR]", code)]
    print(items)
    rotations = re.split(r"\d+", code)[1:]
    print(rotations)

    increment = [0, 1]
    c_inc = 0
    for steps, rot in zip(items, rotations):
        while steps:
            print(steps, rot)
            new_pos = [position[0] + increment[0], position[1] + increment[1]]
            print(new_pos)
            steps -= 1

            y, x = new_pos

            # top of grid
            if y < 0:
                y = y_size-1
            elif y == y_size:
                y = 0 if x < 12 else y_size-4
            
            # bottom of grid
            elif x < 0:
                x = (x_size-4)
            elif x == x_size:
                x = 8

            # top left
            elif y < 4 and x < 8:
                x += 4
            elif y < 4 and x >= 12:
                x -= 4

            # middle left (there are two cubes here)
            elif y >= 4 and x >= 12:
                x = 0
            elif y < 4 and x < 8:
                y += 4
            elif y >= 8 and x < 8:
                y -= 4
            elif y > 8 and x < 8:
                x += 8

            new_pos = [y, x]


            if coordinates[new_pos[0]][new_pos[1]] == "#":
                break
            elif coordinates[new_pos[0]][new_pos[1]] == " ":
                pass
            position = new_pos
            coordinates[position[0]][position[1]] = DIRS[c_inc]
        
        print_coord()
        if rot == "R":
            c_inc = (c_inc+1) % 4
        elif rot == "L":
            c_inc = (c_inc-1) % 4

        increment = COMPAS[c_inc]


    result = 1000 * (position[0]+1) + 4 * (position[1]+1) + COMPAS.index(increment)
    print(result)
    # for i in items:
    #     print(i)

    # print(len(lines))
    # for l in lines:
    #     print(l)
    #print(grid, input)