# This is a simple calculator that adds two floating point numbers and rounds the result to the nearest integer.
x = float(input("x = "))
y = float(input("y = "))

# Add round() function to round the sum of the two numbers to the nearest integer.
z = round(x + y)

# Print the rounded sum of the two numbers
print (z)

# Print the rounded sum of the two numbers with commas as thousands separators
print (f"{z:,}")