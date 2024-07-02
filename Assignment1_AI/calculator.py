def calculator():
    try:
        num1 = int(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ").strip()
        num2 = int(input("Enter second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation.")
            return

        print(f"Result: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()
