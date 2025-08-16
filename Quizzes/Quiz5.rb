text = "IP address 123.89.46.72 and address 125.90.50.85 need to be accessed"
arr = text.scan(/\d{3}\.\d{2}\.\d{2}\.\d{2}/)
print arr; puts

x = 0

arr2 = []
arr.each {|x| x.scan(/\d+/).each{|x| arr2 << x}}

print arr2; puts

print arr2.map(&:to_i).max