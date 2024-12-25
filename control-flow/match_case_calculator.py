num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
operator = (input("Choose the operation (+, -, *, /): "))
sum = num1 + num2
sum = num1 - num2
sum = num1 * num2
sum = num1 / num2

match operator:
    case "+":
        print("addition")
    case "-":
        print("subtraction")
    case "*":
        print("multiplication")
    case "/":
        print("divide")
    case _:
        print("Cannot divide by zero")

print("The result is [sum].")