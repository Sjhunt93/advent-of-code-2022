
with open("input.txt") as f:
    codes = f.read()
    print(codes)
    #codes = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    for i in range(0, len(codes)-3):
        sub = codes[i:i+4]
        print(sub)
        if len(set(sub)) == 4:
            print(i+4)
            break