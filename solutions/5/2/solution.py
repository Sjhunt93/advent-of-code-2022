import re

# returns 3 ints
def parse_instruction(ins):
    match = re.match("move (\d+) from (\d+) to (\d+)", ins)
    quan = match.group(1)
    stack_out = match.group(2)
    stack_in = match.group(3)
    return int(quan), int(stack_out), int(stack_in)

def move(sorted_stacks, amount, stack_out, stack_in):
    to_move = []
    for i in range(0, amount):
        
        to_move.append(sorted_stacks[stack_out].pop())
        #print(out, sorted_stacks[stack_out], sorted_stacks[stack_in])

    to_move.reverse()
    sorted_stacks[stack_in] += to_move
    print(sorted_stacks[stack_in], to_move)
    return sorted_stacks
 
with open("stack.txt") as f:
    stacks = f.readlines()
    to_process = []
    for s in stacks[:-1]:
        # regex? :D 
        i = re.findall('....?', s)
        to_process.append(i)
        print(i)



number_of_stacks = len(to_process[0])
print(number_of_stacks)

# rearranging the logic so the arrays are stacked vertically
sorted_stacks = []

for column in range(0, number_of_stacks):
    stack = []
    for row in range(0, len(to_process)):
        # extract the letter
        letter = re.match("\[(\w)\]", to_process[row][column])
        if letter:
            stack.append(letter.group(1))
    stack.reverse()
    print(stack)
    sorted_stacks.append(stack)

print(sorted_stacks)

print("\n\n")

with open("instruction.txt") as f:
    lines = f.readlines()
    for l in lines:
        quan, stack_out, stack_in = parse_instruction(l)

        print("exe: ", quan, " ", stack_out-1, " ", stack_in-1)
        sorted_stacks = move(sorted_stacks, quan, stack_out-1, stack_in-1)
        print(sorted_stacks)


code = ''.join([stack[-1] for stack in sorted_stacks])
print(code)