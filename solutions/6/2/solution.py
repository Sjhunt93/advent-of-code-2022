
with open("input.txt") as f:
    codes = f.read()
    print(codes)
    #codes = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    for i in range(0, len(codes)-13):
        sub = codes[i:i+14]
        print(sub)
        if len(set(sub)) == 14:
            print(i+14)
            break