"""
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
(to keep things simple let it only be '+', '-' or '*') and an arbitrary number of
arguments (only numbers) as the second parameter.
Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation('+', 7, 7, 2) should return 16
the call make_operation('-', 5, 5, -10, -20) should return 30
the call make_operation('*', 7, 6) should return 42

"""


def make_operation(operator, *numbers):
    result = None

    if operator == '+':
        result = sum(numbers)
    elif operator == '-':
        result = numbers[0] - sum(numbers[1:])
    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num

    return result


def perform_math():
    while True:
        operator = input("Enter an operator (+, -, *), or 'STOP' to quit: ")
        if operator.upper() == 'STOP':
            print("Exiting...")
            break

        numbers = []
        while True:
            num = input("Enter a number (or type 'STOP' to quit): ")
            if num.upper() == 'STOP':
                break
            elif num:
                numbers.append(float(num))

        if operator.upper() != 'STOP':
            result = make_operation(operator, *numbers)

            # Output the result
            print("Result:", result)
            print()


if __name__ == "__main__":
    perform_math()

