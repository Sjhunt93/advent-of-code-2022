from copy import copy

class Point:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0


def has_moved_to_far(head, tail):
    xdif = abs(head.x - tail.x)
    ydif = abs(head.y - tail.y)
    if xdif >= 2 or ydif >= 2:
        return True
    return False

prev = Point()
head = Point()
tail = Point()

positions = []


with open("input.txt") as f:
    lines = f.readlines()
    for l in lines:
        d, amount = l.split(" ")
        amount = int(amount)
        print(d, amount)
        
        if d == "L":
            for i in range(0, amount):
                prev = copy(head)
                head.x -= 1
                if has_moved_to_far(head, tail):
                    tail = copy(prev)
                    positions.append([tail.x, tail.y])
            
        if d == "R":
            for i in range(0, amount):
                prev = copy(head)
                head.x += 1
                if has_moved_to_far(head, tail):
                    tail = copy(prev)
                    positions.append([tail.x, tail.y])
            
        if d == "U":
            for i in range(0, amount):
                prev = copy(head)
                head.y += 1
                if has_moved_to_far(head, tail):
                    tail = copy(prev)
                    positions.append([tail.x, tail.y])
        if d == "D":
            for i in range(0, amount):
                prev = copy(head)
                head.y -= 1
                if has_moved_to_far(head, tail):
                    tail = copy(prev)
                    positions.append([tail.x, tail.y])



print(len(positions))

filtered = []
for x in positions:
    if x not in filtered:
        filtered.append(x)

print(len(filtered))
