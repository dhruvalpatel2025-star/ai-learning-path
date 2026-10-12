words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    for word, point in  words.items():  # .tems() is a built-in dictionary method that returns a view object displaying a list of a dictionary’s key-value tuple pairs.
        print(f"{word} was worth {point} points.")

    while len(words) > 0:
        print(f"{len(words)} words left!")
        guess = input("Guess a word: ")

        # TODO: Check if guess in dictionary
        if guess == "GRAPHIC":
            words.clear() # .clear() is a built-in method used to remove all elements from mutable collections like lists, dictionaries, or sets in-place
            print("You've Won!!!")

        if guess in words.keys():
            points = words.pop(guess) # .pop() is a built-in list function used to remove and return an item from a list
            print(f"Good Job! You Scored {points} points")

    print("That's the game!")

main()