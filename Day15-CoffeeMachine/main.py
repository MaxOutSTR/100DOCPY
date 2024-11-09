from p_data import menu, resources

is_on = True
profit = 0

def is_resource_sufficient(order_ingredients):
  for item in order_ingredients:
    if order_ingredients[item] > resources[item]:
      print(f"Sorry, there's not enough {item}")
      return False
  return True

def get_money():
  total = 0
  total += int(input("How many quarters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.1
  total += int(input("How many nickles?: ")) * 0.05
  total += int(input("How many pennies?: ")) * 0.01
  return total

def get_change(money, price):
  return money - price

def make_coffee(drink_name, order_ingredients):
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  print(f"Here's your {drink_name}")

while is_on:
  choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
  if choice == "off":
    is_on = False
  elif choice == "report":
    print(f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}g
    Money: ${profit}
    """)
  elif choice in ["espresso", "latte", "cappuccino"]:
    drink = menu[choice]
    has_resource = is_resource_sufficient(drink['ingredients'])
    if has_resource:
      money = get_money()
      change = round(get_change(money, drink['cost']), 2)
      if change >= 0:
        print(f"Money is enough, your change is {change}")
        profit += round(money - change, 2)
        make_coffee(choice, drink["ingredients"])
      else:
        print(f"Not enough money, you are short by {change}")
  else:
    print("Invalid choice, please try again.")