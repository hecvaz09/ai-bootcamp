num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Add:", num1 + num2)
print("Subtract:", num1 - num2)
print("Multiply:", num1 * num2)

if num2 != 0:
    print("Divide:", num1 / num2)
else:
    print("Cannot divide by zero")
