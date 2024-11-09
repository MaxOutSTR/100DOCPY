import art
from game_data import data
import random
from os import system

def print_comparison(option_A, option_B):
  print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
  print(art.vs)
  print(f"Against B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}")

def calculate_next_pick (other_pick):
  next_pick = data[random.randint(0, len(data) - 1)]
  while next_pick['name'] == other_pick['name']:
    next_pick = data[random.randint(0, len(data) - 1)]
  return next_pick


is_game_over = False
score = 0

first_pick = data[random.randint(0, len(data) - 1)]
second_pick = calculate_next_pick(first_pick)

while not is_game_over:
  system("cls")
  print(art.logo)
  if score != 0:
    print(f"You're right! Current score: {score}")
  print_comparison(first_pick, second_pick)

  choice = input("Who has more followers?(A/B): ").lower()

  if choice == 'a':
    if first_pick['follower_count'] > second_pick['follower_count']:
      score += 1
      second_pick = calculate_next_pick(first_pick)
    else:
      is_game_over = True
  else:
    if second_pick['follower_count'] > first_pick['follower_count']:
      score += 1
      first_pick = second_pick
      second_pick = calculate_next_pick(first_pick)
    else:
      is_game_over = True
      
system("cls")
print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")
