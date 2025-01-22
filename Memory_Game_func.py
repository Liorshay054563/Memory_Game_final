# functions for Memory game

def print_board(none_board):
    """ print the current board play"""
    print(none_board[0:5])
    print(none_board[5:10])


def player_turn(board_one, none_board, playerT, game_data):
    """take card from user, check if same , update score"""

    while any(card != "[]" for card in none_board):  # stop the func when no cards available

        pick1 = valid_input(board_one, none_board, game_data)  # choose first card
        print(f"== {board_one[pick1]} ==")
        pick2 = valid_input(board_one, none_board, game_data)  # choose second card
        print(f"== {board_one[pick2]} ==")
        if pick1 == pick2 : # player pick the same card
            print("Pick tow different cards")
            continue # pick again
        elif board_one[pick1] != board_one[pick2]:
            print(f"\n Wrong cards, next player turn\n")
        elif board_one[pick1] == board_one[pick2]:  # if same
            print("Well play")
            if len(set(none_board)) > 4:  # in the last turn Don't print
                print("Go again")

            none_board[pick1] = "[]"  # change the board
            none_board[pick2] = "[]"

            # if same, update score
            if playerT:
                game_data["player_a"] += 1
                game_data["player_b"] += 0
            else:
                game_data["player_a"] += 0
                game_data["player_b"] += 1
            print_score(game_data) # print the current score
            print_board(none_board)  # print after changes
            player_turn(board_one, none_board, playerT, game_data)  # if same, player get turn again


        return  # stop the loop when the player pick wrong

    return  # stop the loop when no cards left


def valid_input(board_one, none_board,game_data):
    """check if the pick is on board, or is free"""

    while True:
        try:
            pick = input("Choose your [card] in the board by pick a number: ").upper()
            # "upper" - for case the user put lowercase for restart
            # the input is not "int" because  for "R" restart game
            if pick == "R":
                game_data["play_again"] = pick
                return
            if pick.isalpha():  # if user input letter, he chooses again
                print("Your choose must be a number")

            if int(pick) > len(board_one) or int(pick) < 0 or none_board[int(pick)] == "[]":
                print("your choose is not on board or not free, please choose again")
            else:
                return int(pick)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except NameError as e:
            print(e)


def print_score(game_data):
    """ print the current board score"""
    print(f"player {game_data["player_a_name"]} = {game_data["player_a"]} ")
    print(f"player {game_data["player_b_name"]} = {game_data["player_b"]} ")


def options_restart():
    """make the player know how to restart game"""
    print("If you want to restart the game enter 'R'")


if __name__ == "__main__":
    print("Only if this file is Main")

