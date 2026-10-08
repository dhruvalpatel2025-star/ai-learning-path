# Interpreter for simple arithmetic expressions

expression = input("Expression: ")

x, y, z = expression.split(" ") # Split the input expression into three parts: x (first number), y (operator), and z (second number)

# Convert x and z to float for arithmetic operations
x = float(x)
z = float(z)

if y == "+":
    result = x + z # use result operator to perform addition
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# Print the result formatted to one decimal place
print(f"{result:.1f}")