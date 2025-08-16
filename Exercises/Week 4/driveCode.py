
while True:
    code = int(input("Enter Disk Drive code: "))
    match code:
        case 1:
            print("3M Corporation")
        case 2:
            print("Maxell Corporation")
        case 3:
            print("Sony Corporation")
        case 4:
            print("Verbatim Corporation")
        case 9:
            print("Exiting Program")
            break
        case other:
            print("Invalid Input")