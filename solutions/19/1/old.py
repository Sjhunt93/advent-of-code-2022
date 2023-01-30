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
    def consume_resources(self, resouces):
        resources[ORE] -= self.ore_cost
        resources[CLAY] >= self.clay_cost
        resources[OBSDIAN] >= self.obs_cost
    # def 
    # def can_make(rbt: object):


def expand(robots: list, resources: list):

    # work out what robots we can build

    pass


#
c = 0
## addasdjaisjdkajskdjaklsdjklaj
def get_max(time, resources, robots, max_g, unbuilt_robots, max_resources): #max_resources
    global c
    c += 1
    

    # RULES
    # 1. Always build OBSDIAN robots
    # 2. stop building a robot once we max that resource type

    mo = max_g

    if time == 0:
        return resources[GEODE]

    tts = [0, 0, 0, 0]
    for r in robots:
        r.inc_resources(resources)
        tts[r.rtype] += 1

    
    for unrobot in unbuilt_robots[::-1]:
        # print(unrobot.rtype, unrobot.can_build(resources))
        # if time == 5 and unrobot.rtype == CLAY:
        #     pass
        if unrobot.can_build(resources):
            if tts[unrobot.rtype] < max_resources[unrobot.rtype] or unrobot.rtype == GEODE: #
                unrobot.consume_resources(resources)
                mo = max(mo, get_max(time-1, list(resources), list(robots + [unrobot]), max_g, unbuilt_robots, max_resources))
                
    mo = max(mo, get_max(time-1, list(resources), list(robots), max_g, unbuilt_robots, max_resources))

    return mo
    # option 1 - do nothing
    # options 2-5
        # -> 

with open("test.txt") as f:
    lines = f.read().split("\n")
    for i, l in enumerate(lines[:1]):
        if "Blueprint" in l:
            robot = {}
            a = l.split(":")[1].split(".")
            print(a)
            a = re.findall("\d+", l)
            blueprint = a[0]

            
            ore_rbt = Robot(a[1], 0, 0, 0)
            clay_rbt = Robot(a[2], 0, 0, 1)
            obsdian_rbt = Robot(a[3], a[4], 0, 2)
            geode_rbt = Robot(a[5], 0, a[6], 3)
            
            
            unbuilt_robots = [ore_rbt, clay_rbt, obsdian_rbt, geode_rbt]
            
            max_ore = max( [r.ore_cost for r in unbuilt_robots])
            max_clay = max( [r.clay_cost for r in unbuilt_robots])
            max_obsdian = max( [r.obs_cost for r in unbuilt_robots])

            print("maxes", max_ore, max_clay, max_obsdian)
            
            max_resources = [max_ore, max_clay, max_obsdian, 99999]
            resources = [0,0,0,0]



            robots = [ore_rbt]
            resources = [0,0,0,0]
            print("Obs", get_max(16, resources, robots, 0, unbuilt_robots, max_resources), c)
            # count = 24
            # while count:
            #     for r in robots:
            #         r.inc_resources(resources)
            #     count -= 1

            # print(resources)
            # robot.
            # print(lines[i+1], a)
        

class State:
    def __init__(self) -> None:
        pass