import random
from hangman_words import word_list
from hangman_arts import stages
from hangman_arts import logo

display = []
word = ""
life = 6
end_of_game = False

print(logo)
print("Hint: Animal")
chosen_word = random.choice(word_list)


for letter in range(len(chosen_word)):
  display += "_"
  

while not end_of_game:  
  guess = input("Digite uma letra: ").lower()

  if guess in display:
    print(f"You've alredy guessed {guess}")
  for position in range(len(chosen_word)):
    if guess == chosen_word[position]:
      display[position] = guess
  print(f"{' '.join(display)}")
  
  if guess not in chosen_word:
    life -= 1
    print(f"You guessed {guess}, That letter is not in the word.")
    print(f"{' '.join(display)}")
    print(stages[life])
  if life == 0:
    end_of_game = True
    print("You lose")
      
  if "_" not in display:
    end_of_game = True
    print("You win")