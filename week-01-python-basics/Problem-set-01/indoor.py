# This program takes a string input from the user, converts it to lowercase, removes any leading or trailing whitespace, and then prints the modified string.
name = input("Type in capital letters: ")

# Convert to lowercase and remove leading/trailing whitespace
name = name.lower().strip()

print(name)