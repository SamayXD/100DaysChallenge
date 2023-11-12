import art
import os
import random
os.system('cls' if os=='nt' else 'clear')
print(art.logo)

print("Welcome to Guess Game!")
level = int(input("Select Level of the game...\n1. EASY (10 Attemps)\n2. HARD (5 Attemps)\n=> "))
attempts = 0

if level == 1:
    attempts = 10
else:
    attempts = 5
    
number_to_guess = random.randint(1,100)
# number_to_guess = 50

print("Guess the Number between 1 to 100!")

while(attempts!=0):
    print(f"\nYou have {attempts} attempts remaining...")
    guess = int(input("Enter your guess: "))
    if guess > number_to_guess:
        print("Too high")
        attempts -=1
        
    elif guess < number_to_guess:
        print("Low")
        attempts -=1
        
    elif guess == number_to_guess:
        os.system('cls' if os=='nt' else 'clear')
        print(art.won)
        break
    
if attempts == 0:
    os.system('cls' if os=='nt' else 'clear')

    print(art.lost)
    
