nameOne = input("Enter Name one: ")
nameTwo = input("Enter Name second: ")

combinedNames = nameOne + nameTwo

mainName = combinedNames.lower()

t = mainName.count("t")
r = mainName.count("r")
u = mainName.count("u")
e = mainName.count("e")
firstDigit = t+r+u+e

l = mainName.count("l")
o = mainName.count("o")
v = mainName.count("v")
e = mainName.count("e")
secondDigit = l+o+v+e

finalDigit = str(firstDigit) + str(secondDigit)
finalDigit = int(finalDigit)
if finalDigit <=10:
    print("You are not a match")
elif finalDigit >=11 and finalDigit <=80:
    print("You may be a match")
elif finalDigit >=81 and finalDigit <=100:
    print("You are a match")
else:
    print("You broke the meter")
    
print(f"And your love score is {finalDigit}%")