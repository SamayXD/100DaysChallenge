import art
import os
import gameData
import random

counter = 0;
player_lost = False

def startIt():
    os.system('cls' if os == 'nt' else 'clear')
    print(art.logo)

    print("Welcome to HigherLower Game")
    print(f"Your current score is {counter}")


compareOne = gameData.data[random.randint(0,len(gameData.data)-1)]
compareTwo = gameData.data[random.randint(0,len(gameData.data)-1)]

if compareOne == compareTwo:
    compareTwo = gameData.data[random.randint(0,len(gameData.data)-1)]

# print(compareOne)
# print(compareTwo)

def compare():
    print(f"Compare A = {compareOne['name']}, a {compareOne['description']}, from {compareOne['country']}.")
    print(art.vs)
    print(f"Compare B = {compareTwo['name']}, a {compareTwo['description']}, from {compareTwo['country']}.")


def doCompare():
    choice = input("Who has more followers? Type 'A' or 'B': ")
    
    global choiceCompareA
    global choiceCompareB
    if choice == "A":
        choiceCompareA = compareOne
        choiceCompareB = compareTwo
        
    elif choice == "B":
        choiceCompareA = compareTwo
        choiceCompareB = compareOne
    else:
        print("Invalid input :(")
    
        
        
startIt()
compare()
doCompare()

# choiceCompareA = compareOne
# choiceCompareB = compareTwo

while not player_lost:
    if int(choiceCompareA['follower_count']) > int(choiceCompareB['follower_count']):
        print("YOU DID RIGHT")
        counter +=1
        startIt()
        compare()
        doCompare()
        compareOne = choiceCompareA
        compareTwo = gameData.data[random.randint(0,len(gameData.data)-1)]
        
    else:
        os.system('cls' if os == 'nt' else 'clear')
        print(art.lost)
        player_lost = True