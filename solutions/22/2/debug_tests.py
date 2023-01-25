## I have no idea what went wrong but I ran loads of tests, and evetually i just worked

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


def plot_border():


    corners = []
    for y in range(0, len(coordinates)-1):
        for x in range(0, len(coordinates[0])-1):
            if coordinates[y][x] == " ":
                quad = [[y-1, x+1], [y+1, x-1], [y+1, x+1], [y-1, x-1]]
                for q in quad:
                    if q[0] >= 0 and q[0] < y_size:
                        if q[1] >= 0 and q[1] < x_size:
                            if coordinates[q[0]][q[1]] == ".":
                                coordinates[y][x] = "+"
            
    print(len(corners))

#           A
#   B   C   D
#           E   F

#   A B
#   C
# D E
# F

def do_blank():
    for i in range(0, 150):
        new_pos, _ = check_boundries([i, 51], [i, 50], 0)
        coordinates[new_pos[0]][new_pos[1]] = "8"
        new_pos, _ = check_boundries([i, 98], [i, 99], 0)
        coordinates[new_pos[0]][new_pos[1]] = "8"


def fill_all():
    prev = [0, 50]
    for i in range(0, 150):
        for x in range(50, 100):
            c = [i, x]
            new_pos, _ = check_boundries(prev, c, 0)
            coordinates[new_pos[0]][new_pos[1]] = "*"
            prev = c
    
    prev = [0, 100]
    for i in range(0, 50):
        for x in range(100, 150):
            c = [i, x]
            new_pos, _ = check_boundries(prev, c, 0)
            coordinates[new_pos[0]][new_pos[1]] = "*"
            prev = c

    prev = [100, 0]
    for i in range(100, 200):
        for x in range(0, 50):
            c = [i, x]
            new_pos, _ = check_boundries(prev, c, 0)
            coordinates[new_pos[0]][new_pos[1]] = "*"
            prev = c


def do_A():
    for i in range(0, 50):
        new_pos, _ = check_boundries([i, 50], [i, 49], 0)
        coordinates[new_pos[0]][new_pos[1]] = "A"
        new_pos, _ = check_boundries([0, 50+i], [-1, 50+i], 0)
        coordinates[new_pos[0]][new_pos[1]] = "A"

def do_B():
    for i in range(0, 50):
        new_pos, _ = check_boundries([i, 149], [i, 150], 0)
        coordinates[new_pos[0]][new_pos[1]] = "B"
        new_pos, _ = check_boundries([0, 100+i], [-1, 100+i], 0) # top
        coordinates[new_pos[0]][new_pos[1]] = "B"
        new_pos, _ = check_boundries([49, 100+i], [50, 100+i], 0) # bottoms
        coordinates[new_pos[0]][new_pos[1]] = "B"

def do_C():
    for i in range(50, 100):
        new_pos, _ = check_boundries([i, 50], [i, 49], 0) # left
        coordinates[new_pos[0]][new_pos[1]] = "C"

        new_pos, _ = check_boundries([i, 99], [i, 100], 0) # right
        coordinates[new_pos[0]][new_pos[1]] = "C"

def do_D():
    for i in range(0, 50):
        new_pos, _ = check_boundries([i+100, 0], [i+100, -1], 0) # left
        coordinates[new_pos[0]][new_pos[1]] = "D"

        new_pos, _ = check_boundries([100, i], [99, i], 0) # top
        coordinates[new_pos[0]][new_pos[1]] = "D"

def do_E():
    for i in range(0, 50):
        new_pos, _ = check_boundries([i+100, 99], [i+100, 100], 0) # right
        coordinates[new_pos[0]][new_pos[1]] = "E"

        new_pos, _ = check_boundries([149, i+50], [150, i+50], 0) # bottom
        coordinates[new_pos[0]][new_pos[1]] = "E"

def do_F():
    # left, bottom right
    for i in range(0, 50):
        new_pos, _ = check_boundries([i+150, 0], [i+150, -1], 0) # left
        coordinates[new_pos[0]][new_pos[1]] = "F"

        new_pos, _ = check_boundries([199, i], [200, i], 0) # bottom
        coordinates[new_pos[0]][new_pos[1]] = "F"

        new_pos, _ = check_boundries([i+150, 49], [i+150, 50], 0) # right
        coordinates[new_pos[0]][new_pos[1]] = "F"


with open("input.txt") as f:
    grid, code = f.read().split("\n\n")

    glines = grid.split("\n")
    x_size = max([len(x) for x in glines])
    y_size = len(glines)
    print(x_size, y_size)

    line = [" " for x in range(0, x_size)]
    coordinates = [list(line) for y in range(0, y_size)]
    
    for y, row in enumerate(glines):
        # print(y, row)
        for x, c in enumerate(row):
            
            if c in ".#":
                coordinates[y][x] = c#.replace("#", ".")

    # print(coordinates)
    # plot_border()
    fill_all()
    do_A()
    do_B()
    do_C()
    do_D()
    do_E()
    do_F()
    print_coord()