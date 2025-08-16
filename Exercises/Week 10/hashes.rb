numbers = { "one" => 1, "two" => 2, "three" => 3 }
x = { "a" => 1, "b" => 2 }
x.each { |key, value| puts "#{key} equals #{value}" }

puts x.keys.inspect

#delete hash elements
x.delete("a")
puts x.inspect

#delete conditionally
x = { "a" => 100, "b" => 20 }
x.delete_if { | key, value | value < 25}
puts x.inspect


#nested hashes
people = {
    'fred' => {
        'name' => 'Fred Elliott',
        'age' => 63,
        'gender' => 'male',
        'favorite painters' => ['Monet', 'Constable', 'Da Vinci']
    },
    'janet' => {
        'name' => 'Janet S Porter',
        'age' => 55,
        'gender' => 'female'
    }
}