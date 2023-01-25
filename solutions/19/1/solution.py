import re

class Robot:
    
    
    def __init__(self, ore_cost, clay_cost, obs_cost, rtype) -> None:
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obs_cost = obs_cost
        self.rtype = rtype

    def inc_resources(self, resources):
        resources[self.rtype] += 1

    # def 
    # def can_make(rbt: object):


def expand(robots: list, resources: list):

    # work out what robots we can build

    pass


with open("test.txt") as f:
    lines = f.read().split("\n")
    for i, l in enumerate(lines):
        if "Blueprint" in l:
            robot = {}
            a = l.split(":")[1].split(".")
            print(a)
            a = re.findall("\d+", l)
            blueprint = a[0]

            
            ore_rbt = Robot(a[1], 0, 0, 0)
            clay_rbt = Robot(0, a[2], 0, 1)
            obsdian_rbt = Robot(a[3], a[4], 0, 2)
            geode_rbt = Robot(a[5], 0, a[6], 3)
            
            robots = [ore_rbt]
            resources = [0,0,0,0]
            count = 24
            while count:
                for r in robots:
                    r.inc_resources(resources)
                count -= 1

            print(resources)
            # robot.
            # print(lines[i+1], a)
        

class State:
    def __init__(self) -> None:
        pass