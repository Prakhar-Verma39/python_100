from art4 import logo, vs
from game_data import data
import random



def choice():
    '''
    input: None
    output: a random object from 'data' dictionary
    '''
    return random.choice(data)

def print_info(choice):
    '''
    input: choice object
    output: formatted string
    '''
    return choice["name"] + ", " + choice["description"] + ", " + "from " + choice["country"] + "."


    

def game(choice_a, score):
    '''
    input : first choice and initial score
    output: None
    function: with the initialization of game, the game continues till user gets right bet
    otherwise final score is printed.
    '''
    print(logo)
    print("Compare A: " + print_info(choice_a))
    print(vs)
    choice_b = choice()
    while choice_a == choice_b:
        choice_b = choice()
    print("Against B: " + print_info(choice_b))
    bet = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if choice_a["follower_count"] > choice_b["follower_count"]:
        winner = 'A'
    else:
        winner = 'B'
    if winner == bet:
        score += 1
        game(choice_b, score)
    else:
        print(logo)
        print(f"Sorry,that's wrong. Final score: {score}")

choice_a = choice()
score = 0
game(choice_a, score)