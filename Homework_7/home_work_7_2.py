def greet_on_next_birthday():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    next_age = age + 1
    print(f"Hello {name}, on your next birthday you’ll be {next_age} years.")

if __name__ == "__main__":
    greet_on_next_birthday()