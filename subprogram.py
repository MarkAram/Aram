# Define a function with parameters and return value
def add_numbers(a, b):
    """Function to add two numbers."""
    result = a + b
    return result

# Function with default parameter value
def greet(name="Anonymous"):
    """Function to greet a person."""
    print(f"Hello, {name}!")

# Function with variable number of arguments
def print_items(*args):
    """Function to print all arguments."""
    print("Printing items:")
    for item in args:
        print(item)

# Function with keyword arguments
def describe_person(name, age, **kwargs):
    """Function to describe a person."""
    print(f"Name: {name}, Age: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function with recursion
def factorial(n):
    """Recursive function to calculate factorial."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Function with lambda function
def apply_operation(x, y, operation):
    """Function to apply an operation."""
    return operation(x, y)

# Demonstration of functions
if __name__ == "__main__":
    # Call add_numbers function
    result = add_numbers(5, 3)
    print("Result of add_numbers:", result)

    # Call greet function
    greet("Alice")
    greet()  # Using default value

    # Call print_items function
    print_items("apple", "banana", "cherry")

    # Call describe_person function
    describe_person("Bob", 30, occupation="Engineer", city="New York")

    # Call factorial function
    print("Factorial of 5:", factorial(5))

    # Call apply_operation with a lambda function
    addition = apply_operation(10, 5, lambda x, y: x + y)
    print("Result of applying addition:", addition)
