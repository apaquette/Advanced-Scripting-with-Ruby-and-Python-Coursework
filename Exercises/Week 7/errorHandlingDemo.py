#File-related exceptions: FileNotFoundError, PermissionsError, ValueError

while True:
    try:
        n1 = int(input('Enter numerator: '))
        n2 = int(input('Enter denominator: '))
        result = n1 / n2
    except ValueError:
        print('You must enter two integers\n')
    except ZeroDivisionError:
        print('Attempted to divide by zero\n')
    else:
        print(f'{n1: .3f} / {n2: .3f} = {result: .3f}')
        break