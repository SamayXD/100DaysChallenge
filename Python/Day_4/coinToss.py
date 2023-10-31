import random


getChoice = int(input("Enter 0 for heads and 1 for tails: "))

result = random.randint(0,1)

if getChoice == result:
    print("Yay, you won!")
else:
    print("You lost :(")

