def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice not in (1, 2, 3, 4):
            raise ValueError
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input")
        continue

    if choice == 1:
        result = add(num1, num2)
        print(num1, "+", num2, "=", result)
    elif choice == 2:
        result = subtract(num1, num2)
        print(num1, "-", num2, "=", result)
    elif choice == 3:
        result = multiply(num1, num2)
        print(num1, "*", num2, "=", result)
    elif choice == 4:
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(num1, "/", num2, "=", result)

    print("The result is", result)

    # Print the ASCII art
    print("  /\   /\     .d88b    db    8       /\   /\   ")
    print(" (  O O  )    8P      dPYb   8      (  O O  )  ")
    print(" ( =^=^= )    8b     dPwwYb  8      ( =^=^= )  ")
    print("  ( \"_\" )    `Y88P dP    Yb 8888     ( \"_\" )   ")

    break

input("Press any key to exit")



