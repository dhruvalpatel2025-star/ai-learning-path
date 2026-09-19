# This is a simple calculator that calculates the square of a number.
# The program defines a main() function that prompts the user for an integer input and calls the square() function to calculate the square of the input number.
def main():
    x = int(input("x = "))
    print ("The square of x is: ", square(x))

# The square() function takes an integer input 'n' and returns the square of 'n' by multiplying 'n' by itself. The function can also use the exponentiation operator '**' or the built-in pow() function to calculate the square.
def square(n):
    return n * n # Return the square of 'n'
    # return n ** 2
    # return pow(n, 2)

# Call the main() function to start the program.
main()