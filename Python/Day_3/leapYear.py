year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0 :
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("Its not a leap year")
    else:
        print("It is a leap year")
else:
    print("Its not a leap year")
