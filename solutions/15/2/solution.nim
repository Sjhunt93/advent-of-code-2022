import strutils
import sequtils

type
    Point* = object
        x*, y*: int

const null_point = Point(x: 2147483647, y: 2147483647)

proc any_items_overlap(points: seq[Point]): tuple[a: Point, b: Point] =

    for a in points:
        for b in points:
            # echo a, " ### ", b
            if a.x == b.x and a.y == b.y:
                # echo "A-b EQULA"
                continue
            # |x----A----y|     |x-------B------y|
            if b.x > a.y or a.x > b.y:
                # no overlap so ignore this pair
                #echo "no overlap"
                continue

            else:  # One of the combinations overlaps, so return them
                return (a, b)

    return (null_point, null_point)

type
    Area* = object
        centre*: Point
        effect_area: int

proc `==`(a, b: Point): bool =
    return (a.x == b.x and b.y == b.y)

proc mnhtn_dis*(a: Point, b: Point): int =
    return abs(a.x - b.x) + abs(a.y - b.y)


var becon_areas: seq[Area] = @[]

var xs: seq[int] = @[]
var ys: seq[int] = @[]

proc readItems() =

    #for line in lines("test.txt"):
    for line in lines("input.txt"):
        #echo line
        var numbers = line.split({'=', ',', ':'})
        echo numbers
        var sensor_x = parseInt(numbers[1])
        var sensor_y = parseInt(numbers[3])
        var becon_x = parseInt(numbers[5])
        var becon_y = parseInt(numbers[7])
        echo sensor_x, "~", sensor_y
        echo becon_x, "~", becon_y

        let p1 = Point(x: sensor_x, y: sensor_y)
        let p2 = Point(x: becon_x, y: becon_y)
        echo mnhtn_dis(p1, p2)

        let area = Area(centre: p1, effect_area: mnhtn_dis(p1, p2))
        becon_areas.add(area)

        xs.add(sensor_x)
        xs.add(becon_x)

        ys.add(sensor_y)
        ys.add(becon_y)


readItems()

# var minx = minIndex(xs)
# var maxx = minIndex(xs)
# echo minx, max

echo min(xs), " ~ ", max(xs)

# this is a preety novel solution and takes advtange of the manhattan distance


for y in 0..4000000:

    var points: seq[Point] = @[]
    for b in becon_areas:
        let p1 = Point(x: b.centre.x, y: y)#2000000)
        var dis = mnhtn_dis(b.centre, p1)
        if dis <= b.effect_area:
            var rm = b.effect_area - dis
            #echo "free from: ", b.centre.x - rm, " - > ", b.centre.x + rm
            points.add(Point(x: b.centre.x - rm, y: b.centre.x + rm))

    while true:
        if any_items_overlap(points) == (null_point, null_point):
            # No items overlapped - break the loop and finish
            break

        else:  # There are still overlaps
            var items = any_items_overlap(points)
            #echo " OVERLAP", items    

            # Remove the items from the main list
            points.delete(points.find(items.a))
            points.delete(points.find(items.b))


            var n = Point(x: min(items.a.x, items.b.x), y: max(items.a.y, items.b.y))
            #echo "NEW: ", n
            points.add(n) 
            #echo points
    if len(points) != 1:
        echo "DONE IT"
        echo points, " ~ ", y
        break
        
    

# 3257428 * 4000000 + 2573243

