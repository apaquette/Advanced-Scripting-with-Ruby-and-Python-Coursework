age = 24
gender = "male"
puts "You're NOT a teenager" unless age > 12 && age < 20

puts "You're a working age man" if gender == "male" && (age >= 18 && age <= 65)