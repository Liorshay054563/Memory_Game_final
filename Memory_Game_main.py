# Memory Game

import random

from Memory_Game_func import *

while True:  # big loop for "restart game" use
    board_one = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']  # the real cards
    random.shuffle(board_one)

    none_board = [f"[{i}]" for i in range(len(board_one))]  # same cards but none, cards by number for user pick

    game_data = {
        "player_a_name": input("Enter first player: "),  # input player A name
        "player_b_name": input("Enter second player: "),  # input player A name
        "player_a": 0,  # player A score
        "player_b": 0,  # player B score
        "play_again": None
    }
    options_restart()  # tell the player if they want restart game
    playerT = True  # change the player turn
    # inside loop for running the turns, and when press "R" will exit
    # this loop and start game again
    while any(card != "[]" for card in none_board):  # stop when all cards are "[]", no cards left
        try:

            if game_data["play_again"] == "R":  # if user enter "R",
                print("RESTART GAME")  # will restart the game
                break

            print_score(game_data)  # print the score
            print_board(none_board)  # print the board

            print(f"\n=== {game_data["player_a_name"] if playerT else game_data["player_b_name"]}'s turn ===")
            # run the player turn
            player_turn(board_one, none_board, playerT, game_data)

            options_restart()  # tell the player if they want restart game

            playerT = not playerT  # change turn to player B
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    # print the winner name
    print(
        f"\n=== {game_data["player_a_name"] if game_data["player_a"] > game_data["player_b"] else game_data["player_b_name"]} You are the Winner!! ===")

    print_score(game_data)  # the final score

    if game_data["play_again"] != "R":
        break  # if the game over the code NOT start again
    else:
        print("The game start again !")  # user press "R" , Restart the game
