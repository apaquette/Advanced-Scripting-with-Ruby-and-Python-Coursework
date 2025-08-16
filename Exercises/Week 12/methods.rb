o = "Arduino Nano"

def o.printme
    puts self
end

o.printme

def sum(n1 = 5, n2 = 23)
    return n1 + n2
end

puts sum

def max(first, *rest)
    max = first
    rest.each { |x| max = x if x > max }
    return max
end

puts max(2, 6, 5, 9, 8)
puts max (2)

#passing arrays to methods
def max(arr)
    max = 0
    arr.each { |i| max = i if i > max }
    return max
end

nums = [2,1,4,8,5]
puts max(nums)

#passing hashes to methods
def dispHash(hash)
    hash.each { |key, value| puts value }
end

student = {"name" => "John Doe", "id" => 123, "gpa" => 3.58}
dispHash(student)