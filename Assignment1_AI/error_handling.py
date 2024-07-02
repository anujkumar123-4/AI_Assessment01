def get_integer_input(prompt):
    while True:
        try:
            # Attempt to convert input to an integer
            return int(input(prompt))
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter an integer.")

def divide_numbers():
    try:
        num1 = get_integer_input("Enter the numerator: ")
        num2 = get_integer_input("Enter the denominator: ")
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"The result of dividing {num1} by {num2} is {result}")
    finally:
        print("Division operation completed.")

# Run the function
divide_numbers()
