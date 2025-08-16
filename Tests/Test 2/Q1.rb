def fib(n)
    if(n == 0 || n == 1)
        return n
    end
    return fib(n - 1) + fib(n - 2)
end

pos = 10
start = 0

while start != (pos + 1)
    print fib(start); print " "
    start += 1
end