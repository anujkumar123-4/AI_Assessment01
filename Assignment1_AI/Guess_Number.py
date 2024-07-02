import random

def guess_number():
    print(" Guess the Number !")
    print("Choose a number between 1 and 100. You have to guess it.")

    number = random.randint(1, 100)
    attempt = 0

    while True:
        choice = int(input("Guess the number between 1 and 100: "))
        attempt =attempt + 1
        if choice < number:
            print("Number is low!")
        elif choice > number:
            print("Number is high!")
        else:
            print(f"You guessed the number {number} in {attempt} attempts,Congratulations!")
            break

guess_number()