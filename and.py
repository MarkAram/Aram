# Function to demonstrate parameter passing by value
def pass_by_value(x):
    x = 10
    print("Inside pass_by_value function:", x)

# Function to demonstrate parameter passing by variable
def pass_by_variable(y):
    y.append(4)
    print("Inside pass_by_variable function:", y)

# Function to demonstrate parameter passing by reference
def pass_by_reference(z):
    z['age'] = 30
    print("Inside pass_by_reference function:", z)

# Demonstration
if __name__ == "__main__":
    # Passing by value
    a = 5
    print("Before pass_by_value function call:", a)
    pass_by_value(a)
    print("After pass_by_value function call:", a)  # `a` remains unchanged

    # Passing by variable
    b = [1, 2, 3]
    print("\nBefore pass_by_variable function call:", b)
    pass_by_variable(b)
    print("After pass_by_variable function call:", b)  # `b` is modified

    # Passing by reference
    c = {'name': 'Alice', 'age': 25}
    print("\nBefore pass_by_reference function call:", c)
    pass_by_reference(c)
    print("After pass_by_reference function call:", c)  # `c` is modified
