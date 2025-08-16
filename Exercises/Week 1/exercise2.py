#factorial of positive integer number

import os
os.system('cls')

n = -1

while n < 0:
   n = int(input('Enter positive integer number: ')) 

f = 1

for i in range(1, n+1):
    f *= i

print(f'Factorial = {f}')