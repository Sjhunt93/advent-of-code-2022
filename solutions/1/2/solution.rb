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

# sort then print last 3 elements
amounts = amounts.sort
sum = amounts[-1] + amounts[-2] + amounts[-3]
print(sum)