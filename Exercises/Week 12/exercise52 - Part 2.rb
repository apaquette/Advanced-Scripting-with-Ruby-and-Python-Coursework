def factorial(num)
    fac = 1
    i = 1
    while i <= num
        fac = fac * i
        i = i + 1
    end
    return fac
end

eulerNum = -> (count) do
    e = 1
    term = 1
    while (term <= count)
        e += 1.0/factorial(term)
        term += 1
    end
    return e
end

puts eulerNum.call(100)