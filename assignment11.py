def check_conditions(a, b, c):
    if (a > b or b > c) and (a % 2 == 0 and c % 2 != 0) and (b != c):
        print("Conditions met")
    else:
        print("Conditions not met")

# Test the function
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
check_conditions(a, b, c)
1