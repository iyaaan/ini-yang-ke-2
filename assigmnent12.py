def check_input_types(input1, input2, input3):
    if isinstance(input1, str) and isinstance(input2, int) and isinstance(input3, float):
        return "Valid input types"
    else:
        return "Invalid input types"

# Test the function with different cases
print(check_input_types("Hello", 5, 3.14))  # Should return "Valid input types"
print(check_input_types("Hello", 5, "3.14"))  # Should return "Invalid input types"
print(check_input_types(3.14, 5, "Hello"))  # Should return "Invalid input types"
