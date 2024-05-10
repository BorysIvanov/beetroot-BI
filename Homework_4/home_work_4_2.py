p_number = int(input("Phone number: "))
spec_char = "!@#$%^&*-+?_=,()<>/"


while p_number > 10:
    print("Your number is invalid")
    p_number = int(input("Reenter phone number: "))

print(f"Your phone number is: {p_number}")



p_number = input("Phone number: ")
spec_char = "!@#$%^&*-+?_=,()<>/"


if p_number.isnumeric() and len(p_number) == 10:
    print("Phone number is valid")

elif p_number.isnumeric() and len(p_number) != 10:
    print("Phone number is invalid (must contain 10 digits only). Try again.")

elif p_number.isalpha():
    print("Number allowed only. Try again.")

elif any(i in spec_char for i in p_number):
    print("Special characters are not allowed. Try again")








