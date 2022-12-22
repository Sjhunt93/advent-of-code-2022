
cubes = []

xs = set()
ys = set()
zs = set()

with open("input.txt") as f:
    lines = f.readlines()
    for l in lines:
        
        x,y,z = l.replace("\n", "").split(",")[0:3]
        print(x,y,z)
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
for z in range(0, Z_SIZE): # z is layers
    slice = []
    for y in range(0, Y_SIZE):
        row = ['.' for x in range(0, X_SIZE)]
        slice.append(row)
    grid.append(slice)


def print_2d_slices(grid):
    for zlayer in grid:
        for yrow in zlayer:
            for x in yrow:
                print(x, end=" ")
            print("")
        print("\n")

def count_faces(grid):
    faces_count = 0
    ci = 0
    for zi in range(0, Z_SIZE):
        print("\n")
        for yi in range(0, Y_SIZE):
            for xi in range(0, X_SIZE):
                
                if grid[zi][yi][xi] == "X":
                    print("cube: ", ci, " @", zi, ".", yi, ".", xi, end=" \t\t faces = ")
                    c = 0
                    ci += 1 # debug
                    # z --------
                    if zi == 0 or grid[zi-1][yi][xi] == ".":
                        c += 1
                    if zi == Z_SIZE-1 or grid[zi+1][yi][xi] == ".":
                        c += 1

                    # y --------
                    if yi == 0 or grid[zi][yi-1][xi] == ".":
                        c += 1
                    if yi == Y_SIZE-1 or grid[zi][yi+1][xi] == ".":
                        c += 1
                    
                    # x --------
                    if xi == 0 or grid[zi][yi][xi-1] == ".":
                        c += 1
                    if xi == X_SIZE-1 or grid[zi][yi][xi+1] == ".":
                        c += 1
                    print(c)
                    
                    faces_count += c
    assert ci == len(cubes)
    return faces_count                         
            
for cube in cubes:
    x, y, z = cube
    grid[z][y][x] = 'X'

print_2d_slices(grid)
print(count_faces(grid))