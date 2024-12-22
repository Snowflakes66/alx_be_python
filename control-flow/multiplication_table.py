

# (link unavailable)

def get_user_input():
    """Prompt user for a number"""
    while True:
        try:
            number = int(input("Enter a number to see its multiplication table: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def print_multiplication_table(number):
    """Generate and print the multiplication table"""
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

def main():
    number = get_user_input()
    print_multiplication_table(number)

if __name__ == "__main__":
    main()

