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

def print_blizzard(add_e=True):
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

#with open("input.txt") as f:
with open("test.txt") as f:
    lines = f.read().split("\n")
    ysize = len(lines)-2
    xsize = len(lines[0])-2
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            print(c)
            if c in "><^v":
                w = [x-1, y-1] + dir_map[c] + [c]
                blizzards.append(w)


# print_blizzard()
# cycle()
# print_blizzard()
# exit()
# for i in range(0, 3):
#     cycle()
#     print(blizzards)



elf = [0, -1]
exit = [xsize-1, ysize]
print(exit)

positions = [[1,0], [-1, 0], [0, 1], [0, -1]]

#while not is_free(elf[0], elf[1], blizzards):
# cycle()
# print_blizzard()
# while not is_free(0, 0, blizzards):
#     cycle()
#     print_blizzard()

# cycle()
# blizzards_time = [deepcopy(blizzards)]

blizzards_time = [[]]
visitedSet = set()

print_blizzard()
while elf != exit:

    queue = []
    visitedSet.add(tuple(elf))
    queue.append([elf, 1])

    while queue:
        elf, time = queue[0]
        queue = queue[1:]
        if elf == exit:
            break
        
        # print(time, len(blizzards_time))
        if time >= len(blizzards_time):
            if time > 5:
                blizzards_time[time-5] = []    
            print("Cycling a step", len(blizzards_time), elf)
            cycle()
            # print_blizzard()
            blizzards_time.append(deepcopy(blizzards))

        valid_ps =  [[elf[0] + p[0], elf[1] + p[1]] for p in positions]
        
        did_move = False
        for p in valid_ps:
            # print(p, time)
            if p == exit:
                print("Finished", time+2)
                assert False
            # need to check here... (is size valid or no)
            if p[0] >= 0 and p[0] < xsize and p[1] >=0 and p[1] < ysize:
                # if tuple(p) not in visitedSet or p == elf:
                    if is_free(p[0], p[1], blizzards_time[time]):
                        
                        # visitedSet.add(tuple(p))
                        if [p, time+1] not in queue:
                            queue.append([p, time+1])
                            did_move = True
                    else:
                        # print("Cannot go")
                        pass

        if not did_move:
            if [elf, time+1] not in queue:
                queue.append([elf, time+1])
                    
    assert False
    



# def bfs(points, vertex):
#     visitedSet = set()
#     plot_path = []
#     queue = []
#     visitedSet.add(vertex)
#     plot_path.append(vertex)
#     queue.append([vertex, 0])
    
#     result = []
#     while queue:
#         v, d = queue[0]
#         result.append(v)
#         queue = queue[1:]
#         #print(result)

#         if array_of_vals[v] == 26:
#             print("SUCSESS", "~", len(plot_path), len(visitedSet))
#             print("d is: ", d)
#             return d

#         for neighbor in points[v]:
#             #print("iter", neighbor, v)
#             c = array_of_vals[v]
#             #print(c)
#             n = array_of_vals[neighbor]
#             #print(chr(n+97))

            
            
#             if c >= n - 1:
#             #if n - c >= 1:
#                 if neighbor not in visitedSet:
#                     visitedSet.add(neighbor)
#                     queue.append([neighbor, d+1])
