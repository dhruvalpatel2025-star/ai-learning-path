# This program checks if a number is even or odd.
#x = int(input("x: "))

# Check if x is even or odd using the % operator
#if x % 2 == 0:
 #   print("x is even")
#else:
 #   print("x is odd")

# This program checks if a number is even or odd using a function.
def main():
    x = int(input("x: "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    if n % 2 == 0:  # noqa: SIM103
        return True
    else:
        return False

    # return True if n % 2 == 0 else False  # This is a more concise way to write the function
    # return (n % 2 == 0) # This is the most concise way to write the function

main()