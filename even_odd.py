def check_even_odd(number):
    """Check if a number is even or odd and print the result."""
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

# Example usage
num = int(input("Enter a number: "))
check_even_odd(num)
