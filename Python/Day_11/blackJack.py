############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import os
import random
os.system('cls' if os.name == 'nt' else 'clear')

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

userDraw = []
userDraw.append(random.choice(cards))
userDraw.append(random.choice(cards))

compDraw = []
compDraw.append(random.choice(cards))
compDraw.append(random.choice(cards))

userSum = userDraw[0]+ userDraw[1]
compSum = compDraw[0]+ compDraw[1]

print(f"Your current TOTAL : {userSum} and cards are {userDraw}")
print(f"Computers one card is [{random.choice(compDraw)}]")

print("--------------------------------")
drawMore = True
userLost = False

while drawMore:
    option = (input("Do you want to draw a card? (y/n): ")).lower()
    
    if option == "y":
        drawMore = True
    else: 
        drawMore = False
        break
        
    userDraw.append(random.choice(cards))
    userSum = 0
    for i in range(len(userDraw)):
        userSum = userSum + userDraw[i]

    print(f"Your current TOTAL : {userSum} and cards are {userDraw}")
    
    if userSum > 21:
        for i in range (len(userDraw)):
            if userDraw[i] == 11:
                userDraw[i] = 1
                userSum = 0
                for i in range(len(userDraw)):
                    userSum = userSum + userDraw[i]
                print(f"Your current TOTAL : {userSum} and cards are {userDraw}")
        
        if userSum == 21 and len(userDraw) ==2: 
                print("Its BlackJAck !")
                userLost = False
                drawMore = False
                break

        if userSum > 21:
            print("You Lost :)")
            drawMore = False
            userLost = True
            break
       
def compTurn():
    compMore = True
    while compMore:
        compDraw.append(random.choice(cards))
        compSum = 0

        for i in range(len(compDraw)):
            compSum = compSum + compDraw[i]
    
        print(f"Comps current TOTAL : {compSum} and cards are {compDraw}")
        if compSum > 21:
            for i in range (len(compDraw)):
                if compDraw[i] == 11:
                    compDraw[i] = 1
                    compSum = 0
                    for i in range(len(compDraw)):
                        compSum = compSum + compDraw[i]
                    print(f"COMP's current TOTAL : {compSum} and cards are {compDraw}")
            if compSum > 21:
                print("You WON :)")
                compMore = False
                break
        
        elif compSum > userSum:
            if compSum == 21 and len(compDraw) ==2: 
                print("Its BlackJAck for COMP")
            print("You LOST! :)")
            compMore = False
            break
        elif compSum < 21:
            continue
        else:
            print("It's a tie!")
            compMore = False

if not userLost:
    compTurn()