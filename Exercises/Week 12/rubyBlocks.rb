def myBlock
    yield;yield
end

myBlock {puts "Hello World"}

def numbers
    yield 10
    yield 20
end

numbers {|n| puts n * 2}