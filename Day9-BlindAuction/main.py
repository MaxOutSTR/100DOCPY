# programming_dictionary = { #Dictionary syntax
#   "Bug": "Bug description",
#   "Function": "Function description",
# }
# programming_dictionary["Loop"] = "Loop description"

# print(programming_dictionary["Loop"]) #Accessing value with key

# programming_dictionary = {} #Clean dictionary

# for thing in programming_dictionary: #Loop a dictionary
#   print(thing) #This is the key
#   print(programming_dictionary[thing]) #This access value

import art
from os import system

def find_highest_bidder(dictionary):
  highest_bidder_name = ""
  highest_bid_ammount = 0
  for name in dictionary:
    if dictionary[name] > highest_bid_ammount:
      highest_bid_ammount = dictionary[name]
      highest_bidder_name = name
  return {highest_bidder_name: highest_bid_ammount}
  
print(art.logo)

print("Welcome to the blind auction program")

should_continue = True

bidders_dictionary = {}

while should_continue:
  name = input("What is your name?: ")
  bid = input("What is your bid?: $")
  bidders_dictionary[name] = int(bid)
  more_bidders = input("Are there any other bidders?(yes/no): ")
  if more_bidders.lower() != "yes":
    should_continue = False
  else:
    system("cls")

winner = find_highest_bidder(bidders_dictionary)
for name in winner:
  print(f"The winner is {name} with ${winner[name]}")



