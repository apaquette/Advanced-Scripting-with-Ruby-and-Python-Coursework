grade = 0 
sum = 0
count = 0

while grade != 999:
    grade = float(input('Enter a grade (999 to exit): '))
    
    if grade >= 0 and grade <= 100:
        count += 1
        sum += grade
    elif grade != 999:
        print("Invalid Input")
        
if count > 0:
    print(f'Average grade: {sum/count}')