import pandas as pd

grades = pd.Series([87, 100, 94])

#print(grades)
#print(grades[2])

seriesRange = pd.Series(98.6, range(3))

#print(seriesRange)

# print(grades.count()) #number of elements
# print(grades.min())
# print(grades.max())
# print(grades.std()) #standard deviation
print(f"Describe: \n{grades.describe()}")

ArduinoUNO = pd.Series([14, 6, 3], index=['digital', 'analog', 'timers'])
print(ArduinoUNO)

#Dictionary Initializers
dict_ArduinoUNO = pd.Series({'digital': 14, 'analog': 6, 'timers': 3})
print(dict_ArduinoUNO)

#DataFrames: enhanced 2D array
grades_dict = {'Wally':[87, 96, 70], 'Eva': [100, 87, 90], 'Sam':[94, 77, 90], 'Katie': [100, 81, 82], 'Bob':[83, 65, 85]}
grades = pd.DataFrame(grades_dict)
print(grades)
grades.index = ['Test1', 'Test2', 'Test3']
print(grades)

#Selecting rows via loc & iloc attributes
print(f"Loc: {grades.loc['Test1']}")
print(f"iLoc: {grades.iloc[1]}")

#slice
print(grades.loc['Test1':'Test2'])

#Boolean Indexing
print(grades[grades >= 80])

