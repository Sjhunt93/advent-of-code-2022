
cubes = []

xs = set()
ys = set()
zs = set()

#with open("test.txt") as f:
with open("input.txt") as f:
    lines = f.readlines()
    for l in lines:
        
        x,y,z = l.replace("\n", "").split(",")[0:3]
        
        xs.add(int(x))
        ys.add(int(y))
        zs.add(int(z))
        cubes.append([int(x), int(y), int(z)])


print(min(xs), " ~ ", max(xs))
print(min(ys), " ~ ", max(ys))
print(min(zs), " ~ ", max(zs))

X_SIZE = max(xs)+1
Y_SIZE = max(ys)+1
Z_SIZE = max(zs)+1



grid = []
for z in range(0, Z_SIZE+1): # z is layers
    slice = []
    for y in range(0, Y_SIZE):
        row = ['.' for x in range(0, X_SIZE)]
        slice.append(row)
    grid.append(slice)

for cube in cubes:
    x, y, z = cube
    grid[z][y][x] = 'X'


def print_2d_slices(grid):
    for zlayer in grid:
        for yrow in zlayer:
            for x in yrow:
                print(x, end=" ")
            print("")
        print("\n")


def count_faces_or_air(grid):
    faces_count = 0
    
    barrier = " "
    for zi in range(0, Z_SIZE):
        
        for yi in range(0, Y_SIZE):
            for xi in range(0, X_SIZE):
                
                if grid[zi][yi][xi] == "X":
                    #print("cube: " " @", zi, ".", yi, ".", xi, end=" \t\t faces = ")
                    c = 0
                    
                    # z --------
                    if zi == 0 or grid[zi-1][yi][xi] == barrier:
                        c += 1
                    if zi == Z_SIZE-1 or grid[zi+1][yi][xi] == barrier:
                        c += 1

                    # y --------
                    if yi == 0 or grid[zi][yi-1][xi] == barrier:
                        c += 1
                    if yi == Y_SIZE-1 or grid[zi][yi+1][xi] == barrier:
                        c += 1
                    
                    # x --------
                    if xi == 0 or grid[zi][yi][xi-1] == barrier:
                        c += 1
                    if xi == X_SIZE-1 or grid[zi][yi][xi+1] == barrier:
                        c += 1


                    faces_count += c

    return faces_count                         


def fill_with_lava_up(grid):
    # flood bottom
    for zi in range(0, Z_SIZE):
        for yi in range(0, Y_SIZE):
            for xi in range(0, X_SIZE):
                if zi == 0:
                    grid[zi][yi][xi] = grid[zi][yi][xi].replace(".", " ")
                elif grid[zi][yi][xi] != "X":
                    if grid[zi-1][yi][xi] == " ": # or (grid[zi][yi][xi] == "." and grid[zi-1][yi][xi] == "X"):
                        grid[zi][yi][xi] = grid[zi][yi][xi].replace(".", " ")

def fill_with_lava_down(grid):
    grid.reverse()
    fill_with_lava_up(grid)
    grid.reverse()

def fill_wth_lava_side(grid):
    did_fill = False
    for zi in range(0, Z_SIZE):
        for yi in range(0, Y_SIZE):
            for xi in range(0, X_SIZE):
                fill = False
                if grid[zi][yi][xi] == ".":
                    if yi != 0:
                        if grid[zi][yi-1][xi] == " ":
                            fill = True
                    if yi != Y_SIZE-1:
                        if grid[zi][yi+1][xi] == " ":
                            fill = True
                    if xi != 0:
                        if grid[zi][yi][xi-1] == " ":
                            fill = True
                    if xi != X_SIZE-1:
                        if grid[zi][yi][xi+1] == " ":
                            fill = True
                    
                    if fill:
                        grid[zi][yi][xi] = grid[zi][yi][xi].replace(".", " ")
                        did_fill = True
    return did_fill



#print_2d_slices(grid)

# flood from both directions

fill_with_lava_up(grid)
fill_with_lava_down(grid)
# allow the sides to fill in the remaining gaps (this needs to run a few times)
while fill_wth_lava_side(grid):
    continue

#print_2d_slices(grid)

faces = count_faces_or_air(grid)
print(faces)
