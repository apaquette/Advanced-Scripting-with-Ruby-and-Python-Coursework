#List
#Items indexed, changeable, & allow duplicates
R = ['Carbon', 3.9, 20]
grades = [78, 56, 83, 67, 93]
resistor = ['Carbon', 3.9, 5]

print(f"Length: {len(grades)}")  #gets number of items in list, or "length" of the list
print(f"Index 0: {grades[0]}")   #starts at zero
print(f"Index -1: {grades[-1]}") #negative indicies will loop backwards through the list

#Multi-dimensional lists
matrix = [[10,20],[30,40]]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=' ')
    print()


#removing elements
company = ['Apple', 'Microsoft', 'Google', 'IBM']

del company[3]                  #del method
company.remove('Microsoft')     #.remove method

#appending/inserting elements
company.append('IBM')

#in and not in operators
code = ['C++', 'Java', 'Python']

if('Python' in code):
    print('Awesome!')
else:
    print('Not Awesome!')

#using enumerate()
gates = ['AND', 'OR', 'XOR', 'NOT']

for i, item in enumerate(gates):
    print(f"index {str(i)} in gates is {item}")

#Set
#Items unindexed, unchageable

IT = {'Apple', 'Microsoft', 'Google'}



#Tuple
#Items indexed, unchageable

RLC = ('Resistor', "Capacitor", 'Inductor')



#Dictionary
#Items indexed, changeable
#items are presented in key:value pairs
#can be referred to by using key name
#no duplicates allowed

student = {
    'name' : 'John Doe',
    'id' : 2022123,
    'GPA' : 3.68
}

resistor = {
    'type': 'carbon',
    'value': 3.9,
    'tolerance': 20
}

print(resistor['type'])
print(f'Length: {len(resistor)}')
print(resistor.get("value"))
print(f'Keys: {resistor.keys()}')
print(f'Values: {resistor.values()}')
print(resistor.items())