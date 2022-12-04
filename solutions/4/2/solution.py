import re

insides = 0

with open("full.txt") as f:
    lines = f.readlines()
    for l in lines:
        match = re.match("(\d+)-(\d+),(\d+)-(\d+)", l)
        
        x1 = int(match.group(1))
        y1 = int(match.group(2))
        x2 = int(match.group(3))
        y2 = int(match.group(4))

        print(x1, "->", y1, " :: ", x2, "->", y2)

        l1 = list(range(x1, y1+1))
        l2 = list(range(x2, y2+1))

        # what a beast of a one liner :D         
        insides += 1 if len([x for x in l1 if x in l2]) else 0

print(insides)