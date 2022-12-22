
import re
from copy import deepcopy

to_evaluate = {}

#with open("test.txt") as f:
with open("input.txt") as f:
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
        

def iterate_k(key):
    for i in "*-+/":
        if i in key:
            x, y = key.split(i)
            x = x.strip()
            y = y.strip()
            if isinstance(x, str) and x != "humn":
                if x in to_evaluate and isinstance(to_evaluate[x], float):
                    x = to_evaluate[x] # resolved
                else:
                    x = iterate_k(to_evaluate[x])
            if isinstance(y, str) and y != "humn":
                if y in to_evaluate and isinstance(to_evaluate[y], float):
                    y = to_evaluate[y] # resolved
                else:
                    y = iterate_k(to_evaluate[y])
            return f"({str(x)} {i} {str(y)})"


while not isinstance(to_evaluate["root"], float):
    evals = 0
    for key, value in to_evaluate.items():
        if not isinstance(value, float):
            
            
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

a = iterate_k(to_evaluate["hsdb"])
print(a)#, eval(a))

# 34588563455325.0

for i in range(3059361890000, 90177205134225):
    sum = eval(a.replace("humn", str(i)))
    #print("done", abs(34588563455325.0 - sum))

    if sum - 34588563455325.0 < 0:
        print(i, sum)
        assert False
    #if i % 1000000 == 0:
    print("done", sum - 34588563455325.0, i)
    if sum == 34588563455325.0:
        print("done", abs(34588563455325.0 - sum), i)
        break
