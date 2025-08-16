myLambda = lambda {puts "My 1st lambda"}
myLambda.call

factorial = -> (n) do
    f = 1; i = 1
    while i <= n
        f = f * i; i = i + 1
    end
    return f
end

puts factorial.call(9)