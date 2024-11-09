import random

EASY_TRIES = 10
HARD_TRIES = 5

def set_difficulty(chosen):
  return EASY_TRIES if chosen == "easy" else HARD_TRIES

print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose difficulty (easy/hard): ")

number_of_tries = set_difficulty(difficulty)

thought_number = random.randint(1, 100)

is_game_over = False

while not is_game_over:
  print(f"You have {number_of_tries} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == thought_number:
    print(f"You won! the answer was: {thought_number}")
    is_game_over = True
  elif guess > thought_number:
    print("Too high.")
    
    number_of_tries -= 1
  elif guess < thought_number:
    print("Too low.")
    number_of_tries -= 1

  if number_of_tries < 1:
    print("You've run out of guesses, you lose.")
    is_game_over = True
  elif is_game_over == False:
    print("Guess Again")
