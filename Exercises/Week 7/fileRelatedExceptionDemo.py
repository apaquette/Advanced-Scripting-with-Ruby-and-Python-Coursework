try:
    fin = open('H:\\UnoMem.txt', 'r')
except FileNotFoundError:
    print('File specified does not exist!')