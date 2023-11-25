from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
is_on = True


while is_on:
    
    os.system('cls' if os == 'ns' else 'clear')
    order = input("Enter your order : \n1.latte [250Rs.]\n2.cappuccino [300Rs.]\n3.espresso [150Rs.]\n==> ")

    
    if order == "off":
        is_on= False
        break
    elif order == "report":
        my_coffee_maker.report()
        input()
    elif order == "profit":
        my_money_machine.report()
        input()

    else: 
        coffee = my_menu.find_drink(order)
        coffee_cost = coffee.cost
        if my_coffee_maker.is_resource_sufficient(coffee):
            if my_money_machine.make_payment(coffee_cost):
                my_coffee_maker.make_coffee(coffee)
            
        input()

    