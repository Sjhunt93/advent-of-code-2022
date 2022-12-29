Solution 1 = 3133
Solution 2 = 1547953216393

# notes

This was a bit of a pig of a solution to get right
In the end I looked at the print out to work out how often the pattern repeats. 
I did the calculations manually based on the print outs.
In the end I was off my one error :( 

100% I can automate in the future - but this is a very good start :)

After round 106 height is 172 before it repeats
After round 1816 height is 2819

therefore every 1710 rounds it grows by 2647

After the initial offset of 106 rounds we have (1000000000000 - 999999999894) (rounds) remaining
Doing int division we get = 1547953214687
Doing % division we get 984 rounds left.
Height at 2800 = 4358 - 2819 = 1539

Result = 1547953214687 + 172 + 1539 -4


# to run
g++ -std=c++17 solution.cpp && ./a.out >> o.txt