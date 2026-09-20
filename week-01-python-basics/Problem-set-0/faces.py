# This program takes a string input from the user and replaces occurrences of ":)" with a smiling face emoji and ":(" with a sad face emoji. The modified string is then printed to the console.
# The program defines a main() function that prompts the user for a string input and calls the convert() function with the user's input as an argument. The convert() function replaces occurrences of ":)" with "🙂" and ":(" with "🙁" in the input string and returns the modified string. The main() function then prints the modified string to the console.
def main():
    inp_str = input("Enter a string: ")
    print(convert(inp_str)) # Call the convert() function with the user's input as an argument and print the modified string to the console.
    

def convert(inp_str): # The convert() function takes a string input and replaces occurrences of ":)" with "🙂" and ":(" with "🙁". It returns the modified string.
    inp_str = inp_str.replace(":)", "🙂").replace(":(", "🙁")
    return inp_str

main()