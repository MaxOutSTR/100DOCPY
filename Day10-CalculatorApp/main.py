import art
from os import system

def add(a, b):
  return a + b

def substract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}

def operate_numbers(n1, n2, op):
  return operations[op](n1, n2)

res = 'n'
while res == 'n':
  system("cls")
  print(art.logo)
  num1 = float(input("What's the first number?: "))
  res = "y"
  while res == "y":
    op = input("Pick an operation (+ - * /): ")
    num2 = float(input("What's the next number?: "))
    result = round(operate_numbers(num1, num2, op), 2)
    print(f"{num1} {op} {num2} = {result}")
    res = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if res == 'y':
      num1 = result

