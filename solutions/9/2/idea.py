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

rope = [Point() for x in range(0,10)]