def square_divide():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        result = (a ** 2) / b

        return result

    except ValueError:
        print("Error: Please enter valid numbers.")
        return None

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

result = square_divide()
if result is not None:
    print("Result:", result)
