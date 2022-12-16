
map = []
array_of_vals = []

def solve_with_recusion(points_visted, map, px, py) -> bool:

    if [px, py] in points_visted:
        return False
    points_visted.append([px, py])
    if map[py][px] == 'S':
        return True

    if py < len(map): 
        if map[py][px] - map[py-1][px] >= 1:
            return solve_with_recusion(points_visted, map, px, py-1)


    # if we hit a limit.

    points_visted.pop([px, py])

def height_map(c):
    if c == "S":
        return 0
    elif c == "E":
        return 26
    else:
        return (ord(c)-97)+1


#with open("solutions/12/1/input.txt") as f:
starting_point = 0
with open("input.txt") as f:

    lines  = f.readlines()
    for l in lines:
        l = l.replace("\n", "")
        vals = [height_map(c) for c in l]
        print(vals)

        map.append(vals)
        for a in map[-1]:
            array_of_vals.append(a)
    

    # assert 0 in array_of_vals
    # assert 26 in array_of_vals
    # starting_point = array_of_vals.index(0)
    # array_of_vals[starting_point] = 99

#print(map)
print(array_of_vals)
def generate_points(map):
    y_size = len(map)
    x_size = len(map[0])
    print(y_size, x_size)
    points = {}

    for y in range(0, y_size):
        for x in range(0, x_size):
            
            r = []
            key = x + (y * x_size)
            if x > 0:
                r.append((x-1) + (y * x_size))
            if x < x_size-1:
                r.append((x+1) + (y * x_size))
            if y > 0:
                r.append(x + ((y-1) * x_size))
            if y < y_size-1:
                r.append(x + ((y+1) * x_size))
            
            if r:
                points[key] = r
    return points


#https://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python

def bfs(points, vertex):
    visitedSet = set()
    plot_path = []
    queue = []
    visitedSet.add(vertex)
    plot_path.append(vertex)
    queue.append([vertex, 0])
    
    result = []
    while queue:
        v, d = queue[0]
        result.append(v)
        queue = queue[1:]
        #print(result)

        if array_of_vals[v] == 26:
            print("SUCSESS", "~", len(plot_path), len(visitedSet))
            print("d is: ", d)
            return d

        for neighbor in points[v]:
            #print("iter", neighbor, v)
            c = array_of_vals[v]
            #print(c)
            n = array_of_vals[neighbor]
            #print(chr(n+97))

            
            
            if c >= n - 1:
            #if n - c >= 1:
                if neighbor not in visitedSet:
                    visitedSet.add(neighbor)
                    queue.append([neighbor, d+1])
            
    return 99999999

# results = []
# points = generate_points(map)
# for i, a in enumerate(array_of_vals):
#     if a == 0:
#         res = bfs(points, i)
#         if res != 99999999:
#             results.append(res)
# print(results, min(results))


# points_visited = []
# queue = []
# def bfs(map, startingpoint):


# current_point = [0, 0]


# points = generate_points(map)
# res = bfs(points, 0)
# print(len(res))
def bfs_2(points, vertex):
    visitedSet = set()
    queue = []
    #visitedSet.add(vertex)
    for i, a in enumerate(array_of_vals):
        if a == 1 or a == 0:
            queue.append([i, 0])
            visitedSet.add(i)
    
    result = []
    print(len(queue))
    while queue:
        
        v, d = queue[0]
        result.append(v)
        queue = queue[1:]

        # if v not in visitedSet:
        #     continue


        if array_of_vals[v] == 26:
            print("SUCSESS", "~", len(visitedSet))
            print("d is: ", d)
            return result
        
        for neighbor in points[v]:
            c = array_of_vals[v]            
            n = array_of_vals[neighbor]
            
            if c >= n - 1:
                if neighbor not in visitedSet:
                    visitedSet.add(neighbor)
                    queue.append([neighbor, d+1])
                    
                    

    return result

points = generate_points(map)
res = bfs_2(points, 0)
print(len(res))