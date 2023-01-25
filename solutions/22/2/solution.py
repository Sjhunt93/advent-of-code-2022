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


#           A
#   B   C   D
#           E   F
#
#
#


def mapping(from_face, to_face):
    transitions = {
        "AC" : [-1],
        "AB" : [2],
        "AD" : [0],
        "AF" : [2],
        ## D
        "DC" : [0],
        "DE" : [0],
        "DF" : [1],
        "DA" : [0],
        # E 
        "ED" : [0],
        "EF" : [0],
        "EC" : [1],
        "EB" : [2],
        # B
        "BC" : [0],
        "BA" : [2],
        "BE" : [2],
        "FB" : [-1],
        # C
        "CB" : [0],
        "CD" : [0],
        "CE" : [1],
        "CA" : [-1]
    }
    op1 = from_face+to_face
    op2 = to_face+from_face
    if op1  in transitions:
        return transitions[op1]

    elif op2  in transitions:
        return transitions[-op1]



def find_corners():
    corners = []
    for y in range(0, len(coordinates)-1):
        for x in range(0, len(coordinates[0])-1):
            quad = [[y, x], [y+1, x], [y, x+1], [y+1, x+1]]
            count = [coordinates[q[0]][q[1]] == " "  for q in quad].count(True)
            if count == 1:
                corners.append(quad)
                #for q in quad:


    print(len(corners))
            


def face_for_x_y(x, y):
    if y < 4:
        return 'A'
    if y <  8:
        return 'BCD '[x/4]
    if y < 12:
        return '  EF'[x/4]
    return " "

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
    items = [int(x) for x in re.split(r"[LR]", code)]
    rotations = re.split(r"\d+", code)[1:]
    

    increment = [0, 1]
    c_inc = 0
    for steps, rot in zip(items, rotations):
        while steps:
            
            new_pos = [(position[0] + increment[0]), (position[1] + increment[1])]
            
            steps -= 1
            cy, cx = position
            y, x = new_pos
            new_inc = increment

            # -------------------------- A
            if y < 0: # A -B
                y -= 4
                x = 3 - (x - 8)
                new_inc = COMPAS[DOWN]
            elif x == 7 and y < 4 and cx == 8:# A - B
                x = 4 + y
                y = 4
                new_inc = COMPAS[DOWN]
            elif x >= 12 and y < 4: # A - F
                x += 3
                y = 3-y
                new_inc = COMPAS[LEFT]
            # -------------------------- B
            elif x < 0: # B - F
                x = 12 + (y-4)
                y = 11
                new_inc = COMPAS[UP]
            elif y < 4 and x < 4: # B - A
                y = 0
                x = 8 + (3-x)
                new_inc = COMPAS[DOWN]
            elif y > 8 and x < 4: # B - E
                y = 11
                x = 11 + (3-x)
                new_inc = COMPAS[UP]

            # -------------------------- C 
            elif cy == 4 and y == 3 and x < 8: ## C - A ## valid
                y = x-4
                x = 8
                new_inc = COMPAS[RIGHT]


            # -------------------------- D 
            elif y < 8 and x >=12: # D - F ## valid
                x += (y-3)
                y = 8
                new_inc = COMPAS[DOWN]
            
            # -------------------------- E 
            elif y >= 12 and x < 12: ## E - B ## valid
                y = 7
                x = (3-(x-8))
                new_inc = COMPAS[UP]


            new_pos = [y, x]
            if coordinates[new_pos[0]][new_pos[1]] == "#":
                break
            elif coordinates[new_pos[0]][new_pos[1]] == " ":
                pass
        
            
            increment = new_inc
            c_inc = COMPAS.index(increment)
            position = new_pos
            coordinates[position[0]][position[1]] = DIRS[c_inc]
            print_coord()
        
        # print_coord()
        if rot == "R":
            c_inc = (c_inc+1) % 4
        elif rot == "L":
            c_inc = (c_inc-1) % 4

        increment = COMPAS[c_inc]


    result = 1000 * (position[0]+1) + 4 * (position[1]+1) + COMPAS.index(increment)
    print(result)

    print_coord()

    