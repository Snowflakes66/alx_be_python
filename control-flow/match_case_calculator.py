# (link unavailable)

def get_user_input():
    """Prompt user for input"""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")
    return num1, num2, operation

def perform_calculation(num1, num2, operation):
    """Perform calculation using Match Case statement"""
    match operation:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                return "Cannot divide by zero."
            result = num1 / num2
        case _:
            return "Invalid operation."
    return result

def main():
    num1, num2, operation = get_user_input()
    result = perform_calculation(num1, num2, operation)
    if isinstance(result, str):
        print(result)
    else:
        print(f"The result is {result}.")

if __name__ == "__main__":
    main()

