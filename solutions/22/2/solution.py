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

with open("input.txt") as f:
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
        print(steps, rot)
        while steps:
            
            new_pos = [(position[0] + increment[0]), (position[1] + increment[1])]
            
            steps -= 1
            cy, cx = position
            y, x = new_pos
            new_inc = increment


            # -------------------------- A
            if y < 0 and x < 100: ## A - F
                y = (x - 50) + 150
                x = 0
                new_inc = COMPAS[RIGHT]
                print("AF")

            elif x == 49 and y < 50: ## A - D
                y = 100 + (49-y)
                x = 0    
                new_inc = COMPAS[RIGHT]
                print("AD")
            # AC and AB
            # -------------------------- B
            elif y < 0 and x < 150: ## B - F
                y = 199
                x = x-100
                new_inc = COMPAS[UP]
                #print("AD")
            elif y == 50 and x >= 100: ## B - C
                y = (x - 100) + 50
                x = 99
                new_inc = COMPAS[LEFT]
            elif x == 150: ## B - E
                y = (49-y) + 100
                x = 99
                new_inc = COMPAS[LEFT]
            # BA
            # -------------------------- C
            elif x == 49 and y < 100: ## C - D
                x = y - 50
                y = 100
                new_inc = COMPAS[DOWN]
            elif y < 100 and x == 100: ## C - B
                x = (y - 50) + 100
                y = 49
                new_inc = COMPAS[UP]
            # CE CA
            # -------------------------- D
            elif x < 50 and y == 99: ## D - C
                y = 50+x
                x = 50
                new_inc = COMPAS[RIGHT]

            elif x < 0 and y < 150: ## D - A
                y = 49-(y-100)
                x = 50
                new_inc = COMPAS[RIGHT]
            # DE DF
            # -------------------------- E
            elif x == 100 and y < 150: ## E - B
                y = 49-(y-100)
                x = 149
                new_inc = COMPAS[LEFT]
            elif y == 150 and x >= 50: ## E - F
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

            elif x == 50 and y >= 150: ## F - E
                x = (y - 150) + 50
                y = 149
                new_inc = COMPAS[UP]





            new_pos = [y, x]
            try:
                if coordinates[new_pos[0]][new_pos[1]] == "#":
                    break
                elif coordinates[new_pos[0]][new_pos[1]] == " ":
                    assert False
            except:
                print(new_pos, " from ",  position)
                coordinates[new_pos[0]][new_pos[1]] = "@"
                coordinates[position[0]][position[1]] = "@"

                print_coord()
                print(new_pos)
                raise Exception()
        
            
            increment = new_inc
            c_inc = COMPAS.index(increment)
            position = new_pos
            coordinates[position[0]][position[1]] = DIRS[c_inc]
            #print_coord()
        
        #print_coord()
        if rot == "R":
            c_inc = (c_inc+1) % 4
        elif rot == "L":
            c_inc = (c_inc-1) % 4

        increment = COMPAS[c_inc]


    result = 1000 * (position[0]+1) + 4 * (position[1]+1) + COMPAS.index(increment)
    print(result)

#print_coord()

    