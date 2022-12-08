

class Matrix
    
    attr_accessor :x_size
    attr_accessor :y_size
    attr_accessor :numbers

    def initialize(x, y)
        @numbers = Array.new(x*y)
        @x_size = x
        @y_size = y
        for i in 0..x_size*y_size-1
            numbers[i] = 0
        end
    end

    def read(x, y)
        index = x + y * x_size
        return numbers[index]
    end

    def write(x, y, val)
        index = x + y * x_size
        numbers[index] = val
    end

    # Im sure I can make this one fucntion rather than 2 but meh
    def descend_x(x, y, xinc, yinc)
        disx = x
        disy = y
        
        start = read(x,y)
        loop do
            x += xinc
            y += yinc
            current = read(x,y)
            #print(x, " ", y, "\n")

            if current >= start
                return [(x-disx).abs, (y-disy).abs].max
            end
            if x == 0 or x == x_size-1 or y == 0 or y == y_size-1
                return [(x-disx).abs, (y-disy).abs].max
            end
            
        end
        
    end

    def probe(x,y)
        visable_left =  descend_x(x, y, 1, 0)
        visable_right = descend_x(x, y, -1, 0)
        visable_down =  descend_x(x, y, 0, 1)
        visable_up =    descend_x(x, y, 0, -1)
        print(visable_left, " ", visable_right, " ", visable_up, " ", visable_down, "\n")
        return (visable_left * visable_right * visable_down * visable_up)
    end




end

#lines = File.readlines("map.txt")
lines = File.readlines("input.txt")

ysize = lines.length()
xsize = lines[0].length()-1

puts ysize
puts xsize

grid = Matrix.new(xsize, ysize)

for y in 0..ysize-1
    for x in 0..xsize-1
        grid.write(x,y,lines[y][x].to_i)
        print(grid.read(x, y), ",")
    end
    print("\n")
end

trees = Array.new

for y in 1..ysize-2
    for x in 1..xsize-2
        res = grid.probe(x, y)
        trees.push(res)
    end
end

puts trees.max

