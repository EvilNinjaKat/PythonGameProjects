import random

# generate random number between 1 and 100
number = random.randint(1, 100)

# initialize variables
guess = 0
tries = 0

# loop until user guesses the correct number
while guess != number:
    # ask user to guess a number
    guess = int(input("Guess a number between 1 and 100: "))
    
    # compare user's guess to random number
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    
    # increment the number of tries
    tries += 1

# print congratulatory message
print(f"Congratulations! You guessed the number in {tries} tries!")
