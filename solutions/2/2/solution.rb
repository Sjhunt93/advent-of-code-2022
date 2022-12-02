lines = File.readlines("full.txt")

map = { "X" => "A", "Y" => "B", "Z" => "C"}

# rock, paper, sizzors
NOMRALISED = 'A'.ord

total_score = 0

for l in lines
    a, b = l.match(/(.) (.)/).captures

    if b == "Y" #draw
        b = a
    end

    a_num = a[0].ord - NOMRALISED
    b_num = b[0].ord - NOMRALISED
    
    if b == "Z" #win
        b_num = (a_num+1).modulo(3)
    elsif b == "X" # loose
        b_num = (a_num-1)
        if b_num < 0
            b_num += 3
        end
    end
    
    print(a, " ", b, " ", a_num, " ", b_num, "\n")

    dif = b_num - a_num
    if dif == 0
        puts("draw")
        score = 3 + b_num + 1
    elsif dif == 1 or dif == -2
        puts("You win")
        score = 6 + b_num + 1
    elsif dif == -1 or diff = 2
        puts("You lose")
        score = b_num + 1
    else # incase we messed something up :/
        puts("ERRROR")
    end
     
    total_score += score
end

puts(total_score)