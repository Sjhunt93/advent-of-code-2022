lines = File.readlines("full.txt")
amounts = Array.new
count = 0

for l in lines
    
    if l.length() == 1
        amounts.append(count)
        count = 0
    else
        count += l.to_i
    end

end

# find max of the group sums
print(amounts.max)