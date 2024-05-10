stored_name = "borys"

input_name = input("What is your name?: ")

if stored_name == input_name.lower() or stored_name == input_name.upper():
    print("Hello " + stored_name.capitalize() + "!")

else:
    print("Not your name.")