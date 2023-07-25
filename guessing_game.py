import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number bewtween 1 and 100.")
choice = random.randint(1,100)
print(f"Psst, the correct answer is {choice}.")
choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 5

def guess(choice):
    gue = int(input("Make a guess: "))
    if choice == gue:
        return True
    elif choice < gue:
        print("Too high.")
    else:
        print("Too low.")
    return False

def game(choice, attempts):
    while attempts:
        print(f"You have {attempts} remaining to guess the number.")
        if guess(choice):
            print(f"You got it! The answer was {choice}.")
            return
        else:
            print("Guess again.")
            attempts -= 1
    print("You've run out of guess, you lose.")  

if choose == "easy":
    attempts += 5
else:
    pass
game(choice, attempts)