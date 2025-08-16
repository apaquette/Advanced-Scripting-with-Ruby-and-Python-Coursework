class ComplexMath
    def initialize(r1, i1, r2 = 0, i2 = 0)
        @r1, @i1, @r2, @i2 = r1, i1, r2, i2
    end
    def Addition
        print "Addition: "
        print (@r1 + @r2)
        print " + j"
        print (@i1 + @i2)
        puts
    end

    def Multiplication
        print "Multiplication: "
        print (@r1*@r2 - @i1*@i2)
        print " + j"
        print (@r1*@i2 + @i1*@r2)
        puts
    end

    def Magnitude
        print "Magnitude: "
        print Math.sqrt(@r1**2 + @i1**2)
        puts
    end
end

c = ComplexMath.new(2, 3, 2, 3)

c.Addition
c.Multiplication
c.Magnitude