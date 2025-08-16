import numpy as np
import pandas as pd

array = np.empty((4,5), int, 'C')

i = 2
for x in range(0, 4):
    for y in range (0, 5):
        array[x][y] = i
        i += 2
        
print('Generated a 4x5 Array:'); print()
print(array); print()

print(f'Sum: {np.sum(array)}\tMean: {np.mean(array)}')

for x in range(0, 4):
    for y in range (0, 5):
        if(array[x][y] == 28):
            print(f"Position of value 28: row = {y} col = {x}")
            break