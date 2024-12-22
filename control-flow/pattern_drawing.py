
# (link unavailable)

def get_pattern_size():
    """Prompt user for pattern size"""
    while True:
        try:
            size = int(input("Enter the size of the pattern: "))
            if size <= 0:
                print("Please enter a positive integer.")
            else:
                return size
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def draw_pattern(size):
    """Draw the pattern using nested loops"""
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()
        row += 1

def main():
    size = get_pattern_size()
    draw_pattern(size)

if __name__ == "__main__":
    main()

