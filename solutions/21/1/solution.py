import re
to_evaluate = {}

with open("input.txt") as f:
#with open("test.txt") as f:
    lines = f.readlines()
    for l in lines:
        l = l.replace("\n", "")
        key, res = l.split(":")
        print(key, res)
        try:
            res = float(res)
            to_evaluate[key] = res
        except Exception as e:
            to_evaluate[key] = res.strip()
            pass
        


while not isinstance(to_evaluate["root"], float):
    for key, value in to_evaluate.items():
        if not isinstance(value, float):
            
            
            #t = re.split(r"(\w+) ([*\/\-+]) (\w+)", value)
            t = re.match(r"(\w+) ([*\/\-+]) (\w+)", value)
            print(t.group(1), t.group(2), t.group(3))
            k1 = t.group(1)
            op = t.group(2)
            k2 = t.group(3)

            if isinstance(to_evaluate[k1], float) and isinstance(to_evaluate[k2], float):
                # what a lovely hack :D 
                res = eval(f"{to_evaluate[k1]} {op} {to_evaluate[k2]}")
                print(res)
                to_evaluate[key] = res
    

print(to_evaluate["root"])