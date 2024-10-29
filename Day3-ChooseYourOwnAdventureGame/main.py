#Conditional structure
# a = 5
# if a > 6:
#   print(True)
# else:
#   print(False)

# print(10 % 2) #Modulo operator


#Else if control structure (elif)
# salary = 100_000
# if salary > 100_000:
#   print("Group A")
# elif salary >80_000:
#   print("Group B")
# else:
#   print("Group C")

#Logical Operators
# a and b
# a or b
# not c

print('''
      ___________________________________________________
              Welcome to the abandoned cabin

       ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^
      /|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\\
      /|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\\
      /|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\\
''')

print("You are lost in the woods, the night get's colder and you see a cabin in the distance")
choice1 = input(f"What would you do, go inside, or explore the outside? (inside/outside): ")

if choice1 == "outside" or choice1 == "Outside":
  print("He found you, Game Over")
elif choice1 == "inside" or choice1 == "Inside":
  print("You are now inside the cabin and it's really dark")
  choice2 = input(f"What would you do first, lock the door, or turn on the light? (door/light): ")
  if choice2 == "light" or choice2 == "Light":
    print("He saw the lights and opened the door, Game Over")
  elif choice2 == "door" or choice2 == "Door":
    print("You turn on the lights and see a backdoor and a closet, someone is trying to open the door")
    choice3 = input(f"What will you do now, go through the backdoor or hide in the closet? (backdoor/closet): ")
    if choice3 == "closet" or choice3 == "Closet":
      print("He rushed in and easily found you in the closet, Game Over")
    else:
      print("You escaped the cabin without him noticed. You Win.")
      