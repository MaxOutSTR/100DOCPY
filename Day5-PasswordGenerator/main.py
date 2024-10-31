#For loop structure format
#for item in list_of_items:
  #Do something

# fruits = ["Apple", "Pear", "Banana"]
# for fruit in fruits:
#   print(fruit)


# student_scores = [12, 14, 11, 10, 13, 17]

# total_student_points = sum(student_scores) #sum function sums all numbers in List
# print(total_student_points)

# sum = 0
# for score in student_scores: #sum implemented with for loop instead of sum function
#   sum += score
# print(sum)

# print(max(student_scores)) #max function returns the greatest number in the list

# max_score = 0
# for score in student_scores: #max function implemented with for loop instead of max function
#   if score > max_score:
#     max_score = score
# print(max_score)

# for number in range(1, 11): #Use range function to determine a range of numbers to loop on e.g. [1, 11>
#   print(number)

# sum = 0
# for number in range(1, 101): #Solving the gauss challenge with loops and range
#   sum += number
# print(sum)

import tokens
import random

print("Day 5: Password Generator")
letter_amount = int(input("How many letters would you like in your password?: "))
symbol_amount = int(input("How many symbols would you like?: "))
number_amount = int(input("How many numbers would you like?: "))

password_tokens = []

for amount in range(0, letter_amount):
  password_tokens.append(random.choice(tokens.letters))

for amount in range(0, symbol_amount):
  password_tokens.append(random.choice(tokens.symbols))

for amount in range(0, number_amount):
  password_tokens.append(random.choice(tokens.numbers))

print(password_tokens)

#Without using shuffle function
# final_password = [] 
# num_of_tokens = len(password_tokens)
# for index in range(0, num_of_tokens):
#   chosen_index = random.randint(0, len(password_tokens) - 1)
#   final_password += password_tokens.pop(chosen_index)
# print(final_password)
# print(f"Your password is: ${"".join(final_password)}")

#Using shuffle function
random.shuffle(password_tokens)

print(password_tokens)

print(f"Your password is: {''.join(password_tokens)}")
