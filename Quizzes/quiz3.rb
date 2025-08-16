approx = 1
prev = 0
count = 1
tolerance = 10**-9

def factorial(num)
    fac = 1
    i = 1
    while i <= num
        fac = fac * i
        i = i + 1
    end
    return fac
end

while (approx - prev) > tolerance
    prev = approx
    approx += 1.0/factorial(count)
    count += 1
end

puts approx