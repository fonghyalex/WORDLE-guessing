import re


def request_input(intro: str):
    # Return flag
    flag = False
    while not flag:
        flag = True

        # Ask for input
        print(intro)
        # Input format: Letter + Spot (1-5)
        input_str = input("[Letter+Spot] e.g B2,C3,A5: ")
        # Input length validation
        if len(input_str) > 10:
            print("Error! Invalid length entered!")
            flag = False
            continue
        elif len(input_str) == 0:
            return {}

        # Deal with input
        str_arr = input_str.split(",", 4)
        str_dict = {}
        for st in str_arr:
            letter = list(st)[0]
            # Check letter
            if not re.match("^[A-Z]*$", letter.upper()):
                print("Error! Invalid character inputted!")
                flag = False
                break
            # Check spot
            try:
                spot = int(list(st)[1]) - 1
                if letter in str_dict:
                    str_dict[letter].append(spot)
                else:
                    str_dict[letter] = [spot]
            except ValueError:
                print("Error! Invalid spot value!")
                flag = False

        # Return dict
        if flag:
            return str_dict


def wasted_input():
    # Return flag
    flag = False
    while not flag:
        flag = True

        # Ask for input
        print("3. Enter WASTED letters this round.")
        # Input format: Letter + Spot (1-5)
        input_str = input("[Letter] e.g B,I,R,D,S: ")
        # Input length validation
        if len(input_str) > 9:
            print("Error! Invalid length entered!")
            flag = False
            continue
        wasted = []
        # Input letter validation
        for letter in input_str.split(","):
            if not re.match("^[A-Z]*$", letter.upper()):
                print("Error! Invalid character inputted!")
                flag = False
                break
            wasted.append(letter)

        # Return
        if flag:
            return wasted


def merge_input(game: dict, right: dict, wrong: dict, wasted: list):
    # Right
    # (Record letters and spots)
    if right:
        for letter, spot in right.items():
            game["right"][letter] = spot[0]

    # Wrong
    # (Record letters and wrong spots)
    if wrong:
        for letter in wrong.keys():
            if letter not in game["wrong"]:
                game["wrong"][letter] = []
            for spot in wrong[letter]:
                if spot not in game["wrong"][letter]:
                    game["wrong"][letter].append(spot)

    # Wasted
    # (Record wasted letters)
    if wasted:
        for letter in wasted:
            if letter not in game["wasted"]:
                game["wasted"].append(letter)

    return game
