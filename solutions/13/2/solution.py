
import itertools
    

def expand_items(l1, l2):
    assert isinstance(l1, list)
    assert isinstance(l2, list)

    for a,b in itertools.zip_longest(l1, l2):
        if a == None and b != None :
            return "order"
        if b == None and a != None:
            return "not"

        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return "order"
            elif a > b:
                return "not"

        elif isinstance(a, int) and isinstance(b, list):
            r = expand_items([a],b)
            if r != "continue":
                return r
        elif isinstance(a, list) and isinstance(b, int):
            r = expand_items(a,[b])
            if r != "continue":
                return r
        elif isinstance(a, list) and isinstance(b, list):
            r = expand_items(a,b)
            if r != "continue":
                return r

    return "continue"


to_sort = []
with open("input.txt") as f:
#with open("test.txt") as f:

    lines = f.read()
    packets = [i.split("\n") for i in lines.split("\n\n")]
        
    for i, p in enumerate(packets):
        to_sort.append(eval(p[0]))
        to_sort.append(eval(p[1]))
        

sorted = [to_sort.pop()]
to_sort += [[[2]], [[6]]]

for i in range(0, len(to_sort)):
    packet = to_sort[i]
    for s in range(0, len(sorted)):
        if expand_items(packet, sorted[s]) == "order":
            sorted.insert(s, packet)
            break
        elif s == len(sorted)-1:
            sorted.append(packet)
    

# debug
print("\n\n\n")
for i, s in enumerate(sorted[1:]):    
    print(i, "~", expand_items(sorted[i-1], s))


ia = sorted.index([[2]])+1
ib = sorted.index([[6]])+1
print(ia * ib)
