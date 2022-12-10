
CYCLES_TO_CHECK = {20, 60, 100, 140, 180, 220}


local function in_array(array, x)
    for _, v in ipairs(array) do
        if v == x then
            return true
        end
    end
    return false
end


clock_count = 0
cycles = 0
x_register = 1
sum = 0

-- file = io.open("test.txt", "r")
file = io.open("input.txt", "r")
lines = file:lines()


for line in lines do  
    --print("\t" .. line)
    v = string.find(line, "noop")
    x_inc = 0
    if v then
        cycles = 1
        
    else
        x_inc = tonumber(string.match(line, '%S+$'))
        --print("Increment x by", x_inc)

        cycles = 2
    end
    for i = 0, cycles-1, 1
    do
        clock_count = clock_count + 1
        --print(clock_count)
        if in_array(CYCLES_TO_CHECK, clock_count) then
            print(x_register)
            sum = sum + (x_register * clock_count)
        end 
    end
    x_register = x_register + x_inc
end

print("SUM: ", sum)
-- -- print(cycles)

-- -- for i = 1, #line, 1 
-- -- do
    
-- --     print(line[i])
-- --     
-- --     print(v)
-- -- end

-- -- with open("input.txt") as f:
-- -- codes = f.read()
-- -- print(codes)
-- -- #codes = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
-- -- for i in range(0, len(codes)-3):
-- --     sub = codes[i:i+4]
-- --     print(sub)
-- --     if len(set(sub)) == 4:
-- --         print(i+4)
-- --         break

-- -- local xxx = string.sub(line,i,i+3)
-- --     print(xxx)
-- --     for j = 1, #xxx do
-- --         local c = xxx:sub(j,j)
-- --         print(c)
-- --     end
-- --     -- local c = line:sub(i,i)
-- --     -- print(c)