import sys


def guess(game_spot:dict):
    # Prepare letters list
    right = game_spot["right"]
    wrong = game_spot["wrong"]
    waste = game_spot["wasted"]

    # Prepare available 5-letter vocabulary
    vocabs = []
    with open("./words.txt") as f:
        vocabs = f.readlines()

    # result
    ret = []

    # Filter invalid vocabs
    for word in vocabs:
        word = word.upper()
        valid = True
        # Filter out words without essential letters
        # 1st: Right letters with the right spots
        for letter, spot in right.items():
            if letter not in word or word[spot] != letter:
                valid = False
                break
        # Checkpoint
        if not valid:
            continue

        # 2nd: Wasted letters
        for letter in waste:
            if letter in word:
                valid = False
                break
        # Checkpoint
        if not valid:
            continue

        # 3rd: Right letters with the wrong spots
        for letter, spots in wrong.items():
            # Check if the letter exists
            if letter not in word:
                valid = False
                break
            # Check if the letter is in the wrong spots
            for spot in spots:
                if word[spot] == letter:
                    valid = False
                    break
            # Skip
            if not valid:
                break

        # Checkpoint
        if not valid:
            continue
        else:
            ret.append(word)

    # Show result
    print_result(ret)
    if len(ret) == 1:
        print(f"Congratulations! The answer of the game is: {ret[0]}")
        sys.exit(1)


def print_result(possible: list):
    total = len(possible)
    print(f"Total available words: {total}")
    count = 1
    for word in possible:
        word = word.replace("\n", "")
        print(f"{count}. {word}", end=" ")
        if count % 5 == 0:
            print("\n")
        count = count + 1
        print("\n")
    return

