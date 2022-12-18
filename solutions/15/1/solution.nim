import strutils
import sequtils

type
    Point* = object
        x*, y*: int

type
    Area* = object
        centre*: Point
        effect_area: int


proc mnhtn_dis*(a: Point, b: Point): int =
    return abs(a.x - b.x) + abs(a.y - b.y)


#var grid: seq[seq[char]] = @[]

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

var points: seq[Point] = @[]
for b in becon_areas:
    let p1 = Point(x: b.centre.x, y: 2000000)
    var dis = mnhtn_dis(b.centre, p1)
    if dis <= b.effect_area:
        var rm = b.effect_area - dis
        echo "free from: ", b.centre.x - rm, " - > ", b.centre.x + rm
        points.add(Point(x: b.centre.x - rm, y: b.centre.x + rm))



# # we can join these
# var lines_to_remove: seq[Point] = @[]


# for i in 0..len(points)-1:
#     for a in points:
#         if a != points[i]:
#             if a.x >= points[i].x and a.y > points[i].y and a.x <= points[i].y:
#                 points[i].y = a.y
#                 lines_to_remove.add(a)

# for l in lines_to_remove:
#     points.remove(l)
for p in points:
    echo p

# this does not give us the exact answer but we can inspet the data to see the range
# (4432766 - -518661) = 4951427
### Brute force approaches

# var count: int = 0
# var results: seq[Point] = @[]
# for i in countup(-25, 25):
    
#     let p1 = Point(x: i, y: 10)

#     for b in becon_areas:
#         var dis = mnhtn_dis(b.centre, p1)
#         echo p1, " ", dis, " ", b.effect_area
#         if dis <= b.effect_area:
#             if not (p1 in results):
#                 results.add(p1)
#                 count += 1


# var count: int = 0
# var results: seq[Point] = @[]
# for i in countup(min(xs), max(xs)):
#     if i mod 10000 == 0:
#         echo(i)
#     let p1 = Point(x: i, y: 2000000)

#     for b in becon_areas:
#         var dis = mnhtn_dis(b.centre, p1)
#         #echo p1, " ", dis, " ", b.effect_area
#         if dis <= b.effect_area:
#             if not (p1 in results):
#                 results.add(p1)
#                 count += 1
                
# echo count