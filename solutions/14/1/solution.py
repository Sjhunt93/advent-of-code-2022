

xs = set()
ys = set()

rocks = []

#with open("test.txt") as f:
with open("input.txt") as f:

    lines = f.readlines()
    for l in lines:
        #print(l)
        coords = l.replace("\n", "").split("->")
        print(coords)
        rocks.append(coords)
        for c in coords:
            x, y = c.split(",")
            xs.add(int(x))
            ys.add(int(y))

print(min(xs), " -- ", max(xs))
print(min(ys), " -- ", max(ys))

grid = []

for rows in range(0, max(ys)+1):
    grid.append(["." for x in range(min(xs), max(xs)+1)])


Y_OFFSET = 0 # not used but could be
X_OFFSET = min(xs)

for todraw in rocks:
    for cindex in range(1, len(todraw)):
        prev = todraw[cindex-1]
        current = todraw[cindex]
        x1, y1 = [int(c) for c in prev.split(",")]
        x2, y2 = [int(c) for c in current.split(",")]
        #print(x1, "->", x2, " . ", y1, "->", y2, type(x1))
        
        if abs(x1-x2) == 0: # draw vertical rocks
            for y in range(min([y1, y2]), max([y1, y2])+1):
                grid[y-Y_OFFSET][x1-X_OFFSET] = "#"
        if abs(y1-y2) == 0: # draw horizontal rocks
            for x in range(min([x1, x2]), max([x1, x2])+1):
                grid[y1-Y_OFFSET][x-X_OFFSET] = "#"

def debug_print():
    for row in grid:
        for c in row:
            print(c, end="")
        print("")

#debug_print()

sand_castles = 0

for i in range(0, 500000):
    sand_x = 500
    sand_y = 0
    try:
        while True:
            if grid[sand_y+1][sand_x-X_OFFSET] == ".":
                sand_y += 1
            elif grid[sand_y+1][(sand_x-X_OFFSET)-1] == ".":
                sand_y += 1
                sand_x -= 1
            elif grid[sand_y+1][(sand_x-X_OFFSET)+1] == ".":
                sand_y += 1
                sand_x += 1
            else:
                grid[sand_y][sand_x-X_OFFSET] = "o"
                sand_castles += 1
                break
    # bit lazy but meh
    except Exception as e:
        debug_print()
        print(sand_castles)
        break

    


