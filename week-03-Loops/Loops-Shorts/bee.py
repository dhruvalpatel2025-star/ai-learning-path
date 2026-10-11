words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    for word, point in  words.items():
        print(f"{word} was worth {point} points.")

    while len(words) > 0:
        print(f"{len(words)} words left!")
        guess = input("Guess a word: ")

        # TODO: Check if guess in dictionary
        if guess == "GRAPHIC":
            words.clear()
            print("You've Won!!!")

        if guess in words.keys():
            points = words.pop(guess)
            print(f"Good Job! You Scored {points} points")

    print("That's the game!")

main()