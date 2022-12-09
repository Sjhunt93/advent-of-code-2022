import re

with open("input.txt") as f:
    print(re.search(r"(\w)(?!\1)(\w)(?!\1|\2)(\w)(?!\1|\2|\3)(\w)(?!\1|\2|\3|\4)", f.read()).end())

    # print(codes)
    # #codes = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    # for i in range(0, len(codes)-3):
    #     sub = codes[i:i+4]
    #     print(sub)
    #     if len(set(sub)) == 4:
    #         print(i+4)
    #         break