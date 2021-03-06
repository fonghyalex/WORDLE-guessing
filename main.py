# Author: Alex Fong
# Project name: Wordle guessing

from input import *
from guessing import *


def print_letters(game_spot: dict, turn: int):
    print(f"\n------ Turn {turn} WORDLE ------")
    # Right words
    rt_arr = ["_"] * 5
    for letter, spot in game_spot["right"].items():
        rt_arr[spot] = letter
    for letter in rt_arr:
        print(letter, end=" ")
    print("\n")

    # Wrong words
    print("Words with uncertain spot:")
    wr_str = ""
    for letter in game_spot["wrong"]:
        wr_str = wr_str + letter + " "
    print(wr_str)

    # Wasted words
    print("Wasted words:")
    wa_str = ""
    count = 0
    for letter in game_spot["wasted"]:
        wa_str = wa_str + letter + ", "
        count = count + 1
        if count > 10:
            print(f"{wa_str}\n")
            wa_str = ""
            count = 0
    print(wa_str)


if __name__ == '__main__':
    # Start from 2th round
    # Assume every 1st round starts with "AUDIO" -> A 5-letter word with most vowels
    turn = 1
    # Keep track game letters and spots
    game_spot = {
        "right": {},
        "wrong": {},
        "wasted": []
    }

    # Welcome message
    print("Welcome to the WORDLE guessing program.\nAuthor: Alex Fong\n")

    while turn < 6:
        # Ask for 3 inputs
        # 1st: Right letters with right spot
        turn_right_dict = request_input("1. Enter letters with the RIGHT spot.")

        # 2nd: Right letters with uncertain spot
        turn_wrong_dict = request_input("2. Enter letters with the WRONG spot.")

        # 3rd: Wasted letters
        turn_wasted = wasted_input()

        # Merge letters and spots
        game_spot = merge_input(game_spot, turn_right_dict, turn_wrong_dict, turn_wasted)

        # Report current status
        print_letters(game_spot, turn)

        # Guess
        guess(game_spot)

        turn = turn + 1

    print("Game failed... Good luck next time...")

