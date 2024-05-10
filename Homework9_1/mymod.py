def test(name):
    try:
        with open(name, 'r') as file:
            # Count lines
            lines = count_lines(file)
            # Rewind the file
            file.seek(0)
            # Count characters
            chars = count_chars(file)
            print(f"Number of lines in {name}: {lines}")
            print(f"Number of characters in {name}: {chars}")
    except FileNotFoundError:
        print(f"File '{name}' not found.")
    except PermissionError:
        print(f"Permission denied to access file '{name}'.")

def count_lines(file):
    lines = file.readlines()
    return len(lines)

def count_chars(file):
    content = file.read()
    return len(content)