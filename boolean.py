def demonstrate_boolean_operators():
    # Example variables
    a = True
    b = False

    # AND operator
    and_result1 = a and a  # True and True => True
    and_result2 = a and b  # True and False => False

    # OR operator
    or_result1 = a or b  # True or False => True
    or_result2 = b or b  # False or False => False

    # NOT operator
    not_result1 = not a  # not True => False
    not_result2 = not b  # not False => True

    # Display results
    print("AND operator results:")
    print(f"a and a: {and_result1}")
    print(f"a and b: {and_result2}\n")

    print("OR operator results:")
    print(f"a or b: {or_result1}")
    print(f"b or b: {or_result2}\n")

    print("NOT operator results:")
    print(f"not a: {not_result1}")
    print(f"not b: {not_result2}")

def main():
    demonstrate_boolean_operators()

if __name__ == "__main__":
    main()
