import random
from replit import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  score = sum(cards)
  if score == 21 and len(cards) == 2:
    return 0
  if 11 in cards and score > 21:
    cards.remove(11)
    cards.append(1)
    score = sum(cards)
  return score

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a tie"
  elif computer_score == 0:
    return "Computer has blackjack"
  elif user_score == 0:
    return "User wins with a blackjack"
  elif user_score > 21:
    return "Computer wins"
  elif computer_score > 21:
    return "User wins"
  elif computer_score > user_score:
      return "computer wins"
  elif user_score > computer_score:
      return "You win"
    

def start_game():

  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for i in range (2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your card is: {user_cards}. current score: {user_score}")
    print(f"  Computer's first card is {computer_cards[0]}.")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_choice == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
    
  while computer_score !=0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  start_game()