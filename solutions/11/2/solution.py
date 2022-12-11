import re

# Monkey 0:
#   Starting items: 62, 92, 50, 63, 62, 93, 73, 50
#   Operation: new = old * 7
#   Test: divisible by 2
#     If true: throw to monkey 7
#     If false: throw to monkey 1

class Monkey():
    
    def __init__(self) -> None:
        pass
        self.on_true = 0
        self.on_false = 0
        self.division = 0
        self.items = []
        self.operation = ''
        self.opvalue = ''
        self.items_inspected = 0
    
    def process_operation(self):
        new_items = []
        #print(self.items)
        for x in self.items:
            
            y = x if self.opvalue == 'old' else int(self.opvalue)
            if self.operation == "+":
                new_items.append(x + y)
            elif self.operation == "*":
                new_items.append(x * y)
            else:
                
                assert False
        #print(new_items)
        return new_items
    
    def throw_items(self, othermonkeys):
        items_to_process = self.process_operation()
        
        for i in items_to_process:
            self.items_inspected += 1
            
            i = i % 9699690 # lowest denominator of all the divide by values.

            if i % self.division == 0:
                othermonkeys[self.on_true].items.append(i)
            else:
                othermonkeys[self.on_false].items.append(i)
        self.items = []
    
monkeys = []

with open("input.txt") as f:
    lines = f.readlines()
    for l in lines:
        l = l.strip()
        if re.match("Monkey", l):
            print("new monkey")
            monkeys.append(Monkey())

        if re.match("Starting items:", l):
            numbers = l.split(":")[1].split(",")
            print(numbers)
            monkeys[-1].items = [int(x) for x in numbers]

        if re.match("Operation: new = old", l):
            operation = l.split("= old")[1].strip()
            print(operation)
            opcode, value = operation.split(" ")
            print(opcode, value)
            monkeys[-1].operation = opcode.strip()
            monkeys[-1].opvalue = value

        if re.match("Test: divisible by", l):
            div = int(l.split("by")[1])
            print(div)
            monkeys[-1].division = div

        if re.match("If true", l):
            res = int(l.split("monkey")[1])
            monkeys[-1].on_true = res
        if re.match("If false", l):
            res = int(l.split("monkey")[1])
            monkeys[-1].on_false = res

for m in monkeys:
    print(m.on_true, m.on_false, m.items, m.operation, m.opvalue)


for i in range(0, 10000):
    print(i)
    for m in monkeys:
        m.throw_items(monkeys)

print("\n\n")

for m in monkeys:
    print(m.items_inspected)

quan = [m.items_inspected for m in monkeys]
quan.sort()
print(quan)
print(quan[-1] * quan[-2])