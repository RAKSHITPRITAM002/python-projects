import random
secret_number = random.randint(1, 100)
attempts = 0
print("Welcome to the game!")
print("Guess a number please it must be between 1 to 100:")
while True:
    try:
        guess = int(input("Enter the number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    attempts += 1
    if guess < secret_number:
        print("The number is too low! Try again.")
    elif guess > secret_number:
        print("The number is too high! Try again.")
    else:
        print("You have chosen the right number! Hooray, congrats")
        print(f"You guessed the number in {attempts} attempts")
        break