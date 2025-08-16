def displayVoltage(time):
    if time < 2:
        print('0 volts')
    else:
        print('3 volts')

try:
    time = float(input('Enter the time in seconds: '))
    displayVoltage(time)
except:
    print('Invalid Input')