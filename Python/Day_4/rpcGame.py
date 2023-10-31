import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Welcome to rock, paper, scissors!")

userTurn = input("R for rock\nP for paper\nS for scissors\n=> ")
userTurn = userTurn.upper()

opts = ["rock", "paper", "scissors"]
compDone = opts[random.randint(0, 2)]


if userTurn == "R":
    userDone = "rock"
    print(f"You chose {userDone} \n" + rock)

elif userTurn == "P":
    userDone = "paper"
    print(f"You chose {userDone} \n" + paper)

elif userTurn == "S":
    userDone = "scissors"
    print(f"You chose {userDone} \n" + scissors)

else:
    print("INVALID...")


if compDone == "rock":
    print(f"Comp chose {compDone} \n" + rock)
elif compDone == "paper":
    print(f"Comp chose {compDone} \n" + paper)
elif compDone == "scissors":
    print(f"Comp chose {compDone} \n" + scissors)


if userDone == compDone:
    print("It's a tie!")
elif userDone == "rock" and compDone == "paper":
    print("You Lost!")
elif userDone == "rock" and compDone == "scissors":
    print("You Won!")

elif userDone == "paper" and compDone == "scissors":
    print("You Lost!")
elif userDone == "paper" and compDone == "rock":
    print("You Won!")


elif userDone == "scissors" and compDone == "paper":
    print("You Lost!")
elif userDone == "scissors" and compDone == "rock":
    print("You Won!")
