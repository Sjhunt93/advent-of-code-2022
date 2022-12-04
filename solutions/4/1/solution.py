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

        if (x1 >= x2) and (y1 <= y2):
            print("x inside y")
            insides += 1
        elif (x2 >= x1) and (y2 <= y1):
            print("y inside x")
            insides += 1

print(insides)