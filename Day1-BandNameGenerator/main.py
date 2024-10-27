# Use # to make comments

# print("Hello world!") #Simple Print

# print("Hello world!\nHello world!\nHello world!") #Multiline print with escaped endln

# print("Hello" + " " + "Guillermo") #String concatenation

# input("What is your name?: ") #Prompt input message and receive user text input

# print("Hello " + input("What is your name?: ")) #Use the input function to prompt a welcome message to the user. Exec order = print -> input -> print(with input value)

# name = input("What is your name?: ") #Initialize a variable with the returned string from input function
# print(name) #Print the value stored in the name variable

# name = "John" #Change the value stored in a variable
# print(name)
# length = len(name) #Use len function to get length of a string
# print("Your name has " + str(length) + " characters.") #Use the str function to parse the int to str (print function won't concatenate non str values)

print("Day 1: Band name generator")

city_name = input("What's the name of the city you grew up on?: ")
pet_name = input("What's the name of your first pet?: ")

print("Your band name could be: " + city_name + " " + pet_name)
