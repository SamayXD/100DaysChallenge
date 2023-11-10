import os
os.system('cls' if os.name == 'nt' else 'clear')


mainData = []
def addBid():
    option = "y"
    
    while(option=="y"):
        os.system('cls' if os.name == 'nt' else 'clear')

        name = input("\nWhat's your name? ")
        bid = int(input("What's your bid? $"))
        
        mainData.append({"name" : name,
                        "bid": bid})

        option = input("Do you want to add another? (y to continue) ")


addBid()

maxBidder = ""
maxBet = 0
for i in range(len(mainData)):
    if mainData[i]["bid"] > maxBet:
        maxBet = mainData[i]["bid"]
        maxBidder = mainData[i]["name"]        
        

os.system('cls' if os.name == 'nt' else 'clear')      
# print(mainData)
print(f"\nWinner bidder is {maxBidder.upper()} with bet of ${str(maxBet)}")

