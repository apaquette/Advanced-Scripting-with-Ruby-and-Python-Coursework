x = 8
if x < 10 then x += 1 end
#puts(x)

x = 3
name =  if      x == 1 then "one"
        elsif   x == 2 then "two"
        elsif   x == 3 then "three"
        else                "four"
        end
#puts name

#case Statement
code = 2
case code
when 0
        puts "black"
when 1
        puts "brown"
when 2
        puts "red"
else
        "invalid code!"
end

#ternary operator
bit = 1
bit == 0 ? (puts "Logic 0") : (puts "Logic 1")