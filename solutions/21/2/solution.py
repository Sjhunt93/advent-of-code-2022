
import re
from copy import deepcopy

to_evaluate = {}

with open("input.txt") as f:
#with open("test.txt") as f:
    lines = f.readlines()
    for l in lines:
        l = l.replace("\n", "")
        key, res = l.split(":")
        #print(key, res)
        try:
            res = float(res)
            to_evaluate[key] = res
        except Exception as e:
            to_evaluate[key] = res.strip()
            pass
        


while not isinstance(to_evaluate["root"], float):
    evals = 0
    for key, value in to_evaluate.items():
        if not isinstance(value, float):
            
            
            #t = re.split(r"(\w+) ([*\/\-+]) (\w+)", value)
            t = re.match(r"(\w+) ([*\/\-+]) (\w+)", value)
            #print(t.group(1), t.group(2), t.group(3))
            k1 = t.group(1)
            op = t.group(2)
            k2 = t.group(3)
            if k1 == "humn" or k2 == "humn":
                continue

            if isinstance(to_evaluate[k1], float) and isinstance(to_evaluate[k2], float):
                # what a lovely hack :D 
                if key == "root":
                    print("Root", to_evaluate[k1], "  ~~ ", to_evaluate[k2], " ", to_evaluate[k1]-to_evaluate[k2])
                res = eval(f"{to_evaluate[k1]} {op} {to_evaluate[k2]}")
                #print(res)
                to_evaluate[key] = res
                evals += 1
    
    #print(evals)
    if not evals:
        print(to_evaluate)
        c = 0
        for key, value in to_evaluate.items():
            if isinstance(value, str):
                c += 1
                print(key, " ", value)

        print(c)
        break





print(to_evaluate["root"])