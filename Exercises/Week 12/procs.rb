square = Proc.new { |x| x**2 }
puts square.call(2)
puts square.(3)
puts square[4]