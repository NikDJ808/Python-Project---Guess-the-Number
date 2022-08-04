#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)


print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if game_mode == "easy":
  i = 10
  no_attempts_left = False

  while not no_attempts_left:
    if i == 0:
      no_attempts_left = True
    else:
      print(f"You have {i} attempts left to guess the number.")
      guess = int(input("Make a guess: "))

    if guess == number:
      print(f"You've got it! The correct answer was {number}.")
      no_attempts_left = True
    elif guess < number:
      if i > 1:
        print("Too low.\nGuess again.")
        i = i - 1
      else:
        print("Too low.")
        print("You're out of guesses, you lose.")
        no_attempts_left = True
        i = i - 1
    elif guess > number:
      if i > 1:
        print("Too high.\nGuess again.")
        i = i - 1
      else:
        print("Too high.")
        print("You're out of guesses, you lose.")
        no_attempts_left = True
        i = i - 1
elif game_mode == "hard":
  i = 5
  no_attempts_left = False

  while not no_attempts_left:
    if i == 0:
      no_attempts_left = True
    else:
      print(f"You have {i} attempts left to guess the number.")
      guess = int(input("Make a guess: "))

    if guess == number:
      print(f"You've got it! The correct answer was {number}.")
      no_attempts_left = True
    elif guess < number:
      if i > 1:
        print("Too low.\nGuess again.")
        i = i - 1
      else:
        print("Too low.")
        print("You're out of guesses, you lose.")
        no_attempts_left = True
        i = i - 1
    elif guess > number:
      if i > 1:
        print("Too high.\nGuess again.")
        i = i - 1
      else:
        print("Too high.")
        print("You're out of guesses, you lose.")
        no_attempts_left = True
        i = i - 1
else:
  print("Invalid input.")

    
    
    
  
      


