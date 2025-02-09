

def add_numbers():
    try:
        num1 = float(input("E1nter the first number: "))
        num2 = float(input("Enter the second number: "))
        total = num1 + num2
        print(f"The sum of {num1} and {num2} is: {total}")
    except ValueError:
        print("Please enter valid umbers!")

# Run the function
if __name__ == "__main__":
    add_numbers()

