import re


ORE = 0
CLAY = 1
OBSDIAN = 2
GEODE = 3

class Robot:
    
    
    def __init__(self, ore_cost, clay_cost, obs_cost, rtype) -> None:
        self.ore_cost = int(ore_cost)
        self.clay_cost = int(clay_cost)
        self.obs_cost = int(obs_cost)
        self.rtype = int(rtype)

    def inc_resources(self, resources):
        resources[self.rtype] += 1

    def can_build(self, resources):
        can_build = resources[ORE] >= self.ore_cost \
            and resources[CLAY] >= self.clay_cost \
            and resources[OBSDIAN] >= self.obs_cost

        return can_build


    # def 
    # def can_make(rbt: object):


def expand(robots: list, resources: list):

    # work out what robots we can build

    pass


#
MAX_TIME = 32

c = 0
## addasdjaisjdkajskdjaklsdjklaj

cache = {}
best = {}

o = [ ( t - 1 ) * t // 2 for t in range( 32 + 1 ) ]


def get_max(time: int, resources: list, robots: list, max_resources: list, costs_to_build: list, new_robot: int, max_geodes: int): #max_resources
    global c
    c += 1
    
    global cache
    global best

    # kkk = [*resources, *robots]
    # s = 0
    # for i, k in enumerate(kkk):
    #     s += k << i

    # assert s < 256
    #key = (time << 13) | ((new_robot+1) << 9) | s
    key = tuple([*resources, *robots, time, new_robot])
    
    if key in cache:
        return cache[key]

    if time not in best:
        best[time] = 0

        #geodes collected + geode robots * time remaining + T(time remaining) <= best total geodes found so far.

    # RULES
    # 1. Always build OBSDIAN robots
    # 2. stop building a robot once we max that resource type

    mg = 0

    for i in range(0, 4):
        resources[i] += robots[i]

    

    if time == MAX_TIME:
        return resources[GEODE]

    if resources[GEODE] > best[time]:
        best[time] = resources[GEODE]
    else:
        tremaing = (MAX_TIME-time)
        if (resources[GEODE] + (robots[GEODE] * tremaing) + o[tremaing]) <= best[time] and best[time] != 0:
            return 0    

    # lay over from last turn
    if new_robot != -1:
        robots[new_robot] += 1

    for robot_type in range(0, 4):
        # have we gathered enough resources
        if resources[robot_type] > max_resources[robot_type] and robot_type != GEODE:
            continue

        can_build = True
        for i in range(0, GEODE):
            if resources[i] < costs_to_build[robot_type][i] and costs_to_build[robot_type][i] != 0:
                can_build = False
                break

        if can_build:
            # if robot_type == GEODE:
            #     #print("building geode")
            
            rb = robots.copy()
            #rb[robot_type] += 1
            rc = resources.copy()
            for i in range(0, 3):
                rc[i] -= costs_to_build[robot_type][i]
            mg = max(mg, get_max(time=time+1, resources=rc, robots=rb, max_resources=max_resources, costs_to_build=costs_to_build, new_robot=robot_type, max_geodes=max_geodes))

    
    mg = max(mg, get_max(time+1, resources.copy(), robots.copy(), max_resources, costs_to_build, -1, max_geodes))

    cache[key] = mg

    return mg
    # option 1 - do nothing
    # options 2-5
        # -> 

print(o)
with open("test.txt") as f:
    lines = f.read().split("\n")
    score = 0
    for i, l in enumerate(lines[0:3]):
        if "Blueprint" in l:
            
            cache = {}
            best = {}
            robot = {}
            a = l.split(":")[1].split(".")
            
            a = re.findall("\d+", l)
            blueprint = a[0]
            costs_to_build = [ 
                [int(a[1]), 0, 0],
                [int(a[2]), 0, 0],
                [int(a[3]), int(a[4]), 0],
                [int(a[5]), 0, int(a[6])],
            ]

            #maxes 4 14 7
            
            max_ore = max( [r[0] for r in costs_to_build])
            max_clay = max( [r[1] for r in costs_to_build])
            max_obsdian = max( [r[2] for r in costs_to_build])

            
            
            max_resources = [max_ore, max_clay, max_obsdian, 99999]
            resources = [0,0,0,0]
            robots = [1, 0, 0, 0]
            
            m = get_max(1, resources, robots, max_resources, costs_to_build, -1, 0)
            print("Max geodes after time: ", MAX_TIME, " -> ", m, " geodes \t .......", c)
            score += int(blueprint)*m

    print(score)