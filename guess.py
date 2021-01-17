#Guess the number game from in Invent Your Own Games With Python.
import random


attempt = 0

print("Welcome to Guess my Number! You will attempt to guess the number I've chosen.")
playerName = input('What is your name?: ')

number = random.randint(1, 100)
guessAttempts = random.randint(5, 10)
print(f"Welcome {playerName}, I have chosen a number between 1 and 10 ({number}), you are allowed {guessAttempts} try's.")

for attempt in range(guessAttempts):
    print('Take a guess: ')
    guess = int(input())
    if guess < number:
        print('Too low, try again!')
    elif guess > number:
        print('Too high, try again!')
    elif guess == number:
        break

if guess == number:
    guessAttempts = str(guessAttempts - attempt - 1)
    attempt = str(attempt + 1)
    print(f"Good Job! {playerName}, you guessed correctly in {attempt} try's. You had a {guessAttempts} try's left. My number indeed was {number}! ")

if guess != number:
    number = str(number)
    print(f"You ran out of try's! My number was {number}")
