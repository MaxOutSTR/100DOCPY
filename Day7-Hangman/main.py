import os
import random
import resource

chosen_word = random.choice(resource.word_list)
empty_word = list("_" * len(chosen_word))

has_player_won = True
game_over = False
player_lives = 6
already_warning = False

while not game_over:
  os.system("cls")
  print(resource.logo)
  print(resource.stages[6 - player_lives])
  print("".join(empty_word))
  print(f"Lives: {player_lives}")
  if already_warning:
    print("You already guessed this letter")
    already_warning = False
  initial_empty_spaces = empty_word.count("_")
  chosen_letter = input("Choose a letter: ").lower()
  for index in range(len(chosen_word)):
    if chosen_word[index] == chosen_letter:
      empty_word[index] = chosen_letter
  final_empty_spaces = empty_word.count("_")

  if initial_empty_spaces == final_empty_spaces:
    if chosen_letter not in empty_word:
      player_lives -= 1
    else:
      already_warning = True
  
  if player_lives == 0:
    has_player_won = False
    game_over = True
  
  if "_" not in empty_word:
    game_over = True

if has_player_won:
  print("""
    ************
      You Won!
  it was {chosen_word}
    ************
    """)
else:
  os.system("cls")
  print(resource.stages[6])
  print(f"""
  ************
  You Lose :(
  it was {chosen_word}
  ************
  """)