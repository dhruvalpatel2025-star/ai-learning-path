# This program checks the house of a character based on their name.
name = input("What is your name? ")

# Check the house of the character using if-elif-else statements
#if name == "Harry": 
 #   print("Gryffindor")
#elif name == "Ron":
 #   print("Gryffindor")
#elif name == "Hermione":
 #   print("Gryffindor")
#elif name == "Draco":
 #   print("Slytherin")
#else:
 #   print("Who?")

# The above code can be simplified using the 'or' operator to check for multiple names in a single condition.
#if name == "Harry" or name == "Ron" or name == "Hermione":
 #    print("Gryffindor")
#elif name == "Draco":
 #    print("Slytherin")
#else:
 #    print("Who?")

# We can also use the match statement to check for the house of the character based on their name.
#match name:
 #   case "Harry":
  #      print("Gryffindor")
   # case "Ron":
    #    print("Gryffindor")
    #case "Hermione":
     #   print("Gryffindor")
    #case "Draco":
    #    print("Slytherin")
    #case _:
     #   print("Who?")

# The match statement can be further simplified by using the '|' operator to check for multiple names in a single case.
match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")