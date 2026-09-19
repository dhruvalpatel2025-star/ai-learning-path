# Make a function by using the def() statement
# Print a greeting message to the user. The function takes an optional argument 'to' which defaults to "World!" if not provided. The function prints "hello, " followed by the value of 'to'.
def hello(to = "World!"):
    print ("hello, ", to) # Print the greeting message with the provided argument 'to'

name = input("Your name: ")
hello() # Call the hello() function without any arguments, which will use the default value "World!" for 'to'.
hello(name) # Call the hello() function with the user's input as an argument, which will print "hello, " followed by the user's name.