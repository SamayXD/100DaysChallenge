import random

remainingLives = 6

def reduceLife():
    global remainingLives
    remainingLives -=1
print("Welcome to HandMann")

wordList = ["skkeky", "baleloeon", "jewep", "gaaeaarden"]

selectWord = random.choice(wordList)

print(selectWord)

finalBlank = ""
for i in range(len(selectWord)):
    finalBlank += "_"



blank = []
final =[]
for letters in finalBlank:
    blank.append("_")

for l in selectWord:
    final.append(l)

def addLetter(newGuess):
    wasThere = False
    for lt in range(0 , len(selectWord)):
        if newGuess == selectWord[lt]:
            # index = selectWord.index(lt)
            blank[lt] = newGuess
            wasThere = True
            
        
    else:
        if wasThere == False:
            print("Was not there")
            reduceLife()

while remainingLives != 0:
    print(blank)
    print(final)
    
    if final == blank:
        break
    else: 
        print(f"Current lifes remaining : {remainingLives}")
        newGuess = input("Guess the next letter : ")
        addLetter(newGuess)
