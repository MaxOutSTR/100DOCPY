import random
from os import system

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(u_score, c_score):
  if u_score == c_score:
    return "Draw"
  elif c_score == 0:
    return "Lost, Opponent has Blackjack"
  elif u_score == 0:
    return "Win with a Blackjack"
  elif u_score > 21:
    return "You went over. You lose"
  elif c_score > 21:
    return "Computer went over. You win!"
  elif u_score > c_score:
    return "You Win!"
  else:
    return "You Lose"


def play_game():

  user_cards = []
  computer_cards = []
  computer_score = -1
  user_score = -1

  continue_playing = True

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while continue_playing:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your Cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      continue_playing = False
    else:
        will_get_card = input("Type 'y' to get another card, type 'n' to pass: ") == 'y'
        if will_get_card:
          user_cards.append(deal_card())
        else:
          continue_playing = False

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"User: {user_cards} -> {user_score}  |  Computer: {computer_cards} -> {computer_score}")
  print(f"The result of the match is: {compare(user_score, computer_score)}")


while input('Do you want to play a game of blackjack?(y/n): ') == 'y':
  system("cls")
  play_game()
