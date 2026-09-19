x = float(input("x = "))
y = float (input("y = "))

# Divide the two numbers and round the result to 2 decimal places
z = round(x / y, 2)

print (z)

# Print the rounded result of the division with commas using f string formatting.
print (f"{z:.2f}")