import math
import random
from art3 import logo

# all possible cards
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def init_game():
    start=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    game = {
        "p1": [],
        "p2": []
    }


    def choose_cards(player,no_of_cards):
        while no_of_cards:
            game[player].append(random.choice(cards))
            no_of_cards -= 1
        if 11 in game[player] and sum(game[player]) > 21:
            game[player].remove(11)
            game[player].append(1)
        


    def print_stat(cards, score, card):
        print(f"Your cards: {cards}, current score: {score}")
        print(f"Computer's first card: {card}")

    def result(p1_cards,p1_score,p2_cards,p2_score):
        print(f"Your final hand: {p1_cards}, final score: {p1_score}")
        print(f"Computer's final hand: {p2_cards}, final score: {p2_score}")

    def start_game():
        print(logo)
        
        p1_score = sum(game["p1"])
        if p1_score == 21 and len(game["p1"]) == 2:
            p1_score = 0

        p2_score = sum(game["p2"])
        if p2_score == 21 and len(game["p2"]) == 2:
            p2_score = 0


        if p1_score > 21:
            result(game["p1"],p1_score,game["p2"],p2_score)
            print(f"You went over.You lose")
            return

        

        print_stat(game["p1"],p1_score, game["p2"][0])

        game_continue = input("Type 'y' to get another card, type 'n' to pass: ")

        if game_continue == 'y':
            choose_cards("p1",1)
            choose_cards("p2",1)
            start_game()
        else:
            if p2_score != 0 and p2_score < 17:
                choose_cards("p2",1)
                p2_score = sum(game["p2"])
                if p2_score > 21:
                    result(game["p1"],p1_score,game["p2"],p2_score)
                    print(f"Opponent went over.You win.")
                    return


            result(game["p1"],p1_score,game["p2"],p2_score)
            if p1_score == 0:
                print("Win with a Blackjack")
            elif p2_score == 0:
                print("Lose, opponent has Blackjack ")
            elif p1_score > p2_score and p1_score <= 21:
                print(f"You win.")
            elif p2_score > p1_score and p2_score <= 21:
                print("You lose")
            elif p1_score <= 21 and p2_score > 21:
                print("Opponent went over.You win")
            else:
                print("Match draw.")

    


    if start == 'y':
        choose_cards("p1",2)
        choose_cards("p2",2)
        start_game()
    else:
        return
    init_game()
init_game()