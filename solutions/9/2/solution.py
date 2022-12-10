from copy import copy

class Point:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
    def __str__(self) -> str:
        return str(self.x) + "-" + str(self.y)
    def __repr__(self):
        return str(self.x) + "-" + str(self.y)

def move__tail_to_head(head, tail):
    xdif = head.x - tail.x
    ydif = head.y - tail.y
    
    #print("IN diff: ", xdif, " -- ", ydif,  " ## ", abs(xdif), " ", abs(ydif))
    assert abs(xdif <= 2)
    assert abs(ydif <= 2)
    # x and y only
    if abs(xdif) == 2 and abs(ydif) == 0:
        tail.x += int(xdif / 2)
    elif abs(ydif) == 2 and abs(xdif) == 0:
        tail.y += int(ydif / 2)
    elif abs(ydif) == 2 and abs(xdif) == 1:
        tail.y += int(ydif / 2)
        tail.x += xdif
    elif abs(xdif) == 2 and abs(ydif) == 1:
        tail.x += int(xdif / 2)
        tail.y += ydif
    elif abs(xdif) == 2 and abs(ydif) == 2:
        tail.x += int(xdif / 2)
        tail.y += int(ydif / 2)


    xdif = head.x - tail.x
    ydif = head.y - tail.y
    
    assert abs(xdif <= 1)
    assert abs(ydif <= 1)

def iterate_rope(rope):
    for i in range(1, len(rope)):
        move__tail_to_head(rope[i-1], rope[i])
    return rope




rope = [Point() for x in range(0,10)]
positions = []


# this was my first idea 
def swap_tails(rope):
    rope = [rope[0]] + [rope[9]] + rope[1:9]
    return rope

#with open("test.txt") as f:
with open("input.txt") as f:
    lines = f.readlines()
    for l in lines:
        d, amount = l.split(" ")
        amount = int(amount)
        print(d, amount)
        
        if d == "L":
            for i in range(0, amount):
                rope[0].x -= 1
                rope = iterate_rope(rope)
                positions.append([rope[9].x, rope[9].y])

        elif d == "R":
            for i in range(0, amount):
                rope[0].x += 1
                rope = iterate_rope(rope)
                positions.append([rope[9].x, rope[9].y])

        elif d == "U":
            for i in range(0, amount):
                rope[0].y += 1
                rope = iterate_rope(rope)
                positions.append([rope[9].x, rope[9].y])

        elif d == "D":
            for i in range(0, amount):
                rope[0].y -= 1
                rope = iterate_rope(rope)
                positions.append([rope[9].x, rope[9].y])
            

        print(rope)

print(len(positions))

filtered = []
for x in positions:
    if x not in filtered:
        filtered.append(x)

print(len(filtered))
