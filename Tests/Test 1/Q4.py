import pandas as pd

testDict = {
    1:{
        'A': 56,
        'B': 71,
        'C': 13
    },
    2:{
        'A': 29,
        'B': 63,
        'C': 34
    },
    3:{
        'A': 83,
        'B': 60,
        'C': 71
    }
}

testDataFrame = pd.DataFrame.from_dict(testDict)
testDataFrame = testDataFrame.T
print(testDataFrame)



print(f'Number of values greater than 50: {testDataFrame[testDataFrame > 50].count().sum()}')