# This script demonstrates exception handling in Python.
# It includes a try-except block to handle division by zero and invalid input.
# It also includes a generic exception handler to catch any other unexpected errors.
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError: # This exception is raised when the denominator is zero
    print("Error: Cannot divide by zero.") 
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.") #thus the finally block will always execute