system("cls")
def factorial(n)
    f = 1; i = 1
    while i <= n
        f *= i; i += 1
    end
    return f
end
# main program --------------------------
begin
    print "Enter  a positive integer number: "
    num = gets; num = num.to_i
end while num < 0
fact = factorial(num)
print "Factorial = ", fact