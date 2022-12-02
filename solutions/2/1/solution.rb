lines = File.readlines("full.txt")

map = { "X" => "A", "Y" => "B", "Z" => "C"}

# rock, paper, sizzors
NOMRALISED = 'A'.ord

total_score = 0

for l in lines
    a, b = l.match(/(.) (.)/).captures
    b = map[b]

    a_num = a[0].ord - NOMRALISED
    b_num = b[0].ord - NOMRALISED

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