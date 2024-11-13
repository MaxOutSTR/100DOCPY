# from turtle import Turtle, Screen
# from prettytable import PrettyTable
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")

# timmy.forward(100)

# my_screen = Screen()

# my_screen.exitonclick()

#Creating new venv: py -m venv venv
#Installing package from PyPI: pip install "packagename"

# table = PrettyTable()

# table.add_column("Pokemon name", ["Pikachu", "Charmander"])
# table.add_column("Type", ["Electric", "Fire", "Plant"])

# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? ({options}): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    my_coffee_maker.report()
    my_money_machine.report()
  elif choice in options:
    drink = menu.find_drink(choice)
    if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
        my_coffee_maker.make_coffee(drink)
  else:
    input("Not a valid option.")