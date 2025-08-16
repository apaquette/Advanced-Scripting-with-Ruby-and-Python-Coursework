arrayExample = [1,2,3]
array = [-10...0, 0..10,] #3 dot = not inclusive, 2 dot = inclusive
emptyArray = []
twoDArrayExample = [[1,2], [3,4], [5]]

msg = %w[Python is a gem!]
#print msg

#print twoDArrayExample

empty = Array.new                   #returns a new empty array
nils = Array.new(3)                 #new array with 3 nil elements
zeros = Array.new(4, 0)             #new array with 4 zero elements
copy = Array.new(nils)              #new copy of an existing array
count = Array.new(3) {|i| i+1}      #3 elements computed from index

#print count[-2, 2]

a = [1,2,3] + [4,5]
#print a
#puts
a = a + [[6,7,8]]
#print a

a = ['a', 'b', 'c', 'b', 'a'] - ['b', 'c', 'd']
#puts
#print a

a = []      #starts empty
a << 1      #a is [1]
a << 2 << 3 #a is [1,2,3]
a << [4,5,6]#a is [1,2,3, [4,5,6]]
a = [0] * 8 #[0,0,0,0,0,0,0,0]

a = [1,1,2,2,3,3,4]
b = [5,5,4,4,3,3,2]
c = a | b
print c
puts
c = b | a
print c
puts
c = a & b
print c
puts
c = b & a
print c

a = ('A'..'Z').to_a
a.each {|x| print x}