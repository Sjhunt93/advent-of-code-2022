



const
    NO_ENTRY = '%'
    LAST = '_'


var grid: seq[seq[char]] = @[]
var
  point: tuple[x: int, y: int]   # Tuples have *both* field names


proc readItems() =

    for line in lines("input.txt"):
        
        var larray: seq[char] = @[]
        for c in line:
            if c == 'S':
                larray.add('a')
            elif c == 'E':
                larray.add('(')
            else:
                larray.add(c)
            echo c
            
        grid.add(larray)

    for g in grid:
        echo g


readItems()
let sizeY = grid.len()
let sizeX = grid[0].len()
echo sizeX, " x ", sizeY

var item = grid[0][0]
var ascii = int(item)
echo ascii


#echo ('b' - 'a')

var progress: seq[tuple[x: int, y: int]] = @[]

var last_x = 0
var last_y = 0

progress.add((0,0))

var max = 1000000

echo "starting - ", point

var original_grid: seq[seq[char]] = grid

# proc enterStack (stack: seq[tuple[x: int, y: int]], point: tuple[x: int, y: int]): seq[tuple[x: int, y: int]] =

#     var goLeft = false
#     var goRight = false
#     var goUp = false
#     var goDown = false

#     let z = int(grid[point.y][point.x])
#     if point.x > 0:
#         goLeft = z >= (int(grid[point.y][point.x-1]) - 1) and not (grid[point.y][point.x-1] in [NO_ENTRY, LAST])
#     if point.x < sizeX-1:
#         goRight = z >= (int(grid[point.y][point.x+1]) - 1) and not (grid[point.y][point.x+1] in [NO_ENTRY, LAST])
#     if point.y > 0:
#         goUp = z >= (int(grid[point.y-1][point.x]) - 1) and not (grid[point.y-1][point.x] in [NO_ENTRY, LAST])
#     if point.y < sizeY-1:
#         goDown = z >= (int(grid[point.y+1][point.x]) - 1) and not (grid[point.y+1][point.x] in [NO_ENTRY, LAST])

#     if not (goLeft or goRight or goUp or goDown):
#         # rollback
#         echo "rollback"
#         grid[point.y][point.x] = NO_ENTRY
#         # point.x = progress[-1].x
#         # point.y = progress[-1].y
#         # discard progress.pop()
        
#         grid[point.y][point.x] = original_grid[point.y][point.x]
#         return stack
#     else:
#         grid[point.y][point.x] = LAST

#         if goLeft:
#             enterStack(stack)
#         if goRight:
#             point.x += 1
#         if goUp:
#             point.y -= 1
#         if goDown:
#             point.y += 1

#         echo goLeft, " ", goRight, " ", goUp, " ", goDown, " - ", point

#         progress.add(point)
#     if grid[point.y][point.x] == '(':
#         echo("EXITING")
#         break




while max >= 0:

    max -= 1

    var goLeft = false
    var goRight = false
    var goUp = false
    var goDown = false

    let z = int(grid[point.y][point.x])
    if point.x > 0:
        goLeft = z >= (int(grid[point.y][point.x-1]) - 1) and not (grid[point.y][point.x-1] in [NO_ENTRY, LAST])
    if point.x < sizeX-1:
        goRight = z >= (int(grid[point.y][point.x+1]) - 1) and not (grid[point.y][point.x+1] in [NO_ENTRY, LAST])
    if point.y > 0:
        goUp = z >= (int(grid[point.y-1][point.x]) - 1) and not (grid[point.y-1][point.x] in [NO_ENTRY, LAST])
    if point.y < sizeY-1:
        goDown = z >= (int(grid[point.y+1][point.x]) - 1) and not (grid[point.y+1][point.x] in [NO_ENTRY, LAST])

    if not (goLeft or goRight or goUp or goDown):
        # rollback
        echo "rollback"
        grid[point.y][point.x] = NO_ENTRY
        # point.x = progress[-1].x
        # point.y = progress[-1].y
        # discard progress.pop()
        point = progress.pop()
        grid[point.y][point.x] = original_grid[point.y][point.x]
    else:
        grid[point.y][point.x] = LAST


        if goRight:
            point.x += 1
        elif goLeft:
            point.x -= 1
        elif goUp:
            point.y -= 1
        elif goDown:
            point.y += 1

        echo goLeft, " ", goRight, " ", goUp, " ", goDown, " - ", point

        progress.add(point)
    if grid[point.y][point.x] == '(':
        echo("EXITING")
        break

    
    
echo(progress, " --> ", len(progress))

# for g in grid:
#     echo(g)
