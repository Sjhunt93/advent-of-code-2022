
import itertools


indexes_in_order = []

def compare_lists(l1, l2):
    if l1 == None:
        return True
    if l2 == None:
        return False

    if not isinstance(l1, list):
        l1 = [l1]
    if not isinstance(l2, list):
        l2 = [l2]
    for a,b in itertools.zip_longest(l1, l2):
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return True
            elif a > b:
                return False
        else:
            return compare_lists(a, b)

    

def expand_items(l1, l2):
    assert isinstance(l1, list)
    assert isinstance(l2, list)
    for a,b in itertools.zip_longest(l1, l2):
        if a == None and b != None :
            indexes_in_order.append(i+1)
            return "order"
        if b == None and a != None:
            return "not"

        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                indexes_in_order.append(i+1)
                return "order"
            elif a > b:
                return "not"
        elif isinstance(a, int) and isinstance(b, list):
            r = expand_items([a],b)
            if r == "order" or r == 'not':
                #indexes_in_order.append(i+1)
                return r
        elif isinstance(a, list) and isinstance(b, int):
            r = expand_items(a,[b])
            if r == "order" or r == 'not':
                #indexes_in_order.append(i+1)
                return r
        elif isinstance(a, list) and isinstance(b, list):
            if a and b:
                r = expand_items(a,b)
                if r == "order" or r == 'not':
                    #indexes_in_order.append(i+1)
                    return r
    return "not"


#with open("test.txt") as f:
with open("input.txt") as f:

    lines = f.read()
    packets = [i.split("\n") for i in lines.split("\n\n")]
        
    for i, p in enumerate(packets):
        l1 = eval(p[0])
        l2 = eval(p[1])
        print(l1)
        print(l2)
        expand_items(l1, l2)
        # if i == 31:
        #     print("..")
        # if (compare_lists(l1, l2)):
        #     indexes_in_order.append(i+1)
        
indexes_in_order.sort()
print(indexes_in_order)
    # print(set(indexes_in_order))
print(sum(set(indexes_in_order)))