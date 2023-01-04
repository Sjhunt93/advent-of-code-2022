
# places = [1]
# for x in range(1,10):
#     places.append(places[-1] * 5)

places = [5 ** x for x in range(0, 20)]
print(places)

# def 

def convert_snafu_to_dec(snafu):
    sum = 0
    for i, x in enumerate(snafu[::-1]):
        x = x.replace("-", "-1").replace("=", "-2")
        # print(x)
        sum += int(x) * places[i]
    return sum

def convert_dec_to_snafu(sum):
    quantaties = []
    
        
    for i in places[::-1]:
        print(i)
        part = int(sum/i)
        quantaties.append(part)
        sum -= part*i

    quantaties = quantaties[::-1]
    

    carry = 0
    reversed = ""
    for q in quantaties:
        q += carry
        carry = 1
        if q == 3:
            reversed += "="
        elif q == 4:
            reversed += "-"
        elif q == 5:
            reversed += "0"
        else:
            carry = 0
            reversed += str(q)

    reversed = reversed[::-1]
    while reversed[0] == "0":
        reversed = reversed[1:]

    return reversed

output_sum = 0
with open("input.txt") as f:
    lines = f.read().split("\n")
    for l in lines:
        # l = l[::-1]
        # print(l)
        sum = convert_snafu_to_dec(l)
        print(l, " = ", sum)

        output_sum += sum
        reversed = convert_dec_to_snafu(sum)

        print("final output", reversed)
        assert reversed == l

    print("final: ", convert_dec_to_snafu(output_sum))