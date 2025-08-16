#fin = open('NanoMem.txt', 'r')#open for reading
#print(fin.read()) #reads entire text file
#print(fin.read(5))#reads first five characters
#print(fin.readline())#reads line until finding return character

#for i in fin: print(i, end='')#loop through each character
#fin.close()#close to free resources

#fout = open('NanoMem.txt', 'a')#open for appending
#fout.write("\nArduino Nano is awesome!")#append at end of text file
#fout.close()#close to free resources

import os
os.system('cls')
if os.path.exists('NanoMem.txt'):
    print('File exists')
else:
    print('File does not exist')

with open('accounts.txt', mode='w') as account:
    account.write('100 Jones 24.98\n')
    account.write('200 Doe 345.67\n')
    account.write('300 White 0.00\n')
    account.write('400 Stone -42.16\n')
    account.write('500 Rich 224.62\n')

with open('accounts.txt', mode='r') as account:
    print(f'{"Account":<10}{"Name":>10}{"Balance":>10}')
    for record in account:
        account, name, balance = record.split()
        print(f'{account:<10}{name:<10}{balance:>10}')

#JSON: JavaScript Object Notation
