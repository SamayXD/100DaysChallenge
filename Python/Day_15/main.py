#Coffee Machine Project
import os
import pprint
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0
}
    

machineOn = True
isReady = ""
billPaid = False

def makeEspresso():
    global isReady
    if int(MENU["espresso"]["ingredients"]["water"]) > int(resources["water"]):
        isReady = "Insufficient Waterrr"
    elif int(MENU["espresso"]["ingredients"]["coffee"]) > int(resources["coffee"]):
        isReady = "Insufficient Coffie"           
    else:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        isReady = "YES"
        goBill("e")
        
    if isReady == "YES": goBill("e")
        
        
def makeLattee():
    global isReady
    if int(MENU["latte"]["ingredients"]["water"]) > int(resources["water"]):
        isReady = "Insufficient Waterrr"
    elif int(MENU["latte"]["ingredients"]["coffee"]) > int(resources["coffee"]):
        isReady = "Insufficient Coffie"      
    elif int(MENU["latte"]["ingredients"]["milk"]) > int(resources["milk"]):
        isReady = "Insufficient milk"        
    else:
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        isReady = "YES"
    if isReady == "YES": goBill("l")
    
        
def makeCappuccino():
    global isReady
    if int(MENU["cappuccino"]["ingredients"]["water"]) > int(resources["water"]):
        isReady = "Insufficient Waterrr"
    elif int(MENU["cappuccino"]["ingredients"]["coffee"]) > int(resources["coffee"]):
        isReady = "Insufficient Coffie"    
    elif int(MENU["cappuccino"]["ingredients"]["milk"]) > int(resources["milk"]):
        isReady = "Insufficient milk"        
    else:
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        isReady = "YES"
        
    if isReady == "YES": 
        goBill("c")

        
def goBill(whichCoffee):
    global billPaid
    
    cash_100 = int(input("Cash of 100 -> ")) * 100
    cash_50 = int(input("Cash of 50 -> "))* 50
    cash_20 = int(input("Cash of 20 -> "))* 20
    cash_10 = int(input("Cash of 10 -> "))*10
    
    cash_paid = cash_10 + cash_20 + cash_50 + cash_100
    cost = MENU["espresso"]["cost"]
    if whichCoffee == "e":
        cost = MENU["espresso"]["cost"]
    elif whichCoffee == "l":
        cost = MENU["latte"]["cost"]
    elif whichCoffee == "c":
        cost = MENU["cappuccino"]["cost"]

    if cost == cash_paid:
        print("ThankYou...")
        billPaid = True
            
    elif cost < cash_paid:
        cash_back = cash_paid - cost
        cash_paid -= cash_back
        print(f"ThankYou. Here's the chance : {cash_back}")
        billPaid = True

    elif cost > cash_paid:
        print("Less Paid. Refunded.")
        cash_paid = 0
        billPaid = False
            
            
    resources["profit"] += cost
    
while machineOn:
    isReady = ""
    billPaid = False

    os.system('cls' if os == 'ns' else 'clear')
    choice = input("What would you like?\nespresso -e\nlatte -l\ncappuccino -c\n -:> ")
    
    if choice == "off":
        machineOn = False
        break
    elif choice == "report":
        pprint.pprint(resources)
        input()
    elif choice == "e":
        makeEspresso()    
    elif choice == "l":
        makeLattee()    
    elif choice == "c":
        makeCappuccino()


    if billPaid == True:
        print("Enjoy your Coffee")
        input()
    else:
        print(isReady)
        input()