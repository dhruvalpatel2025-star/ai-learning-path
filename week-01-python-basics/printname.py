# Ask user for their name
name = input("What is your name? ")

# Remove whitespace from string using strip() method
#name = name.strip()

# Print first letter of the name in uppercase using capitalize() method
#name = name.capitalize()

# Print the full name and their first letter of the name in uppercase using title() method
#name = name.title()

# Split user's name into first name and last name using split() method
first, last = name.split(" ")

# We can combine both strip() and title() methods to remove whitespace and capitalize the first letter of each word in the name.
name = name.strip().title()
# We can also combine both strip() and title() in the first line of the code to remove whitespace and capitalize the first letter of each word in the name.
# name = input("What is your name? ").strip().title()

# Print the name using print("Hello,", name)
# We can also print the name using print("Hello, " + name)
# We can also print it by using print ("Hello, ",end="") and then print(name) on the next line. This will print Hello, <name>! on the same line.
# We can also print it by using print ("Hello, ", name, sep="")

# This is called an f-string. It allows us to include variables inside a string by using curly braces {}.
print(f"Hello, {name}") 

# Print only first name
print(f"Your first name is {first}")

#print only last name
print(f"Your last name is {last}")
