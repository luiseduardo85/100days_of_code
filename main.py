import random
from game_data import data
from art import *
from replit import clear

print(logo)


def get_random():
    return random.choice(data)


aux = False
score = 0
a = get_random()
b = get_random()

while aux != True:

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")

    print(vs)

    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    while a == b:
        b = random.choice(data)
    if user_choice == 'a':
        if a['follower_count'] > b['follower_count']:
            a = b
            b = random.choice(data)
            score += 1
            clear()
            print(logo)
            print(f"You're right! current score: {score}")
        else:
            print(f"This is your final score: {score}")
            aux = True
    elif user_choice == 'b':
        if b['follower_count'] > a['follower_count']:
            a = b
            b = random.choice(data)
            score += 1
            clear()
            print(logo)
            print(f"You're right! current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            aux = True