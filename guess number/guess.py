from art import logo
import random

EASY_LVL = 10
HARD_LVL = 5

def check(guess_num, computer_num, life):
  if guess_num > computer_num:
    print("Too high.")
    return life - 1
  elif guess_num < computer_num:
    print("Too low.")
    return life - 1
  else:
    print("Nice job")

def mode():
  difficulty = input("Chose difficulty: Type 'easy' or 'hard': ").lower()
  if difficulty == 'easy':
    return EASY_LVL
  elif difficulty == 'hard' :
    return HARD_LVL

def start_game():
  
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  computer_num = random.choice(range(1,100))

  life = mode()
  
  guessed = False
  while guessed != True:
    print(f"You have {life} attempts remaining to guess the number.")
    guess_num = int(input("Make a Guess: "))
    life= check(guess_num, computer_num, life)
    
    if life == 0:
      print("You've run out of guesses, you lose.")
      guessed = True
      return
    elif guess_num != computer_num:
      print("Guess again.")
    elif guess_num == computer_num:
      guessed = True
      print(f"You guessed it! The number was {computer_num}.")

start_game()