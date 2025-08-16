fibLambd = lambda do |n|
    fib = 0
    num1 = 0
    num2 = 1
    i = 0
    while (i < n)
        print fib; print " "
        num1 = fib + num2
        fib = num2
        num2 = num1
        i += 1
    end
end

fibLambd.call(100)