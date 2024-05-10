import random

def generate_random_strings(input_string, num_strings):
    characters = list(input_string)

    for string in range(num_strings):
        random.shuffle(characters)
        random_string = ''.join(characters)
        print(random_string)

if __name__ == "__main__":
    input_string = input("Enter a string: ")

    generate_random_strings(input_string, 5)

