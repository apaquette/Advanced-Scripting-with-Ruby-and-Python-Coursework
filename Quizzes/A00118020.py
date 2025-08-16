from array import *

generatorRead = [[0]*3]*5

generator = 0
voltRead = 0

#Get input for generators
while(generator != 5):
    print(f"Generator {generator +1}")
    voltRead = 0
    while(voltRead != 3):
        generatorRead[generator][voltRead] = float(input(f"Enter Output Voltage {voltRead + 1}: "))
        voltRead += 1
    generator += 1


#output Generator voltages
generator = 0
while(generator != 5):
    print(f"Generator {generator + 1}: \t")
    voltRead = 0
    while(voltRead != 3):
        print(f"{generatorRead[generator][voltRead]}",end="\t")
        voltRead += 1
    generator += 1
    print("\n")