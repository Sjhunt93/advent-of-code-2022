from copy import deepcopy

#x, y, xinc, yinc
#wind = [0,0,0,0]
blizzards = []

xsize = 0
ysize = 0

dir_map = {">" : [1, 0], "<" : [-1, 0], "^" : [0, -1], "v" : [0, 1]}

def cycle():
    for b in blizzards:
        b[0] = (b[0] + b[2]) % xsize
        b[1] = (b[1] + b[3]) % ysize

def is_free(x, y, blizzard_step):
    for b in blizzard_step:
        if b[0] == x and b[1] == y:
            return False
    return True

def print_blizzard(elf, add_e=True):
    map = []
    
    for y in range(0, ysize):
        map.append(["." for x in range(0, xsize)])
    

    for b in blizzards:
        if map[b[1]][b[0]] != ".":
            map[b[1]][b[0]] = "2"
        else:    
            map[b[1]][b[0]] = b[4]

    if add_e:
        map[elf[1]][elf[0]] = "E"
    for y in map:
        for x in y:
            print(x, end="")
        print("")
    
    print("\n")

with open("input.txt") as f:
#with open("test.txt") as f:
    lines = f.read().split("\n")
    ysize = len(lines)-2
    xsize = len(lines[0])-2
    for y, l in enumerate(lines):
        
        for x, c in enumerate(l):    
            if c in "><^v":
                w = [x-1, y-1] + dir_map[c] + [c]
                blizzards.append(w)
            elif c in "#.":
                pass
            else:
                assert False


blizzard_paths = []
blizzard_paths.append(deepcopy(blizzards))


cycle()

while blizzards != blizzard_paths[0]:
    blizzard_paths.append(deepcopy(blizzards))
    cycle()


print(len(blizzard_paths))

elf = [0, -1]
exit = [xsize-1, ysize]



def steps_between(start, end, time=0):

    visitedSet = set()

    queue = []
    visitedSet.add(tuple(start + [1]))
    queue.append([start, time])

    while queue:
        current, time = queue[0]
        queue = queue[1:]
#        print(time)

        # print(time)
        valid_ps =  [[current[0] + p[0], current[1] + p[1]] for p in [[1,0], [-1, 0], [0, 1], [0, -1], [0, 0]]]
        
        # did_move = False
        for p in valid_ps:
            if p == end:
                print("Finished", time)
                return time
            
            if tuple(p + [time]) in visitedSet:
                continue

            if (p[0] < 0 or p[0] >= xsize or p[1]  < 0 or p[1] >= ysize) and p != start:
                continue

            
            if is_free(p[0], p[1], blizzard_paths[time % len(blizzard_paths)]):
                
                # print("elf can move to ", p, "at time", time)
                visitedSet.add(tuple(p + [time]))
                queue.append([deepcopy(p), time+1])
                    
    assert False
    
v1 = steps_between([0, -1], [xsize-1, ysize])
print("1st trip", v1)


v2 = steps_between([xsize-1, ysize], [0, -1], v1)
print("2nd trip", v2-v1)


v3 = steps_between([0, -1], [xsize-1, ysize], v2)
print("2nd trip", v3-v2)

