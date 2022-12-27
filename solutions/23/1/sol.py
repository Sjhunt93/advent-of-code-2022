
def is_elf_in_position_optimised(x, y, elves):
    for e in elves:
        if x == e.x and y == e.y:
            return True, e
    
    return False, e

def is_elf_in_position(x, y, elves):
    for e in elves:
        if x == e.x and y == e.y:
            return True
    
    return False

# we just check here
next_positions = []

order = ["north", "south", "west", "east"]


class Elf:
    x = 0
    y = 0
    
    nx = 0
    ny = 0
    next = ""

    # cordinates = {
    #     "north" : {"x" :}
    # }



    def move(elf, elves, order):

        elf.next = ""
        elf.nx = elf.x
        elf.ny = elf.y

        c = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                if not is_elf_in_position(elf.x + x, elf.y + y, elves):
                    c += 1
                else:
                    break
        if c == 8:
            return

        for dir in order:
            if dir == "north" or dir == "south":
                yinc = -1 if dir == "north" else 1
                blocked = is_elf_in_position(elf.x-1, elf.y+yinc, elves) or is_elf_in_position(elf.x, elf.y+yinc, elves) or is_elf_in_position(elf.x+1, elf.y+yinc, elves)
                if not blocked:
                    elf.ny = elf.y + yinc
                    elf.nx = elf.x
                    elf.next = dir
                    break

            if dir == "east" or dir == "west":
                xinc = 1 if dir == "east" else -1
                blocked = is_elf_in_position(elf.x+xinc, elf.y-1, elves) or is_elf_in_position(elf.x+xinc, elf.y, elves) or is_elf_in_position(elf.x+xinc, elf.y+1, elves)
                if not blocked:
                    elf.ny = elf.y
                    elf.nx = elf.x + xinc
                    elf.next = dir
                    break
        # print(elf.order)
        # print("elf is moving: ", elf.next)

    
    # def rotate(elf):
    #     # if elf.next:
            
    #     #     i = elf.order.index(elf.next)
    #     #     # rotate order
    #     #     elf.order = [elf.order[(i+1) % 4], elf.order[(i+2) % 4], elf.order[(i+3) % 4], elf.next ]
    #     #     print(elf.order)        
    #     a = elf.order.pop(0)
    #     elf.order.append(a)
    #     print(elf)
    

elves = []

grid = []
x_width = 0
y_height = 0

def read(x, y):
    return grid[x + y * x_width]
def write(x, y, val):
    grid[x + y * x_width] = val

positions_to_move = []

with open("input.txt") as f:
# with open("test2.txt") as f:
    lines = f.readlines()
    y_height = len(lines)
    x_width = len(lines[0])-1
    grid = ["." for i in range(0,x_width * y_height)]
    for y, l in enumerate(lines):
        l = l.replace("\n", "")
        for x, val in enumerate(l):
            
            if val == "#":
                e = Elf()
                e.x = x
                e.y = y
                elves.append(e)



# for i in range(0, 10):
#     e = Elf()
#     e.x = i
#     elves.append(e)

# elves[3].x = 1000

for round in range(0, 1000):
    print(round)
    for e in elves:
        # print(e.x, " ~ ", e.y)
        Elf.move(e, elves, order)
        if e.next:
            next_positions.append([e.nx, e.ny])

    for e in elves:
        if next_positions.count([e.nx, e.ny]) == 1:
            e.x = e.nx
            e.y = e.ny
        # Elf.rotate(e)
        # print(e.x, " ~ ", e.y)

    a = order.pop(0)
    order.append(a)
    print("\t", len(next_positions))
    if len(next_positions) == 0:
        break
    next_positions = []
    # for e in elves:
    #     write(e.x, e.y, "#")


    # for y in range(0, y_height):
    #     for x in range(0, x_width):
    #         print(read(x, y), end="")
    #         write(x, y, ".")
    #     print()
    # print("\n")
# print(elfs)

xs = []
ys = []

for e in elves:
    xs.append(e.x)
    ys.append(e.y)

xmin = min(xs)
xmax = max(xs)
ymin = min(ys)
ymax = max(ys)

grid = []
for y in range(ymin, ymax+1):
    line = ["." for x in range(xmin, xmax+1)]
    grid.append(line)

for e in elves:
    grid[e.y-ymin][e.x-xmin] = "#"

for y in grid:
    for x in y:
        print(x, end="")
    print("")



print(sum([g.count(".") for g in grid]))



