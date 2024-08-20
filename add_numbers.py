import sys

def add_numbers(number1, number2):
    return number1 + number2

if __name__ == "__main__":
    # Read the numbers from the command line arguments
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])
    
    # Call the function to add the numbers
    result = add_numbers(number1, number2)
    
    # Print the result
    print(f"The sum of {number1} and {number2} is {result}")
