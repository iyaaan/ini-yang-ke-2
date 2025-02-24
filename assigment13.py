def logical_operations(x, y):
    # Convert inputs to boolean
    bool_x = bool(x)
    bool_y = bool(y)

    print(f"Boolean value of x: {bool_x}")
    print(f"Boolean value of y: {bool_y}")
    
    # AND, OR, NOT, XOR operations
    print(f"x AND y: {bool_x and bool_y}")
    print(f"x OR y: {bool_x or bool_y}")
    print(f"NOT x: {not bool_x}")
    print(f"x XOR y: {bool_x != bool_y}")  # XOR using != (Exclusive OR)

# Test the function with different inputs
x = input("Enter value for x: ")
y = input("Enter value for y: ")

logical_operations(x, y)
