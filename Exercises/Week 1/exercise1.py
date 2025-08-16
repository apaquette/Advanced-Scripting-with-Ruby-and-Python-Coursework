import os
os.system('cls')

uTemp = float(input('Enter the temperature: '))

tempUnit = input('Is this in Celcius or Farenheit? ')

if(tempUnit == 'C'):
    oTemp = uTemp * 9/5 + 32
    unit = 'Farenheit'
else:
    oTemp = 5/9 * (uTemp - 32)
    unit = 'Celcius'


print(f'Converted Temperature: {oTemp} degrees {unit}')