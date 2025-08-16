text = "Arduino Uno uses ATmega328 i-bit controller that has 32 16-bit registers"

arr = text.scan(/\d+/)

print arr; puts

sum = 0

arr.each { |x| sum += x.to_i}

print sum