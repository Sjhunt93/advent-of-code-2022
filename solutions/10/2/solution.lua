
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

-- file = io.open("test.txt", "r")
file = io.open("input.txt", "r")
lines = file:lines()


crt = ""

for line in lines do  
    --print("\t" .. line)
    v = string.find(line, "noop")
    x_inc = 0
    if v then
        cycles = 1
    else
        x_inc = tonumber(string.match(line, '%S+$'))
        cycles = 2
    end
    for i = 0, cycles-1, 1
    do
        print(clock_count, x_register)
        m = clock_count % 40
        if m == x_register-1 or m == x_register or m == x_register+1 then
            crt = crt .. "#"
        else
            crt = crt .. " "
        end

        clock_count = clock_count + 1
    end
    x_register = x_register + x_inc
end

print("\n\n")


for i = 1, 241, 40 do
    -- print(i, i+39)
    print(crt:sub(i, i+39))
end
-- print(crt:sub(1, 40))
-- print(crt:sub(41, 80))
-- print(crt:sub(81, 120))
-- print(crt:sub(121, 160))
-- print(crt:sub(161, 200))
-- print(crt:sub(201, 240))
-- for c in crt do
--     print(c)
-- end
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