import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

tempPass = []

for lett in range(0, nr_letters):
    cur = random.choice(letters)
    tempPass.append(cur)

for lett in range(0, nr_symbols):
    cur = random.choice(symbols)
    tempPass.append(cur)

for lett in range(0, nr_numbers):
    cur = random.choice(numbers)
    tempPass.append(cur)


mainPass = ""
for lit in range(0, len(tempPass)):
    cur = random.choice(tempPass)
    mainPass = mainPass + cur
    tempPass.remove(cur)
    
print(f"Your password is : {mainPass}")

#We CAN use shuffle() function!!!
