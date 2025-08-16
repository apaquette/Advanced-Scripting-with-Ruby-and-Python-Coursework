def toleranceApplication(tol):
    application = 'Toy'
    if tol < 10:
        application = 'Commercial'
    if tol < 1:
        application = 'Military'
    if tol < 0.1:
        application = 'Space Exploration'
    
    return(application)

try:
    tolerance = float(input('Enter the tolerance: '))
    print(toleranceApplication(tolerance))
except:
    print('Invalid Input')