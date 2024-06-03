def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    else:
        return x / y

print("Choose your desired operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

selection = input("Enter your choice (1/2/3/4): ")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if selection == '1':
    print(number1, "+", number2, "=", addition(number1, number2))
elif selection == '2':
    print(number1, "-", number2, "=", subtraction(number1, number2))
elif selection == '3':
    print(number1, "*", number2, "=", multiplication(number1, number2))
elif selection == '4':
    print(number1, "/", number2, "=", division(number1, number2))
else:
    print("Invalid input. Please select a valid operation.")
