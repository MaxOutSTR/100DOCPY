# import random #Python module to generate pseudorandom numbers

# random_number = random.randint(0, 1) #Getting an int between [a and b]
# random_number = random.random() #Getting random number betweeen [0.0 and 1.0>
# random_number = random.uniform(1, 10) #Same as rand int but with floats [a and b]

# print(random_number)

# fibbonacci_numbers = [1, 1, 2, 3, 5] #List data structure declaration in python
# print(fibbonacci_numbers[3]) #Access element on the list with list_name[i]

# fibbonacci_numbers.append(8) #Add element to the end of the list with append

# fibbonacci_numbers.extend([13, 21, 34]) #Add another list to the end of the array

# print(fibbonacci_numbers)

# friends = ["Bruno", "Mauro", "Luis", "Aaron"]
# print(f"{random.choice(friends)} should pay the bill") #random.choice will return a random element inside a list

# fruits = ["Apple", "Banana", "Orange"]
# vegetables = ["Lettuce", "Carrot", "Onion"]

# foods = [fruits, vegetables] #Nested Lists structure [[...], [...], ..., [...]]
# print(foods)

import random
import ascii

print("Day 4: RockPaperScissors")
ascii_options = [ascii.rock_ascii, ascii.paper_ascii, ascii.scissors_ascii]
cpu_option = random.randint(1, 3)
user_option = int(input("What do you choose? Rock-1 Paper-2 Scissors-3: "))
print("")
print("You chose: ")
print(ascii_options[user_option - 1])
print("Computer chose: ")
print(ascii_options[cpu_option - 1])

if user_option == cpu_option:
  print("Tie!")
elif user_option == 1:
  if cpu_option == 2:
    print("CPU Wins")
  else:
    print("You Win!")
elif user_option == 2:
  if cpu_option == 3:
    print("CPU Wins")
  else:
    print("You Win!")
elif user_option == 3:
  if cpu_option == 1:
    print("CPU Wins")
  else:
    print("You Win!")
else:
  print("Not a valid option, Game Over")
