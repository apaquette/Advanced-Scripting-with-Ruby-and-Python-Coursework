maxLambd = lambda do |n1, n2, n3|
    nums = Array[n1, n2, n3]
    max = n1
    i = 1
    while i < 3
      max = nums[i] if max < nums[i]
      i += 1
    end
    return max
  end
  
  puts maxLambd.call(5, 10, 1)