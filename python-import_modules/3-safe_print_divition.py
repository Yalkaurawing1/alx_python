#!/usr/bin/python3

# Define the function safe_print_division with two parameters a and b
def safe_print_division(a, b):
    # Initialize a variable result to None
    result = None

    # Use a try block to attempt the division
    try:
        # Assign the result of a divided by b to result
        result = a / b

    # Use an except block to handle the ZeroDivisionError
    except ZeroDivisionError:
        # Print an error message
        print("Cannot divide by zero")

    # Use a finally block to print the result
    finally:
        # Print the result using string format
        print("Inside result: {}".format(result))

        # Return the result
        return result